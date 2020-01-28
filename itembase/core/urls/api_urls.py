from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from itembase.core.views.client_views import ClientCreateListAPI, ClientDetailAPI
from itembase.core.views.location_views import LocationCreateListAPI, LocationDetailAPI
from itembase.core.views.vendor_views import VendorDetailAPI, VendorCreateListAPI, \
    VendorAddressCreateListAPI, VendorAddressDetailAPI, VendorClientCreateListAPI, VendorClientDetailAPI, \
    VineVendorImportViewSet
from itembase.core.views.item_views import VendorItemCreateListAPI, VendorItemDetailAPI

app_name = "api"
urlpatterns = [
    # path("ajax/validate_client_code", validate_client_code, name="validate_client_code"),
    path("client/", ClientCreateListAPI.as_view()),
    path("client/<int:pk>", ClientDetailAPI.as_view()),
    path("loc/", LocationCreateListAPI.as_view()),
    path("loc/<int:pk>", LocationDetailAPI.as_view()),
    path("vendor/", VendorCreateListAPI.as_view()),
    path("vendor/<int:pk>", VendorDetailAPI.as_view()),
    path("vi/", VendorItemCreateListAPI.as_view()),
    path("vi/<int:pk>", VendorItemDetailAPI.as_view()),
    path("va/", VendorAddressCreateListAPI.as_view()),
    path("va/<int:pk>", VendorAddressDetailAPI.as_view()),
    path("vc/", VendorClientCreateListAPI.as_view()),
    path("vc/<int:pk>", VendorClientDetailAPI.as_view()),
    path("vineup/", VineVendorImportViewSet.as_view()),
]
