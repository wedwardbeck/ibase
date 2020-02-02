from rest_framework import serializers

from itembase.core.models import Client, ClientStatus


class ClientSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    imp_fee_status = serializers.CharField(source='get_imp_fee_status_display')
    client_status = serializers.CharField(source='get_client_status_display')
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
