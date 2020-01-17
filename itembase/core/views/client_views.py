from braces import views
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from vanilla import CreateView, DeleteView, DetailView, UpdateView
from vanilla import ListView as ListView

from itembase.core.forms.client_forms import ClientForm
from itembase.core.models import Client


class ClientCreateView(SuccessMessageMixin, views.LoginRequiredMixin,
                       views.StaffuserRequiredMixin, CreateView):
    model = Client
    template_name = 'core/clients/client_new.html'

    form_class = ClientForm
    success_url = reverse_lazy('clients:list')
    success_message = "%(client_name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ClientUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin,
                       views.StaffuserRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'core/clients/client_edit.html'
    success_message = "%(client_name)s was updated successfully"

    def get_success_url(self):
        return reverse_lazy('clients:view', args=(self.object.slug,))


class ClientDetailView(views.LoginRequiredMixin,
                       views.StaffuserRequiredMixin, DetailView):
    model = Client
    template_name = 'core/clients/client_detail.html'
    context_object_name = 'client'
    slug_url_kwarg = 'slug'


class ClientDeleteView(views.LoginRequiredMixin,
                       views.StaffuserRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('list')


class ClientListView(views.LoginRequiredMixin,
                     views.StaffuserRequiredMixin, ListView):
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
