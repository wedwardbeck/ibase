from rest_framework import serializers

from itembase.core.models import FeeGroup, FeeItem


class FeeGroupSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    status_name = serializers.CharField(source='get_status_display')

    class Meta:
        model = FeeGroup
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'name',
            'description',
            'status',
            'status_name',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )


class FeeItemSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.name')
    status_name = serializers.CharField(source='get_status_display')

    class Meta:
        model = FeeItem
        created_by = serializers.HiddenField(
            default=serializers.CurrentUserDefault())

        fields = (
            'id',
            'item',
            'description',
            'fee_group',
            'status',
            'status_name',
            'created_on',
            'updated_on',
            'created_by',
            'created_by_name',
        )
