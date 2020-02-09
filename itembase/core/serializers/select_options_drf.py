from rest_framework import serializers

from itembase.core.models import EngagementType


class EngagementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementType
        fields = (
            'id',
            'service_description',
            'service_abbreviation',
        )
