from django.forms import ModelForm
from itembase.core.models import Contact


class ClientContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'email', 'title', 'client', 'contact_type',
            'status',
        ]


#
# class AddressForm(ModelForm):
#     address_type = forms.ModelChoiceField(queryset=AddressType.objects.order_by('id'))
#
#     class Meta:
#         model = Address
#         fields = [
#             'vendor', 'address_type', 'address1', 'address2', 'city',
#             'state', 'postal_code', 'status',
#         ]
#
#
# ContactAddressFormSet = inlineformset_factory(
#         Partner,
#         Address, fields=('address_type', 'address1', 'city', 'state', 'postal_code'),
#         extra=2,
#         can_delete=False
#     )
#


class VendorContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'email', 'title', 'vendor', 'contact_type',
            'status',
        ]
