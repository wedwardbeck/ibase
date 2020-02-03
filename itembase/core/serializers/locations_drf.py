from rest_framework import serializers

from itembase.core.models import Location


class LocationSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')

    class Meta:
        model = Location
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'loc_id',
            'name',
            'client',
            'status',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )
