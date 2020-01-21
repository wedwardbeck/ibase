from braces import views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
# from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from django.views import generic
from vanilla import CreateView, DeleteView, DetailView, ListView as ListView, UpdateView

from itembase.utils.mixins import CancelMixin
from itembase.core.models import Client, HolidayList, TeamMember
from itembase.core.forms.staffing_forms import HolidayForm, TeamMemberForm


# Create your views here.


class HolidayCreateView(SuccessMessageMixin, views.LoginRequiredMixin,
                        views.StaffuserRequiredMixin, CreateView):
    model = HolidayList
    template_name = 'core/holidays/holiday_new.html'

    form_class = HolidayForm
    success_url = reverse_lazy('holidays:holidays-list')
    success_message = "%(name)s for %(date_from)s was created successfully"


class HolidayUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin,
                        views.StaffuserRequiredMixin, UpdateView):
    model = HolidayList
    form_class = HolidayForm
    success_url = reverse_lazy('staffing:holiday-list')
    template_name = 'core/holidays/holiday_edit.html'
    success_message = "%(holiday_name)s was updated successfully"


class HolidayDetailView(SingleObjectMixin, views.LoginRequiredMixin,
                        views.StaffuserRequiredMixin, DetailView):
    model = HolidayList
    form_class = HolidayForm
    template_name = 'core/holidays/holiday_detail.html'
    context_object_name = 'holiday'


class HolidayDeleteView(views.LoginRequiredMixin,
                        views.StaffuserRequiredMixin, DeleteView):
    model = HolidayList
    success_url = reverse_lazy('holidays-list')


class HolidayListView(views.LoginRequiredMixin,
                      views.StaffuserRequiredMixin, ListView):
    model = HolidayList
    template_name = 'core/holidays/holiday_list.html'
    context_object_name = 'holiday_list'


class TeamLeadListView(views.LoginRequiredMixin,
                       views.StaffuserRequiredMixin, ListView):
    model = TeamMember
    template_name = 'core/staffing/team_lead_list.html'
    context_object_name = 'lead_list'
    queryset = TeamMember.objects.filter(role__role__exact='Team Lead').filter(status=2)


class TeamListView(views.LoginRequiredMixin,
                   views.StaffuserRequiredMixin, ListView):
    model = TeamMember
    template_name = 'core/staffing/team_list.html'
    context_object_name = 'team_list'


class ProjectManagerListView(views.LoginRequiredMixin,
                             views.StaffuserRequiredMixin, ListView):
    model = TeamMember
    template_name = 'core/staffing/project_manager_list.html'
    context_object_name = 'pm_list'
    queryset = TeamMember.objects.filter(role__role__exact='Project Manager').filter(status=2)


class TeamMemberCreateView(SuccessMessageMixin, views.LoginRequiredMixin,
                           views.StaffuserRequiredMixin, CancelMixin, CreateView):
    model = TeamMember
    template_name = 'core/staffing/team_member_new.html'

    form_class = TeamMemberForm
    success_url = reverse_lazy('staff:team-list')
    success_message = "%(staff)s for %(client)s was created successfully"


class TeamMemberClientCreateView(SuccessMessageMixin, views.LoginRequiredMixin,
                                 views.StaffuserRequiredMixin, CancelMixin, generic.CreateView):
    model = TeamMember
    template_name = 'core/staffing/team_member_new.html'
    # template_name = 'core/staffing/team_member_client_new.html'

    form_class = TeamMemberForm
    # success_url = reverse_lazy('staff:team-list')
    success_message = "%(staff)s for %(client)s was created successfully"

    def get_initial(self):
        client = get_object_or_404(Client, slug=self.kwargs.get('slug'))
        return {'client': client}

    def get_success_url(self):
        return reverse('clients:view', args=(self.object.client.slug,))


class TeamMemberUpdateView(SuccessMessageMixin, SingleObjectMixin, views.LoginRequiredMixin,
                           views.StaffuserRequiredMixin, UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('staff:team-edit')
    template_name = 'core/staffing/team_member_edit.html'
    success_message = "%(holiday_name)s was updated successfully"


class TeamMemberDetailView(SingleObjectMixin, views.LoginRequiredMixin,
                           views.StaffuserRequiredMixin, DetailView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'core/staffing/team_member_detail.html'
    context_object_name = 'holiday'
