from django.forms import ModelForm, ModelChoiceField

from itembase.core.models import AddressType, Vendor, VendorAddress


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "name1",
            "name2",
            "taxid",
            "status",
            "parent"
        ]


class VendorAddressForm(ModelForm):
    address_type = ModelChoiceField(queryset=AddressType.objects.order_by('id'))
    # TODO Remove FK Vendor from form - display only in content

    class Meta:
        model = VendorAddress
        fields = [
            'vendor',
            'address_type', 'address1', 'address2', 'city',
            'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
        ]
