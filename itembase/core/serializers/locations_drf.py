from rest_framework import serializers

from itembase.core.models import Location


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
