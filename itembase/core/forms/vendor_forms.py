from django.forms import ModelForm, ModelChoiceField

from itembase.core.models import Address, AddressType, AddressUsage, Vendor, VendorClientMatrix, VendorLocMatrix


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
    # used_on = ModelChoiceField(queryset=AddressUsage.objects.order_by('id'))
    vendor = ModelChoiceField(queryset=Vendor.objects.order_by('name1'))
    # TODO Remove FK Vendor from form - display only in content

    class Meta:
        model = Address
        fields = [
            'vendor',
            'address_type', 'used_on', 'address1', 'address2', 'city',
            'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
        ]


class VendorClientForm(ModelForm):

    class Meta:
        model = VendorClientMatrix
        fields = [
            'client',
            'vendor', 'status',
        ]


class VendorLocationForm(ModelForm):

    class Meta:
        model = VendorLocMatrix
        fields = [
            'location',
            'vendor', 'status',
        ]
