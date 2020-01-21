from django.urls import path

from itembase.core.views.staffing_views import ProjectManagerListView, TeamLeadListView, TeamListView, \
    TeamMemberCreateView, TeamMemberClientCreateView, TeamMemberDetailView, TeamMemberUpdateView


app_name = "staff"
urlpatterns = [
    # Client URL Patterns
    path('', TeamListView.as_view(), name='team-list'),
    path('pm/', ProjectManagerListView.as_view(), name='pm-list'),
    path('tl/', TeamLeadListView.as_view(), name='teamlead-list'),
    path('newtm/', TeamMemberCreateView.as_view(), name='team-new'),
    path('newtm/<slug:slug>/', TeamMemberClientCreateView.as_view(), name='client-team-new'),
    path('<int:pk>/', TeamMemberDetailView.as_view(), name='team-view'),
    path('edittm/', TeamMemberUpdateView.as_view(), name='team-edit'),

]
