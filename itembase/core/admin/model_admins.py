# noinspection PyUnresolvedReferences
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from itembase.core.models import AddressType, Client, EngagementType, VendorItem, Location,  \
    LocationAddress, UnitOfMeasure, Vendor, VendorAddress

from .resources import AddressTypeResource, ClientResource, EngagementTypeResource, ItemDataResource, \
    LocationResource, LocationAddressResource, UnitOfMeasureResource, VendorResource, VendorAddressResource


# region Core Data

class AddressTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = AddressType
    resource_class = AddressTypeResource


class ClientAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Client
    list_display = ('client_code', 'client_name', 'engagement', 'production_support_number',
                    'upload_address', 'iq_support_address', 'imp_fee_status', 'client_status',
                    'approved', 'created_on')
    search_fields = ['client_code', 'client_name']
    resource_class = ClientResource


class EngagementTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = EngagementType
    list_display = ('service_description', 'service_abbreviation')
    ordering = ('service_description', 'service_abbreviation')
    resource_class = EngagementTypeResource


class ItemDataAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = VendorItem
    resource_class = ItemDataResource


class LocationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Location
    resource_class = LocationResource


class LocationAddressAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = LocationAddress
    resource_class = LocationAddressResource


class UnitOfMeasureAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = UnitOfMeasure
    resource_class = UnitOfMeasureResource


class VendorAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Vendor
    fields = ('name1', 'name2', 'taxid', 'parent', 'status', 'created_by')
    list_display = ('name1', 'name2', 'taxid', 'status', 'created_on', 'created_by')
    resource_class = VendorResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == Vendor:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()


class VendorAddressAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = VendorAddress
    resource_class = VendorAddressResource


# endregion


admin.site.register(AddressType, AddressTypeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(EngagementType, EngagementTypeAdmin)
admin.site.register(VendorItem, ItemDataAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationAddress, LocationAddressAdmin)
admin.site.register(UnitOfMeasure, UnitOfMeasureAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorAddress, VendorAddressAdmin)
