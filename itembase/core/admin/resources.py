from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from itembase.core.models import AddressType, Brand, Client, ClientSystem, Contact, EngagementType, FeeGroup, \
    FeeItem, HolidayList, InstallBase, Location, LocationAddress, UnitOfMeasure, StaffMember, \
    StaffRoles, StaffShift, StaffTitle, System, SystemType, TeamMember, Vendor, VendorAddress, VendorItem


# region Core Data
class AddressTypeResource(resources.ModelResource):
    class Meta:
        model = AddressType


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('id', 'client_code', 'client_name', 'engagement',
                  'imp_fee_status', 'client_status', 'slug', 'production_support_number',
                  'approved', 'upload_address', 'iq_support_address', 'parent')
        skip_unchanged = True


class ClientSystemResource(resources.ModelResource):
    client = fields.Field(column_name='client',
                          attribute='client',
                          widget=ForeignKeyWidget(Client, 'client_code'))

    class Meta:
        model = ClientSystem
        fields = ('client', 'system')
        skip_unchanged = True


class ContactResource(resources.ModelResource):
    client = fields.Field(column_name='client',
                          attribute='client',
                          widget=ForeignKeyWidget(Client, 'client_code'))

    class Meta:
        model = Contact
        fields = ('id', 'client', 'client__client_name', 'first_name', 'last_name', 'title', 'email',
                  'contact_type', 'vendor', 'is_valid')
        export_order = ('id', 'client', 'client__client_name', 'first_name', 'last_name', 'title', 'email',
                        'contact_type', 'vendor', 'is_valid')


class EngagementTypeResource(resources.ModelResource):
    class Meta:
        model = EngagementType


class FeeGroupResource(resources.ModelResource):
    class Meta:
        model = FeeGroup
        fields = ('id', 'name', 'description')
        skip_unchanged = True


class FeeItemResource(resources.ModelResource):
    fee_group = fields.Field(column_name='fee_group',
                             attribute='fee_group',
                             widget=ForeignKeyWidget(FeeGroup, 'name'))

    class Meta:
        model = FeeItem
        fields = ('id', 'item', 'description', 'fee_group')
        skip_unchanged = True


class HolidayListResource(resources.ModelResource):
    class Meta:
        model = HolidayList
        skip_unchanged = True


class InstallBaseResource(resources.ModelResource):
    class Meta:
        model = InstallBase
        skip_unchanged = True


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location


class LocationAddressResource(resources.ModelResource):
    class Meta:
        model = LocationAddress
        skip_unchanged = True


class StaffRolesResource(resources.ModelResource):
    class Meta:
        model = StaffRoles


class StaffMemberResource(resources.ModelResource):
    title = fields.Field(column_name='title',
                         attribute='title',
                         widget=ForeignKeyWidget(StaffTitle, 'title'))

    class Meta:
        model = StaffMember
        skip_unchanged = True


class StaffShiftResource(resources.ModelResource):
    class Meta:
        model = StaffShift


class StaffTitlesResource(resources.ModelResource):
    class Meta:
        model = StaffTitle


class SystemResource(resources.ModelResource):
    class Meta:
        model = System


class SystemTypeResource(resources.ModelResource):
    class Meta:
        model = SystemType


class TeamMemberResource(resources.ModelResource):
    client = fields.Field(column_name='client',
                          attribute='client',
                          widget=ForeignKeyWidget(Client, 'client_code'))

    class Meta:
        model = TeamMember


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


class VendorItemDataResource(resources.ModelResource):
    class Meta:
        model = VendorItem
        fields = ('id', 'item_number', 'description', 'vendor', 'uom',
                  'pack_count', 'status', 'created_by', 'created_on')
        skip_unchanged = True

# endregion
