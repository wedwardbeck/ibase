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

    class Meta:
        model = Address
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'vendor',
            'address_type', 'address1', 'address2', 'city',
            'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )


class VendorClientSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')

    class Meta:
        model = VendorClientMatrix
        fields = (
            'client',
            'vendor',
            'status',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )


class VendorItemSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')

    class Meta:
        model = VendorItem
        fields = (
            'item_number',
            'description',
            'vendor',
            'uom',
            'pack_count',
            'status',
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
