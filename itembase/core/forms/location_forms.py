from django.forms import ModelForm, ModelChoiceField

from itembase.core.models import AddressType, Location, LocationAddress


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = [
            "loc_id",
            "name",
            "client",
        ]


class LocationAddressForm(ModelForm):
    location = ModelChoiceField(queryset=Location.objects.order_by('loc_id'))
    address_type = ModelChoiceField(queryset=AddressType.objects.order_by('id'))
    # TODO Remove FK Location from form - display only in content

    class Meta:
        model = LocationAddress
        fields = [
            'location',
            'address_type', 'address1', 'address2', 'city',
            'state', 'postal_code', 'country', 'phone_number', 'email', 'primary', 'status',
        ]
    #
    # def __init__(self, location, *args, **kwargs):
    #     super(LocationAddressForm, self).__init__(*args, **kwargs)
    #     self.fields['location'].queryset = Location.objects.filter(client=self.location.client)
