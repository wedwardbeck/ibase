# noinspection PyUnresolvedReferences
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from itembase.core.models import AddressType, Brand, Client, ClientSystem, Contact, EngagementType, FeeGroup, \
    FeeItem, HolidayList, InstallBase, Location, LocationAddress, StaffMember, StaffRoles, StaffShift, \
    StaffTitle, System, SystemType, TeamMember, UnitOfMeasure, Vendor, VendorAddress, VendorItem

from .resources import AddressTypeResource, BrandResource, ClientResource, ClientSystemResource, ContactResource, \
    EngagementTypeResource, FeeGroupResource, FeeItemResource, HolidayListResource, InstallBaseResource, \
    LocationResource, LocationAddressResource, StaffMemberResource, StaffRolesResource, StaffShiftResource, \
    StaffTitlesResource, SystemResource, SystemTypeResource, TeamMemberResource, UnitOfMeasureResource, \
    VendorResource, VendorAddressResource, VendorItemDataResource


# region Core Data

class AddressTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = AddressType
    resource_class = AddressTypeResource


class BrandAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Brand
    search_fields = ['name']
    resource_class = BrandResource
    ordering = ('name',)


class ClientAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Client
    list_display = ('client_code', 'client_name', 'engagement', 'production_support_number',
                    'upload_address', 'iq_support_address', 'imp_fee_status', 'client_status',
                    'approved', 'created_on')
    search_fields = ['client_code', 'client_name']
    resource_class = ClientResource


class ClientSystemAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    fields = ('client', 'system')
    list_display = ('client', 'system', 'get_version', 'created_on')
    resource_class = ClientSystemResource
    list_select_related = ['client', 'client']
    ordering = ('-system', 'client',)

    search_fields = ['system']

    def queryset(self, request):
        return super(ClientSystemAdmin, self).get_queryset(request).select_related('system', 'system_version')

    def get_version(self, obj):
        return obj.system.system_version

    get_version.short_description = 'Version'
    get_version.admin_order_field = 'brand'


class ContactAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Contact
    list_display = ('client', 'first_name', 'last_name', 'title', 'email',
                    'contact_type', 'vendor', 'created_on', 'status')
    list_select_related = ['client', 'vendor']
    resource_class = ContactResource
    ordering = ('first_name', 'last_name')


class EngagementTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = EngagementType
    list_display = ('service_description', 'service_abbreviation')
    ordering = ('service_description', 'service_abbreviation')
    resource_class = EngagementTypeResource


class FeeGroupAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = FeeGroup
    list_display = ('name', 'description', 'created_by', 'created_on', 'updated_on')
    ordering = ('created_on', 'name')
    resource_class = FeeGroupResource


class FeeItemAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = FeeItem
    list_display = ('fee_group', 'item', 'description', 'created_by', 'created_on', 'updated_on')
    ordering = ('created_on', 'fee_group', 'item')
    resource_class = FeeItemResource


class HolidayListAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = HolidayList
    resource_class = HolidayListResource


class InstallBaseAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = InstallBase
    resource_class = InstallBaseResource


class LocationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = Location
    resource_class = LocationResource


class LocationAddressAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = LocationAddress
    resource_class = LocationAddressResource


class StaffShiftAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = StaffShift
    list_display = ('name', 'code', 'start_time', 'end_time')
    ordering = ('id',)
    resource_class = StaffShiftResource


class StaffRoleAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = StaffRoles
    list_display = ('role', 'status')
    ordering = ('id',)
    resource_class = StaffRolesResource


class StaffMemberAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = StaffMember
    list_display = ('last_name', 'first_name', 'second_name', 'arch_id',
                    'gender', 'title', 'shift', 'joined_on',)
    ordering = ('last_name', 'arch_id',)
    resource_class = StaffMemberResource


class StaffTitleAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = StaffTitle
    list_display = ('title',)
    ordering = ('title',)
    resource_class = StaffTitlesResource


class SystemAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = System
    resource_class = SystemResource
    autocomplete_fields = ['brand']
    list_display = ('brand', 'name', 'version', 'type', 'install_base', 'status')
    ordering = ('brand', 'name', 'version')


class SystemTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = SystemType
    list_display = ('code', 'typename')
    resource_class = SystemTypeResource


class TeamMemberAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = TeamMember
    resource_class = TeamMemberResource
    list_display = ('staff', 'client', 'role', 'valid_from', 'valid_to', 'status')
    ordering = ('client', 'staff', 'status')


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


class VendorItemDataAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = VendorItem
    resource_class = VendorItemDataResource


# endregion


admin.site.register(AddressType, AddressTypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientSystem, ClientSystemAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(EngagementType, EngagementTypeAdmin)
admin.site.register(FeeGroup, FeeGroupAdmin)
admin.site.register(FeeItem, FeeItemAdmin)
admin.site.register(HolidayList, HolidayListAdmin)
admin.site.register(InstallBase, InstallBaseAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationAddress, LocationAddressAdmin)
admin.site.register(StaffMember, StaffMemberAdmin)
admin.site.register(StaffRoles, StaffRoleAdmin)
admin.site.register(StaffShift, StaffShiftAdmin)
admin.site.register(StaffTitle, StaffTitleAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(SystemType, SystemTypeAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(UnitOfMeasure, UnitOfMeasureAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorAddress, VendorAddressAdmin)
admin.site.register(VendorItem, VendorItemDataAdmin)
