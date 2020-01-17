from django.forms import ModelForm

from itembase.core.models import UnitOfMeasure, VendorItem


class UOMForm(ModelForm):
    class Meta:
        model = UnitOfMeasure
        fields = [
            "name",
            "abbreviation",
            "description"
        ]


class VendorItemForm(ModelForm):
    class Meta:
        model = VendorItem
        fields = [
            "item_number",
            "description",
            "vendor",
            "uom",
            "pack_count",
            "status"
        ]
