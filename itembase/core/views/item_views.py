from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, SuperuserRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from itembase.utils.mixins import CancelMixin
from django.views.generic.detail import SingleObjectMixin
# from django.views.generic import CreateView as gen_CreateView
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView
from itembase.core.forms.item_forms import UOMForm, VendorItemForm
from itembase.core.models import VendorItem, UnitOfMeasure


class UOMCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = UnitOfMeasure
    template_name = 'core/items/uom_new.html'
    form_class = UOMForm
    success_url = reverse_lazy('vendor-items:uom-list')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UOMUpdateView(SuccessMessageMixin, SingleObjectMixin, LoginRequiredMixin, UpdateView):
    model = UnitOfMeasure
    form_class = UOMForm
    success_url = reverse_lazy('vendor-items:uom-list')
    template_name = 'core/items/uom_edit.html'
    success_message = "%(name)s was updated successfully"


class UOMDetailView(SingleObjectMixin, LoginRequiredMixin, DetailView):
    model = UnitOfMeasure
    form_class = UOMForm
    template_name = 'core/items/uom_detail.html'
    context_object_name = 'uom'

    # def get_context_data(self, **kwargs):
    #     context = super(VendorItemDetailView, self).get_context_data(**kwargs)
    #     context['address_list'] = Location.objects.select_related(). \
    #         filter(item=self.object)
    #     return context
    # TODO: Using where used table, add in related vendor records to show in item detail which locations
    #  use item if where used on location is feasible - pseudo code above - need interim relation on vendor to loc


class UOMDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = UnitOfMeasure
    success_url = reverse_lazy('vendor-items-list')
    # TODO: replace direct edit/delete with a workflow/event approval flow


class UOMListView(LoginRequiredMixin, ListView):
    model = UnitOfMeasure
    template_name = 'core/items/uom_list.html'
    context_object_name = 'uom'


class VendorItemCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = VendorItem
    template_name = 'core/items/vendor_item_new.html'
    form_class = VendorItemForm
    success_url = reverse_lazy('vendor-items:list')
    success_message = "%(item_number)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class VendorItemUpdateView(SuccessMessageMixin, SingleObjectMixin, LoginRequiredMixin, UpdateView):
    model = VendorItem
    form_class = VendorItemForm
    success_url = reverse_lazy('vendor-items:list')
    template_name = 'core/items/vendor_item_edit.html'
    success_message = "%(item_number)s was updated successfully"


class VendorItemDetailView(SingleObjectMixin, LoginRequiredMixin, DetailView):
    model = VendorItem
    form_class = VendorItemForm
    template_name = 'core/items/vendor_item_detail.html'
    context_object_name = 'vendor_item'


class VendorItemDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = VendorItem
    success_url = reverse_lazy('vendor-items-list')


class VendorItemListView(LoginRequiredMixin, ListView):
    # model = VendorItem
    queryset = VendorItem.objects.select_related('created_by', 'vendor', 'uom').\
        order_by('vendor__name1', 'item_number')
    template_name = 'core/items/vendor_item_list.html'
    context_object_name = 'vendor_items'
