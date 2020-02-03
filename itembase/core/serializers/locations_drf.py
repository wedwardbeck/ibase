from rest_framework import serializers

from itembase.core.models import Address, Location


class LocationSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    status_name = serializers.CharField(source='get_status_display')
    client = serializers.StringRelatedField()
    client_code = serializers.StringRelatedField(source='client.client_code')

    class Meta:
        model = Location
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'loc_id',
            'name',
            'client',
            'client_code',
            'status',
            'status_name',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )


class LocationAddressSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    loc_id = serializers.CharField(source='location.loc_id')
    loc_name = serializers.CharField(source='location.name')
    status_name = serializers.CharField(source='get_status_display')
    address_type_name = serializers.CharField(source='address_type.address_type')
    loc_client = serializers.CharField(source='location.client.client_name')
    loc_client_code = serializers.CharField(source='location.client.client_code')
    used_on = serializers.ChoiceField(choices='L')

    class Meta:
        model = Address
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'location',
            'loc_id',
            'loc_name',
            'loc_client_code',
            'loc_client',
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
