from django import forms
# from django.forms.models import inlineformset_factory, BaseInlineFormSet
from itembase.core.models import Client, EngagementType     # , Modules
# from .widgets import RelatedFieldWidgetCanAdd


class ClientForm(forms.ModelForm):
    # service_start = forms.DateField(widget=forms.SelectDateWidget)
    engagement = forms.ModelChoiceField(queryset=EngagementType.objects, empty_label="Select Engagement")
    parent = forms.ModelChoiceField(queryset=Client.objects.filter(client_status__lt=5), required=False)

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
