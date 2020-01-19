from braces import views
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from itembase.utils.mixins import CancelMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import CreateView as gen_CreateView
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView
from itembase.core.forms.vendor_forms import VendorForm, VendorAddressForm
from itembase.core.models import Vendor, VendorAddress


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
    success_message = "%(vendor_name)s was updated successfully"


class VendorDetailView(SingleObjectMixin, views.LoginRequiredMixin, DetailView):
    model = Vendor
    form_class = VendorForm
    template_name = 'core/vendors/vendor_detail.html'
    context_object_name = 'vendor'

    def get_context_data(self, **kwargs):
        context = super(VendorDetailView, self).get_context_data(**kwargs)
        context['address_list'] = VendorAddress.objects.select_related(). \
            filter(vendor=self.object)
        return context


class VendorDeleteView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendors:vendors-list')


class VendorListView(views.LoginRequiredMixin, ListView):
    # model = Vendor
    queryset = Vendor.objects.select_related('created_by').annotate(item_count=Count('vendoritems')).order_by('name1')

    template_name = 'core/vendors/vendor_list.html'
    context_object_name = 'vendors'


class VendorAddressCreateView(SuccessMessageMixin, views.LoginRequiredMixin, views.StaffuserRequiredMixin,
                              CancelMixin, gen_CreateView):
    model = VendorAddress
    template_name = 'core/vendors/address_new.html'
    form_class = VendorAddressForm

    success_message = "%(vendor)s %(address_type)s address record was created successfully"

    def get_initial(self):
        vendor = get_object_or_404(Vendor, id=self.kwargs.get('pk'))
        print(vendor)
        return {'vendor': vendor}

    def get_success_url(self):
        return reverse_lazy('vendors:vendor-view', args=(self.object.vendor.id,))


class VendorAddressUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin, CancelMixin,
                              UpdateView):
    model = VendorAddress
    form_class = VendorAddressForm
    template_name = 'core/vendors/address_edit.html'
    success_message = "%(vendor)s %(address_type)s address was updated successfully"

    def get_success_url(self):
        return reverse_lazy('vendors:vendor-view', args=(self.object.vendor.id,))


class VendorAddressDetailView(SingleObjectMixin, views.LoginRequiredMixin, DetailView):
    model = VendorAddress
    form_class = VendorAddressForm
    template_name = 'core/vendors/address_detail.html'
    context_object_name = 'address'


class VendorAddressDeleteView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, DeleteView):
    model = VendorAddress
    success_url = reverse_lazy('vendors:vendors-list')

