# from rest_framework import serializers
#
# from itembase.core.models import VendorItem
#
#
# class VendorItemSerializerD(serializers.ModelSerializer):
#     created_by_name = serializers.ReadOnlyField(source='created_by.name')
#     status_name = serializers.CharField(source='get_status_display')
#     uom_display = serializers.StringRelatedField(source='unitofmeasure.abbreviation')
#     uom_desc = serializers.StringRelatedField(source='unitofmeasure.description')
#
#     class Meta:
#         model = VendorItem
#         created_by = serializers.HiddenField(
#             default=serializers.CurrentUserDefault())
#
#         fields = (
#             'id',
#             'item_number',
#             'description',
#             'vendor',
#             'uom',
#             'uom_display',
#             'uom_desc',
#             'pack_count',
#             'status',
#             'status_name',
#             'created_on',
#             'updated_on',
#             'created_by',
#             'created_by_name',
#         )
