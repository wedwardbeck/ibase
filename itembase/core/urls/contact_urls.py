from django.urls import path

from itembase.core.views.contact_views import (
    ContactDetailView, VendorContactCreateView, ContactDeleteView, ContactListView, ClientContactUpdateView,
    ClientContactCreateView, ContactsAggregateListView
    )

app_name = "contacts"
urlpatterns = [
    path('', ContactListView.as_view(), name='list'),
    path('new/', VendorContactCreateView.as_view(), name='new'),
    path('agg/', ContactsAggregateListView.as_view(), name='agg'),
    # path('<int:pk>/new-contact/', CreateVendorContactView.as_view(), name='vendor-contact-new'),
    # path('<int:pk>/address-new/', CreateContactAddressView.as_view(), name='address-new'),
    path('edit/<int:pk>/', ClientContactUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ContactDeleteView.as_view(), name='delete'),
    path('<int:pk>/', ContactDetailView.as_view(), name='view'),

]
