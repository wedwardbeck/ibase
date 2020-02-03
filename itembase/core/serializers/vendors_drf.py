from rest_framework import serializers
from itembase.core.models import Vendor, Address, VendorClientMatrix, VendorItem, \
    VendorLocMatrix, VineVendorImport, VineVendorFile


class VendorSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')

    class Meta:
        model = Vendor
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'name1',
            'name2',
            'taxid',
            'status',
            'parent',
            'num_items',
            'num_locations',
            'status',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )
        #
        # @staticmethod
        # def setup_eager_loading(queryset):
        #     # select_related for 'to-one' relationships
        #     queryset = Vendor.objects.all().prefetch_related('created_by')
        #     return queryset


class VendorAddressSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    vendor_name = serializers.CharField(source='vendor.name1')
    status_name = serializers.CharField(source='get_status_display')
    address_type_name = serializers.CharField(source='address_type.address_type')
    used_on = serializers.ChoiceField(choices='V')

    class Meta:
        model = Address
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'vendor',
            'vendor_name',
            'used_on',
            'address_type',
            'address_type_name',
            'address1',
            'address2',
            'city',
            'state',
            'postal_code',
            'country',
            'phone_number',
            'email',
            'primary',
            'status',
            'status_name',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )


class VendorClientSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    vendor_name = serializers.ReadOnlyField(source='vendor.name1')
    status_name = serializers.ReadOnlyField(source='get_status_display')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    client_code = serializers.ReadOnlyField(source='client.client_code')

    class Meta:
        model = VendorClientMatrix
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'client',
            'client_code',
            'client_name',
            'vendor',
            'vendor_name',
            'cv_id',
            'cv_name',
            'status',
            'status_name',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )

    # @staticmethod
    # def setup_eager_loading(queryset):
    #     """ Perform necessary eager loading of data. """
    #     # select_related for "to-one" relationships
    #     queryset = queryset.select_related('created_by', 'created_by_name')
    #
    #     return queryset


class VendorItemSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    status_name = serializers.CharField(source='get_status_display')
    vendor_name = serializers.CharField(source='vendor.name1')
    uom_display = serializers.StringRelatedField(source='uom.abbreviation')
    uom_desc = serializers.StringRelatedField(source='uom.description')

    class Meta:
        model = VendorItem
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'item_number',
            'description',
            'vendor',
            'vendor_name',
            'uom',
            'uom_display',
            'uom_desc',
            'pack_count',
            'status',
            'status_name',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )


class VineVendorSerializer(serializers.ModelSerializer):
    # created_by_name = serializers.ReadOnlyField(source='created_by.name')

    class Meta:
        model = VineVendorFile
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'file',
            'created_by',
            'created_on',
        )
