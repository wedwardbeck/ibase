from import_export import resources
# from import_export.widgets import ForeignKeyWidget

from itembase.core.models import EngagementType, Client, Vendor, UnitOfMeasure, VendorItem, Location, AddressType, \
    LocationAddress, VendorAddress


# region Core Data
class AddressTypeResource(resources.ModelResource):
    class Meta:
        model = AddressType


class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('id', 'client_code', 'client_name', 'engagement',
                  'imp_fee_status', 'client_status', 'slug', 'production_support_number',
                  'approved', 'upload_address', 'iq_support_address', 'parent')
        skip_unchanged = True


class ItemDataResource(resources.ModelResource):
    class Meta:
        model = VendorItem
        fields = ('id', 'item_number', 'description', 'vendor', 'uom',
                  'pack_count', 'status', 'created_by', 'created_on')
        skip_unchanged = True


class EngagementTypeResource(resources.ModelResource):
    class Meta:
        model = EngagementType


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location


class LocationAddressResource(resources.ModelResource):
    class Meta:
        model = LocationAddress
        skip_unchanged = True


class UnitOfMeasureResource(resources.ModelResource):
    class Meta:
        model = UnitOfMeasure


class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor


class VendorAddressResource(resources.ModelResource):
    class Meta:
        model = VendorAddress
        skip_unchanged = True

# endregion
