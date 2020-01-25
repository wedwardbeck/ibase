from rest_framework import serializers
from itembase.core.models import Vendor, VendorAddress, VendorClientMatrix, VendorItem, VendorLocMatrix


class VendorSerializer(serializers.ModelSerializer):
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
            'status',
            'created_on',
            'updated_on',
            'created_by',
        )


class VendorAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAddress
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'vendor',
            'address_type', 'address1', 'address2', 'city',
            'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
            'created_on',
            'updated_on',
            'created_by',
        )


class VendorClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorClientMatrix
        fields = (
            'client',
            'vendor',
            'status',
            'created_on',
            'updated_on',
        )


class VendorItemSerializer(serializers.ModelSerializer):
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
        )
