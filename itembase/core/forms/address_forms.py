# from django.forms import ModelForm, ModelChoiceField
#
# from itembase.core.models import Address, AddressType, Client, Location, Vendor
#
#
# class ClientAddressForm(ModelForm):
#     address_type = ModelChoiceField(queryset=AddressType.objects.order_by('id'))
#     client = ModelChoiceField(queryset=Client.objects.order_by('client_name'))
#
#     class Meta:
#         model = Address
#         fields = [
#             'client',
#             'address_type', 'address1', 'address2', 'city',
#             'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
#         ]

#
# class LocationAddressForm(ModelForm):
#     address_type = ModelChoiceField(queryset=AddressType.objects.order_by('id'))
#
#     class Meta:
#         model = Address
#         fields = [
#             'location',
#             'address_type', 'address1', 'address2', 'city',
#             'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
#         ]
#
#
# class VendorAddressForm(ModelForm):
#     address_type = ModelChoiceField(queryset=AddressType.objects.order_by('id'))
#
#     class Meta:
#         model = Address
#         fields = [
#             'vendor',
#             'address_type', 'address1', 'address2', 'city',
#             'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
#         ]
