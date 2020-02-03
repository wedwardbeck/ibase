from braces import views
from django.urls import reverse_lazy
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.views import generic
from vanilla import DetailView, GenericView, ListView

from itembase.core.models import Address, Client, Vendor, VendorItem
from itembase.users.models import User

#
# class HomePageViews(views.LoginRequiredMixin,
#                     views.StaffuserRequiredMixin, generic.ListView):
#
#     model = Client
#     context_object_name = 'client_list'
#     template_name = 'pages/home.html'
#     # queryset = Client.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePageViews, self).get_context_data(**kwargs)
#         context['users'] = User.objects.all()
#         context['contacts'] = Contact.objects.all().select_related()
#         return context
