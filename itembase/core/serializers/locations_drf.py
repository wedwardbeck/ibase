from rest_framework import serializers

from itembase.core.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'loc_id',
            'name',
            'status',
            'created_on',
            'updated_on',
        )
