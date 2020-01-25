from rest_framework import serializers

from itembase.core.models import VendorItem


class VendorItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendorItem
        fields = (
            'item_number',
            'description',
            'vendor',
            'uom',
            'pack_count',
            'status',
        )
