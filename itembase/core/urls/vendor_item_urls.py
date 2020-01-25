from django.urls import path

from itembase.core.views.item_views import UOMCreateView, UOMDeleteView, UOMDetailView, \
    UOMListView, UOMUpdateView, VendorItemCreateView, VendorItemDeleteView, VendorItemDetailView, \
    VendorItemListView, VendorItemUpdateView

app_name = "vendor-items"
urlpatterns = [
    path("uom/", UOMListView.as_view(), name="uom-list"),
    path("uom/new/", UOMCreateView.as_view(), name="uom-new"),
    path("uom/edit/<int:pk>/", UOMUpdateView.as_view(), name="uom-edit"),
    path("uom/delete/<int:pk>/", UOMDeleteView.as_view(), name="uom-delete"),
    path("uom/<int:pk>/", UOMDetailView.as_view(), name="uom-view"),
    path("vi/", VendorItemListView.as_view(), name="list"),
    path("vi/new/", VendorItemCreateView.as_view(), name="new"),
    path("vi/edit/<int:pk>/", VendorItemUpdateView.as_view(), name="edit"),
    path("vi/delete/<int:pk>/", VendorItemDeleteView.as_view(), name="delete"),
    path("vi/<int:pk>/", VendorItemDetailView.as_view(), name="view"),
]
