from django.forms import ModelForm, ModelChoiceField
from itembase.core.models import Address, AddressType, AddressUsage, Client, EngagementType     # , Modules


class ClientForm(ModelForm):
    # service_start = forms.DateField(widget=forms.SelectDateWidget)
    engagement = ModelChoiceField(queryset=EngagementType.objects, empty_label="Select Engagement")
    parent = ModelChoiceField(queryset=Client.objects.filter(client_status__lt=5), required=False)

    class Meta:
        model = Client
        fields = [
            'client_code',
            'client_name',
            'engagement',
            'parent',
            'service_start',
            'service_end',
            'client_status',
            'imp_fee_status',
            'production_support_number',
            'upload_address',
            'iq_support_address',
            'approved',
        ]


class ClientAddressForm(ModelForm):
    address_type = ModelChoiceField(queryset=AddressType.objects.order_by('id'))
    # used_on = ModelChoiceField(queryset=AddressUsage.objects.order_by('id'))
    client = ModelChoiceField(queryset=Client.objects.order_by('client_name'))

    class Meta:
        model = Address
        fields = [
            'client',
            'address_type', 'used_on', 'address1', 'address2', 'city',
            'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
        ]
