from braces import views
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import CreateView as gen_CreateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.views import APIView
# from rest_framework.parsers import FormParser, MultiPartParser
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView

from itembase.core.forms.vendor_forms import VendorForm, VendorAddressForm, VendorClientForm, VendorLocationForm
from itembase.core.models import Contact, Vendor, Address, VendorClientMatrix, VendorLocMatrix, \
    VineVendorImport, VineVendorFile
from itembase.core.serializers.vendors_drf import VendorSerializer, VendorAddressSerializer, \
    VendorClientSerializer, VineVendorSerializer
from itembase.utils.mixins import CancelMixin


class VendorCreateView(SuccessMessageMixin, views.LoginRequiredMixin, CreateView):
    model = Vendor
    template_name = 'core/vendors/vendor_new.html'
    form_class = VendorForm
    success_url = reverse_lazy('vendors:vendor-list')
    success_message = "%(name1)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class VendorUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin, UpdateView):
    model = Vendor
    form_class = VendorForm
    success_url = reverse_lazy('vendors:vendor-list')
    template_name = 'core/vendors/vendor_edit.html'
    success_message = "%(name1)s was updated successfully"


class VendorDetailView(SingleObjectMixin, views.LoginRequiredMixin, DetailView):
    model = Vendor
    form_class = VendorForm
    template_name = 'core/vendors/vendor_detail.html'
    context_object_name = 'vendor'

    def get_context_data(self, **kwargs):
        context = super(VendorDetailView, self).get_context_data(**kwargs)
        context['address_list'] = Address.objects.select_related(). \
            filter(vendor=self.object)
        context['contact_list'] = Contact.objects.select_related(). \
            filter(vendor=self.object).order_by('last_name').filter(Q(status='2') | Q(status='1'))
        context['locations_used'] = VendorLocMatrix.objects. \
            filter(vendor=self.object).annotate(location_count=Count('location'))

        return context


class VendorDeleteView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendors:vendors-list')


class VendorListView(views.LoginRequiredMixin, ListView):
    # model = Vendor
    queryset = Vendor.objects.select_related('created_by').annotate(item_count=Count('vendoritems')).order_by('name1')

    template_name = 'core/vendors/vendor_list.html'
    context_object_name = 'vendors'

    # def get_context_data(self, **kwargs):
    #     context = super(VendorListView, self).get_context_data(**kwargs)
    #     context['locations_used'] = VendorLocMatrix.objects.select_related(). \
    #         filter(vendor=self.object_list).annotate(location_count=Count('location')).filter(location_count__gt=0)
    #
    #     return context


class VendorAddressCreateView(SuccessMessageMixin, views.LoginRequiredMixin, views.StaffuserRequiredMixin,
                              CancelMixin, gen_CreateView):
    model = Address
    template_name = 'core/vendors/address_new.html'
    form_class = VendorAddressForm

    success_message = "%(vendor)s %(address_type)s address record was created successfully"

    def get_initial(self):
        vendor = get_object_or_404(Vendor, id=self.kwargs.get('pk'))
        used_on = 'V'
        return {'vendor': vendor, 'used_on': used_on}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('vendors:vendor-view', args=(self.object.vendor.id,))


class VendorAddressUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin, CancelMixin,
                              UpdateView):
    model = Address
    form_class = VendorAddressForm
    template_name = 'core/vendors/address_edit.html'
    success_message = "%(vendor)s %(address_type)s address was updated successfully"

    def get_success_url(self):
        return reverse_lazy('vendors:vendor-view', args=(self.object.vendor.id,))


class VendorAddressDetailView(SingleObjectMixin, views.LoginRequiredMixin, DetailView):
    model = Address
    form_class = VendorAddressForm
    template_name = 'core/vendors/address_detail.html'
    context_object_name = 'address'


class VendorAddressDeleteView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('vendors:vendors-list')


class VendorLocCreateView(SuccessMessageMixin, views.LoginRequiredMixin, views.StaffuserRequiredMixin,
                          CancelMixin, gen_CreateView):
    model = VendorLocMatrix
    template_name = 'core/vendors/vendor_loc_new.html'
    form_class = VendorLocationForm

    success_message = "%(vendor)s %(location)s record was created successfully"

    def get_initial(self):
        vendor = get_object_or_404(Vendor, id=self.kwargs.get('pk'))
        return {'vendor': vendor}

    def get_success_url(self):
        return reverse_lazy('vendors:vendor-view', args=(self.object.vendor.id,))


class VendorClientCreateView(SuccessMessageMixin, views.LoginRequiredMixin, views.StaffuserRequiredMixin,
                             CancelMixin, gen_CreateView):
    model = VendorClientMatrix
    template_name = 'core/vendors/vendor_client_new.html'
    form_class = VendorClientForm

    success_message = "%(vendor)s %(client)s record was created successfully"

    def get_initial(self):
        vendor = get_object_or_404(Vendor, id=self.kwargs.get('pk'))
        return {'vendor': vendor}

    def get_success_url(self):
        return reverse_lazy('vendors:vendor-view', args=(self.object.vendor.id,))


# API Region

class VendorCreateListAPI(ListCreateAPIView):
    queryset = Vendor.objects.all().select_related('created_by')
    serializer_class = VendorSerializer


class VendorDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all().select_related('created_by')
    serializer_class = VendorSerializer


class VendorAddressCreateListAPI(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = VendorAddressSerializer


class VendorAddressDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = VendorAddressSerializer


class VendorClientCreateListAPI(ListCreateAPIView):
    queryset = VendorClientMatrix.objects.all()
    serializer_class = VendorClientSerializer


class VendorClientDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = VendorClientMatrix.objects.all()
    serializer_class = VendorClientSerializer


#
# def vine_import_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/clients/logos/slug_client_<id>/<filename>
#     # return 'resources/res_None/{1}'.format(filename)
#     return 'clients/logos/{0}/{1}'.format(instance.slug, filename)


class VineVendorImportViewSet(ListCreateAPIView):
    queryset = VineVendorFile.objects.all()
    serializer_class = VineVendorSerializer



# endregion
