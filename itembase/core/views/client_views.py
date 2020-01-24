from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect  # ,  HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView as gen_CreateView
from django.views.generic.detail import SingleObjectMixin
from vanilla import CreateView, DeleteView, DetailView, UpdateView
from vanilla import ListView as ListView

from itembase.core.forms.client_forms import ClientForm
from itembase.core.forms.location_forms import LocationForm
from itembase.core.models import Client, Contact, Location, TeamMember


class ClientCreateView(SuccessMessageMixin, LoginRequiredMixin,
                       StaffuserRequiredMixin, CreateView):
    model = Client
    template_name = 'core/clients/client_new.html'

    form_class = ClientForm
    success_url = reverse_lazy('clients:list')
    success_message = "%(client_name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ClientUpdateView(SuccessMessageMixin, SingleObjectMixin, LoginRequiredMixin,
                       StaffuserRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'core/clients/client_edit.html'
    success_message = "%(client_name)s was updated successfully"

    def get_success_url(self):
        return reverse_lazy('clients:view', args=(self.object.slug,))


class ClientDetailView(LoginRequiredMixin,
                       StaffuserRequiredMixin, DetailView):
    model = Client
    template_name = 'core/clients/client_detail.html'
    context_object_name = 'client'
    slug_url_kwarg = 'slug'
    lookup_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.select_related(). \
            filter(client=self.object)
        context['contact_list'] = Contact.objects.select_related(). \
            filter(client=self.object).order_by('last_name').filter(Q(status='2') | Q(status='1'))
        context['team_list'] = TeamMember.objects.prefetch_related(). \
            filter(client=self.object).filter(status='2')
        return context


class ClientDeleteView(LoginRequiredMixin,
                       SuperuserRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('list')


class ClientListView(LoginRequiredMixin,
                     StaffuserRequiredMixin, ListView):
    # model = Client
    queryset = Client.objects.select_related('engagement').order_by('client_name')
    template_name = 'core/clients/client_list.html'
    context_object_name = 'client_list'


def validate_client_code(request):
    client_code = request.GET.get('client_code', None)
    data = {
        'is_taken': Client.objects.filter(client_code__iexact=client_code).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A client with this client code already exists.'
    # return HttpResponse(is_available)
    # return JsonResponse(is_available, safe=False)
    return JsonResponse(data)


class ClientLocationCreateView(SuccessMessageMixin, LoginRequiredMixin, gen_CreateView):
    model = Location
    template_name = 'core/locations/location_new.html'
    form_class = LocationForm
    # success_url = reverse_lazy('clients:view')
    success_message = "%(name)s was created successfully"

    def get_success_url(self):
        return reverse_lazy('clients:view', args=(self.object.slug,))

    def get_initial(self):
        client = get_object_or_404(Client, slug=self.kwargs.get('slug'))
        return {'client': client}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return redirect('clients:view', args=(self.object.slug,))
        # return super().form_valid(form)


