from rest_framework import serializers

from itembase.core.models import Address, Client, ClientStatus


class ClientSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    imp_fee_status = serializers.CharField(source='get_imp_fee_status_display')
    client_status_name = serializers.CharField(source='get_client_status_display')
    engagement = serializers.StringRelatedField()

    class Meta:
        model = Client
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'client_code',
            'client_name',
            'slug',
            'engagement',
            'service_start',
            'service_end',
            'imp_fee_status',
            'client_status',
            'client_status_name',
            'production_support_number',
            'approved',
            'upload_address',
            'iq_support_address',
            'parent',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',

        )


class ClientCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = (
            'client_code',
        )


class ClientAddressSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    client_name = serializers.CharField(source='client.client_name')
    status_name = serializers.CharField(source='get_status_display')
    address_type_name = serializers.CharField(source='address_type.address_type')
    used_on = serializers.ChoiceField(choices='C')

    class Meta:
        model = Address
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'client',
            'client_name',
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
