from django.urls import path

from itembase.core.views.client_views import ClientCreateView, ClientDeleteView, \
    ClientDetailView, ClientListView, ClientUpdateView, validate_client_code
from itembase.core.views.contact_views import CreateClientContactView

app_name = "clients"
urlpatterns = [
    path("ajax/validate_client_code", validate_client_code, name="validate_client_code"),
    path("", ClientListView.as_view(), name="list"),
    path("new/", ClientCreateView.as_view(), name="new"),
    path("edit/<slug:slug>/", ClientUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", ClientDeleteView.as_view(), name="delete"),
    path("<slug>/", ClientDetailView.as_view(), name="view"),
    path('<slug:slug>/new-contact/', CreateClientContactView.as_view(), name='client-contact-new'),
]
