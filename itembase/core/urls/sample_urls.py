from django.urls import path

from iqms.core.views.test_views import MessageCreateView, MessageDeleteView, \
    MessageDetailView, MessageListView, MessageUpdateView


app_name = "messages"
urlpatterns = [
    # path("ajax/validate_client_code", validate_client_code, name="validate_client_code"),
    path("", MessageListView.as_view(), name="list"),
    path("new/", MessageCreateView.as_view(), name="new"),
    path("edit/<int:pk>/", MessageUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", MessageDeleteView.as_view(), name="delete"),
    path("<int:pk>/", MessageDetailView.as_view(), name="view"),
]
