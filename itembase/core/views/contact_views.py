from braces.views import StaffuserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404  # , redirect, HttpResponseRedirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from itembase.utils.mixins import CancelMixin
from itembase.core.models import Client, Contact, Vendor
from itembase.core.forms.contact_forms import ClientContactForm, VendorContactForm
from django.db.models import Count


# Create your views here.


class ClientContactCreateView(SuccessMessageMixin, LoginRequiredMixin, StaffuserRequiredMixin,
                              CreateView):
    model = Contact
    template_name = 'core/contacts/contact_new.html'
    form_class = ClientContactForm

    success_message = "%(first_name)s %(last_name)s contact record was created successfully"

    def get_initial(self):
        client = get_object_or_404(Client, slug=self.kwargs.get('slug'))
        return {'client': client, 'contact_type': 2}

    def get_success_url(self):
        return reverse('clients:view', args=(self.object.client.slug,))


class ClientContactUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Contact
    template_name = 'core/contacts/contact_edit.html'
    form_class = ClientContactForm

    def get_success_url(self):
        return reverse('contacts:list')


class ContactListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Contact
    template_name = 'core/contacts/contact_list.html'
    context_object_name = 'contact_list'
    queryset = Contact.objects.prefetch_related('client')

    # def get_queryset(self, **kwargs):
    #     queryset = Contact.


class VendorContactCreateView(CancelMixin, SuccessMessageMixin, LoginRequiredMixin, StaffuserRequiredMixin,
                              CreateView):
    model = Contact
    template_name = 'core/contacts/contact_new.html'
    form_class = VendorContactForm

    success_message = "%(first_name)s %(last_name)s contact record was created successfully"

    def get_initial(self):
        vendor = get_object_or_404(Vendor, id=self.kwargs.get('pk'))
        return {'vendor': vendor}

    def get_success_url(self):
        return reverse('contacts:list')


class VendorContactUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Contact
    template_name = 'core/contacts/contact_edit.html'
    form_class = VendorContactForm

    def get_success_url(self):
        return reverse('contacts:list')


class ContactDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = Contact
    template_name = 'core/contacts/contact_delete.html'

    def get_success_url(self):
        return reverse('contacts:list')


class ContactDetailView(LoginRequiredMixin, StaffuserRequiredMixin, DetailView):
    model = Contact
    template_name = 'core/contacts/contact_detail.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        return context


class ContactsAggregateListView(StaffuserRequiredMixin, ListView):
    model = Client
    template_name = 'core/contacts/contact_agg_list.html'
    fields = '__all__'

    # clients = Contact.objects.aggregate(contacts_count=Count('contact'))

    def get_context_data(self, **kwargs):
        context = super(ContactsAggregateListView, self).get_context_data(**kwargs)
        context['client_agg'] = Client.objects.values('client_code'). \
            annotate(contacts_count=Count('contact')).filter(contacts_count__gt=0)

        return context
