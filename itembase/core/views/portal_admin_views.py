from braces.views import StaffuserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView


# Views

