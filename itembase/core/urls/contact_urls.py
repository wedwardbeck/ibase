from django.urls import path

from itembase.core.views.contact_views import (
    DetailContactView, CreateVendorContactView, DeleteContactView, ListContactView, UpdateClientContactView,
    CreateClientContactView, ContactsAggregateListView
    )

app_name = "contacts"
urlpatterns = [
    path('', ListContactView.as_view(), name='list'),
    path('new/', CreateVendorContactView.as_view(), name='new'),
    path('agg/', ContactsAggregateListView.as_view(), name='agg'),
    # path('<int:pk>/new-contact/', CreateVendorContactView.as_view(), name='vendor-contact-new'),
    # path('<int:pk>/address-new/', CreateContactAddressView.as_view(), name='address-new'),
    path('edit/<int:pk>/', UpdateClientContactView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteContactView.as_view(), name='delete'),
    path('<int:pk>/', DetailContactView.as_view(), name='view'),

]
