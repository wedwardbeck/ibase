from django.urls import path

from itembase.core.views.vendor_views import VendorAddressCreateView, VendorAddressDetailView, \
    VendorAddressUpdateView, VendorCreateView, VendorDeleteView, VendorDetailView, VendorListView, VendorUpdateView
from itembase.core.views.contact_views import VendorContactCreateView

app_name = "vendors"
urlpatterns = [
    path("", VendorListView.as_view(), name="vendor-list"),
    path("new/", VendorCreateView.as_view(), name="vendor-new"),
    path("edit/<int:pk>/", VendorUpdateView.as_view(), name="vendor-edit"),
    path("delete/<int:pk>/", VendorDeleteView.as_view(), name="vendor-delete"),
    path("<int:pk>/", VendorDetailView.as_view(), name="vendor-view"),
    path('<int:pk>/address-new/', VendorAddressCreateView.as_view(), name='vendor-address-new'),
    path('address/<int:pk>', VendorAddressDetailView.as_view(), name='vendor-address-view'),
    path('address/edit/<int:pk>', VendorAddressUpdateView.as_view(), name='vendor-address-edit'),
    path("upload/", VendorCreateView.as_view(), name="vendor-upload"),
    path('<int:pk>/contact-new/', VendorContactCreateView.as_view(), name='vendor-contact-new'),
]
