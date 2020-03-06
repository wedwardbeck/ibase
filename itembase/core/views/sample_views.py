from braces import views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import SingleObjectMixin
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView
from iqms.core.forms.test_forms import MessageForm
from iqms.core.models import Message


# Create your views here.

# region Message Views


class MessageCreateView(SuccessMessageMixin, views.LoginRequiredMixin,
                     views.StaffuserRequiredMixin, CreateView):
    model = Message
    template_name = 'core/tests/message_new.html'
    form_class = MessageForm
    success_url = reverse_lazy('messages:list')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MessageUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin,
                     views.StaffuserRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('messages:list')
    template_name = 'core/tests/message_edit.html'
    success_message = "%(name)s was updated successfully"


class MessageDetailView(SingleObjectMixin, views.LoginRequiredMixin,
                     views.StaffuserRequiredMixin, DetailView):
    model = Message
    form_class = MessageForm
    template_name = 'core/tests/message_detail.html'
    context_object_name = 'message'


class MessageDeleteView(views.LoginRequiredMixin,
                     views.StaffuserRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('list')


class MessageListView(views.LoginRequiredMixin,
                   views.StaffuserRequiredMixin, ListView):
    model = Message
    template_name = 'core/tests/message_list.html'
    context_object_name = 'message_list'


# endregion
