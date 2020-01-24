from django.urls import path

from itembase.core.views.location_views import LocationAddressCreateView, LocationAddressDetailView, \
    LocationAddressUpdateView, LocationCreateView, LocationDeleteView, LocationDetailView, LocationListView, \
    LocationUpdateView, get_locations

app_name = "locations"
urlpatterns = [
    path("", LocationListView.as_view(), name="list"),
    path("new/", LocationCreateView.as_view(), name="new"),
    path("edit/<int:pk>/", LocationUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", LocationDeleteView.as_view(), name="delete"),
    path("<int:pk>/", LocationDetailView.as_view(), name="view"),
    path('<int:pk>/address-new/', LocationAddressCreateView.as_view(), name='address-new'),
    path('address/<int:pk>', LocationAddressDetailView.as_view(), name='address-view'),
    path('address/edit/<int:pk>', LocationAddressUpdateView.as_view(), name='address-edit'),
]
