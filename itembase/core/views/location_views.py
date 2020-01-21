from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from itembase.utils.mixins import CancelMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import CreateView as gen_CreateView
# from django.views.generic import UpdateView
from vanilla import CreateView, DeleteView, DetailView, ListView,  UpdateView
from itembase.core.forms.location_forms import LocationForm, LocationAddressForm
from itembase.core.models import Location, LocationAddress


class LocationCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'core/locations/location_new.html'
    form_class = LocationForm
    success_url = reverse_lazy('locations:list')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LocationUpdateView(SuccessMessageMixin, SingleObjectMixin, LoginRequiredMixin,
                         StaffuserRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('locations:list')
    template_name = 'core/locations/location_edit.html'
    success_message = "%(name)s was updated successfully"


class LocationDetailView(SingleObjectMixin, LoginRequiredMixin, DetailView):
    model = Location
    form_class = LocationForm
    template_name = 'core/locations/location_detail.html'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        context['address_list'] = LocationAddress.objects.select_related(). \
            filter(location=self.object)
        return context


class LocationDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('locations-list')


class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'core/locations/location_list.html'
    context_object_name = 'locations'


class LocationAddressCreateView(SuccessMessageMixin, LoginRequiredMixin, StaffuserRequiredMixin,
                                CancelMixin, gen_CreateView):
    model = LocationAddress
    template_name = 'core/locations/address_new.html'
    form_class = LocationAddressForm

    success_message = "%(location)s %(address_type)s address record was created successfully"

    def get_initial(self):
        location = get_object_or_404(Location, id=self.kwargs.get('pk'))
        return {'location': location}

    def get_success_url(self):
        return reverse_lazy('locations:view', args=(self.object.location.id,))


class LocationAddressUpdateView(SuccessMessageMixin, SingleObjectMixin, LoginRequiredMixin, CancelMixin,
                                UpdateView):
    model = LocationAddress
    form_class = LocationAddressForm
    template_name = 'core/locations/address_edit.html'
    success_message = "%(location)s %(address_type)s address was updated successfully"

    def get_success_url(self):
        return reverse_lazy('locations:view', args=(self.object.location.id,))


class LocationAddressDetailView(SingleObjectMixin, LoginRequiredMixin, DetailView):
    model = LocationAddress
    form_class = LocationAddressForm
    template_name = 'core/locations/address_detail.html'
    context_object_name = 'address'


class LocationAddressDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = LocationAddress
    success_url = reverse_lazy('locations-list')
