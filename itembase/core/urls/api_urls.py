from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from itembase.core.views.client_views import ClientAddressCreateListAPI, ClientCreateListAPI, \
    ClientDetailAPI, ClientAddressDetailAPI
from itembase.core.views.location_views import LocationCreateListAPI, LocationDetailAPI, \
    LocationAddressCreateListAPI, LocationAddressDetailAPI
from itembase.core.views.vendor_views import VendorDetailAPI, VendorCreateListAPI, \
    VendorAddressCreateListAPI, VendorAddressDetailAPI, VendorClientCreateListAPI, VendorClientDetailAPI, \
    VineVendorImportViewSet
from itembase.core.views.item_views import VendorItemCreateListAPI, VendorItemDetailAPI

app_name = "api"
urlpatterns = [
    # path("ajax/validate_client_code", validate_client_code, name="validate_client_code"),
    path("cas/", ClientAddressCreateListAPI.as_view()),
    path("cas/<int:pk>", ClientAddressDetailAPI.as_view()),
    path("clients/", ClientCreateListAPI.as_view()),
    path("clients/<int:pk>", ClientDetailAPI.as_view()),
    path("las/", LocationAddressCreateListAPI.as_view()),
    path("las/<int:pk>", LocationAddressDetailAPI.as_view()),
    path("locs/", LocationCreateListAPI.as_view()),
    path("locs/<int:pk>", LocationDetailAPI.as_view()),
    path("vendors/", VendorCreateListAPI.as_view()),
    path("vendors/<int:pk>", VendorDetailAPI.as_view()),
    path("vis/", VendorItemCreateListAPI.as_view()),
    path("vis/<int:pk>", VendorItemDetailAPI.as_view()),
    path("vas/", VendorAddressCreateListAPI.as_view()),
    path("vas/<int:pk>", VendorAddressDetailAPI.as_view()),
    path("vcs/", VendorClientCreateListAPI.as_view()),
    path("vcs/<int:pk>", VendorClientDetailAPI.as_view()),
    path("vineup/", VineVendorImportViewSet.as_view()),
]
