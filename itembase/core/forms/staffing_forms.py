from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from itembase.core.models import HolidayList, TeamMember, StaffMember


class HolidayForm(forms.ModelForm):

    class Meta:
        model = HolidayList
        fields = [
            'name',
            'date_from',
            'date_to',
            'notes',
        ]


class TeamMemberForm(forms.ModelForm):

    class Meta:
        model = TeamMember
        fields = [
            'staff',
            'client',
            'role',
            'valid_from',
            'valid_to',
            'status',
        ]

    def clean(self):
        cleaned_data = self.cleaned_data
        staff = cleaned_data.get('staff')
        client = cleaned_data.get('client')

        if TeamMember.objects.filter(staff=staff, client=client, status=2).exists():
            raise ValidationError(_('%(name)s is already active on %(client)s'),
                                  code='invalid',
                                  params={'name': staff, 'client': client})
        return cleaned_data
