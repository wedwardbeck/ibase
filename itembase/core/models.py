# import uuid
from django.conf import settings
from django.db import models  # , transaction
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from djchoices import ChoiceItem, DjangoChoices
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords
from versatileimagefield.fields import VersatileImageField


# Create your models here.

def client_logo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/clients/logos/slug_client_<id>/<filename>
    # return 'resources/res_None/{1}'.format(filename)
    return 'clients/logos/{0}/{1}'.format(instance.slug, filename)


class AddressUsage(DjangoChoices):
    location = ChoiceItem('L', _('Location'))
    vendor = ChoiceItem('V', _('Vendor'))
    client = ChoiceItem('C', _('Client'))


class BaseStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    validated = ChoiceItem(2, _('Valid'))
    inactive = ChoiceItem(3, _('Inactive'))


class ClientStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    engaged = ChoiceItem(2, _('Under Implementation'))
    hypercare = ChoiceItem(3, _('HyperCare Period'))
    live = ChoiceItem(4, _('Live'))
    inactive = ChoiceItem(5, _('Inactive'))


class ContactType(DjangoChoices):
    person = ChoiceItem(1, 'Person')
    business = ChoiceItem(2, 'Business')


class FeeStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    billed = ChoiceItem(2, _('Billed'))
    partial = ChoiceItem(3, _('Partially Paid'))
    paid = ChoiceItem(4, _('Paid'))


class GenderType(DjangoChoices):
    female = ChoiceItem('F', _('Female'))
    male = ChoiceItem('M', _('Male'))


class ItemStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    validated = ChoiceItem(2, _('Valid'))
    inactive = ChoiceItem(3, _('Inactive'))


class VendorStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    validated = ChoiceItem(2, _('Valid'))
    inactive = ChoiceItem(3, _('Inactive'))


class Brand(models.Model):
    name = models.CharField(_('Brand'), max_length=75)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class EngagementType(models.Model):
    service_description = models.CharField(max_length=100, verbose_name='Service')
    service_abbreviation = models.CharField(max_length=10)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Engagement Type'
        verbose_name_plural = 'Engagement Types'

    def __str__(self):
        return self.service_description


class InstallBase(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = 'Install Base'
        verbose_name_plural = 'Install Bases'

    def __str__(self):
        return self.name


class StaffRoles(models.Model):
    role = models.CharField(max_length=30)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_roles_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT, null=True)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Staff Role'
        verbose_name_plural = 'Staff Roles'

    def __str__(self):
        return self.role


class SystemType(models.Model):
    code = models.CharField(max_length=5, default='ERP')
    typename = models.CharField(max_length=50)
    purpose = models.TextField(verbose_name='System Use', blank=True)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='system_type_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT, null=True)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'System Type'

    def __str__(self):
        return self.typename


class System(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    name = models.CharField(_('System Name'), max_length=75)
    version = models.CharField(_('Version'), max_length=15)
    type = models.ForeignKey(SystemType, verbose_name=_('System Type'), on_delete=models.PROTECT)
    install_base = models.ForeignKey(InstallBase, verbose_name=_('Install Base'), on_delete=models.PROTECT)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)

    class Meta:
        verbose_name = 'System'
        unique_together = ('brand', 'name', 'version')

    def get_absolute_url(self):
        return reverse('system-view', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s - %s - %s' % (self.brand, self.name, self.version)


class Client(models.Model):
    client_code = models.CharField(_('Client Code'), max_length=10, unique=True)
    client_name = models.CharField(_('Client Name'), max_length=100)
    slug = AutoSlugField(populate_from='client_code', unique=True)
    engagement = models.ForeignKey(EngagementType, verbose_name=_('Engagement Type'), on_delete=models.PROTECT)
    service_start = models.DateField(_('Service Start'), default=timezone.now)
    service_end = models.DateField(_('Service End'), null=True, blank=True)
    imp_fee_status = models.SmallIntegerField(_('Implementation Fee Status'), choices=FeeStatus.choices,
                                              default=FeeStatus.new)
    client_status = models.SmallIntegerField(_('Client Status'), choices=ClientStatus.choices,
                                             default=ClientStatus.new)
    production_support_number = PhoneNumberField(_('Production Support Number'), blank=True, null=True)
    approved = models.BooleanField(default=False)
    upload_address = models.EmailField(_('Upload Address'), blank=True, null=True)
    iq_support_address = models.EmailField(_('IQ Support Address'), blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name=_('Parent Client'), null=True, blank=True, on_delete=models.PROTECT)
    logo = VersatileImageField(
        _('Image'),
        # upload_to='media/clients/logos/',
        upload_to=client_logo_directory_path,
        # width_field='width',
        # height_field='height',
        null=True, blank=True
        # TODO review VIM documents to determine posting error - not accepting input
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = "Clients"

    def get_absolute_url(self):
        return reverse('clients:view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.client_name


class ClientSystem(models.Model):
    client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='client_systems',
                               on_delete=models.PROTECT)
    system = models.ForeignKey(System, verbose_name=_('System'), on_delete=models.PROTECT)
    have_access = models.BooleanField(_('Access?'), default=True)
    # TODO Redo this as choices  -minimize boolean
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Client System'
        unique_together = ('client', 'system')

    def __str__(self):
        return '%s - %s - %s' % (self.client, self.system, self.system.version)

    def get_absolute_url(self):
        return reverse('client_systems:client-system-view', kwargs={'pk': self.pk})


class Vendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name1 = models.CharField(_('Primary Name'), max_length=150)
    name2 = models.CharField(_('Additional Name '), max_length=100, blank=True)
    taxid = models.CharField(_('Tax ID'), max_length=15, blank=True)
    status = models.SmallIntegerField(_('Status'), choices=VendorStatus.choices,
                                      default=VendorStatus.new)
    parent = models.ForeignKey('self', verbose_name=_('Parent Vendor'), null=True, blank=True,
                               related_name='parent_vendor', on_delete=models.PROTECT)
    num_items = models.IntegerField(_("Number of Items"), null=True, blank=True)
    num_locations = models.IntegerField(_("Number of Locations"), null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   related_name='vendor_created', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    def full_name(self):
        if self.name2 is None:
            return self.name1
        else:
            return ' '.join([self.name1, self.name2, ])

    def __str__(self):
        return self.name1

    def get_absolute_url(self):
        return reverse('vendors:vendor-view', kwargs={'pk': self.pk})


class UnitOfMeasure(models.Model):
    name = models.CharField(_('Unit'), max_length=50, unique=True)
    abbreviation = models.CharField(_('Abbreviation'), max_length=15)
    description = models.CharField(_('Description'), max_length=150)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   related_name='uom_created', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Unit of Measure'
        verbose_name_plural = 'Units of Measure'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendor-items:uom-view', kwargs={'pk': self.pk})


class VendorItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_number = models.CharField(_('Item Number'), max_length=100)
    description = models.CharField(_('Description'), max_length=255)
    vendor = models.ForeignKey(Vendor, related_name='vendoritems',
                               verbose_name=_('Vendor'), on_delete=models.PROTECT, null=False)
    uom = models.ForeignKey(UnitOfMeasure, related_name='unitofmeasure',
                            verbose_name=_('UOM'), on_delete=models.PROTECT, null=False)
    pack_count = models.CharField(_('Package Count'), max_length=50)
    status = models.IntegerField(_('Status'), choices=ItemStatus.choices,
                                 default=ItemStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='item_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT, null=True)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Item Data'
        verbose_name_plural = 'Item Data'

    def __str__(self):
        return '%s - %s - %s' % (self.vendor, self.item_number, self.description)

    def get_absolute_url(self):
        return reverse('vendor-items:view', kwargs={'pk': self.pk})


class Location(models.Model):
    loc_id = models.CharField(_('Location ID'), max_length=50)
    name = models.CharField(_('Primary Name'), max_length=150)
    client = models.ForeignKey(Client, verbose_name=_('Client'), on_delete=models.PROTECT)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT, null=True)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return '%s - %s' % (self.loc_id, self.name)
        #
        # def get_absolute_url(self):
        #     return reverse('locations:view', kwargs={'pk': self.pk})


class Contact(models.Model):
    first_name = models.CharField(_('First Name'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=255, )
    email = models.EmailField(_('Email'), null=True, blank=True)
    title = models.CharField(_('Title'), max_length=200, blank=True)
    client = models.ForeignKey(Client, verbose_name=_('Client'), null=True, blank=True, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, verbose_name=_('Location'), null=True, blank=True, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, verbose_name=_('Vendor'), null=True, blank=True,
                               on_delete=models.PROTECT)
    contact_type = models.SmallIntegerField(
        _('Contact Type'),
        choices=ContactType.choices,
        default=ContactType.person
    )
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contact_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return ' '.join([
            self.first_name if self.first_name else '-',
            self.last_name,
        ])

    def get_absolute_url(self):
        return reverse('contacts:view', args=[str(self.id)])


# region Address Models

class AddressType(models.Model):
    address_type = models.CharField(_('Address Type'), max_length=20)
    usage = models.CharField(_('Gender'), max_length=1, choices=AddressUsage.choices)
    fa_string = models.CharField(_('FA String'), max_length=50, blank=True, null=True)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='address_type_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.address_type


class LocationAddress(models.Model):
    location = models.ForeignKey(Location, verbose_name=_('Location'), related_name='location_address',
                                 on_delete=models.PROTECT)
    address_type = models.ForeignKey(AddressType, verbose_name=_('Address Type'), on_delete=models.PROTECT)
    address1 = models.CharField(_('Address 1'), max_length=255, )
    address2 = models.CharField(_('Address 2'), max_length=255, null=True, blank=True)
    city = models.CharField(_('City'), max_length=255)
    state = models.CharField(_('State'), max_length=2)
    postal_code = models.CharField(_('Postal Code'), max_length=20, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=3, blank=True, null=True)
    phone_number = PhoneNumberField(_('Phone Number'), blank=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    primary = models.BooleanField(default=False)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_address_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __str__(self):
        return ' '.join([
            self.address1,
            ',',
            self.city,
        ])

    def get_absolute_url(self):
        return reverse('vendors:address-view', args=[str(self.id)])


class VendorAddress(models.Model):
    vendor = models.ForeignKey(Vendor, verbose_name=_('Vendor'), related_name='vendor_address',
                               on_delete=models.PROTECT)
    address_type = models.ForeignKey(AddressType, verbose_name=_('Address Type'), on_delete=models.PROTECT)
    address1 = models.CharField(_('Address 1'), max_length=255, )
    address2 = models.CharField(_('Address 2'), max_length=255, null=True, blank=True)
    city = models.CharField(_('City'), max_length=255)
    state = models.CharField(_('State'), max_length=2)
    postal_code = models.CharField(_('Postal Code'), max_length=20, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=3, blank=True, null=True)
    phone_number = PhoneNumberField(_('Phone Number'), blank=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    primary = models.BooleanField(default=False)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vendor_address_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Vendor Address'
        verbose_name_plural = 'Vendor Addresses'

    def __str__(self):
        return ' '.join([
            self.address1,
            ',',
            self.city,
        ])

    def get_absolute_url(self):
        return reverse('vendors:address-view', args=[str(self.id)])


class VendorLocMatrix(models.Model):
    location = models.ForeignKey(Location, verbose_name=_('Location'), related_name='loc_2_vn',
                                 on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, verbose_name=_('Vendor'), related_name='vn_2_loc',
                               on_delete=models.PROTECT)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vlm_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Vendor Location Record'
        verbose_name_plural = 'Vendor Location Records'

    def __str__(self):
        return ' '.join([
            self.location,
            ',',
            self.vendor,
        ])


class VendorClientMatrix(models.Model):
    client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='client_2_vn',
                               on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, verbose_name=_('Vendor'), related_name='vn_2_client',
                               on_delete=models.PROTECT)
    cv_id = models.CharField(_('Client Vendor ID'), max_length=30, null=True, blank=True)
    cv_name = models.CharField(_('Client Vendor Name'), max_length=100, null=True, blank=True)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vcm_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Vendor Client Record'
        verbose_name_plural = 'Vendor Client Records'

    def __str__(self):
        return ' '.join([
            self.client,
            ',',
            self.vendor,
        ])


# endregion


# region Staffing

class StaffShift(models.Model):
    code = models.CharField(_('Code'), max_length=5)
    name = models.CharField(_('Shift Name'), max_length=30)
    start_time = models.TimeField(_('Starts UTC'))
    end_time = models.TimeField(_('Ends UTC'))
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_shift_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'

    def __str__(self):
        return self.name


class StaffTitle(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_title_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Staff Title'
        verbose_name_plural = 'Staff Titles'

    def __str__(self):
        return self.title


class StaffMember(models.Model):
    first_name = models.CharField(_('First Name'), max_length=50)
    second_name = models.CharField(_('Second Name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=50)
    gender = models.CharField(_('Gender'), max_length=1, choices=GenderType.choices)
    title = models.ForeignKey(StaffTitle, verbose_name=_('Title'), on_delete=models.PROTECT)
    joined_on = models.DateField(_('Joined IQ On'))
    departed_on = models.DateField(_('Left IQ On'), null=True, blank=True)
    arch_id = models.CharField(_('Archimedes ID'), max_length=50, blank=True, null=True)
    emp_id = models.IntegerField(_('Employee ID'), blank=True, null=True)
    shift = models.ForeignKey(StaffShift, on_delete=models.PROTECT)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_member_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Staff Member'
        verbose_name_plural = 'Staff Members'
        unique_together = ('first_name', 'second_name', 'last_name')
        ordering = ['first_name', 'second_name', 'last_name']

    def __str__(self):
        if self.second_name:
            string = '%s %s %s' % (self.first_name, self.second_name, self.last_name)
        else:
            string = '%s %s' % (self.first_name, self.last_name)
        return string


class TeamMember(models.Model):
    staff = models.ForeignKey(StaffMember, verbose_name=_('Staff'), limit_choices_to={'status': 2},
                              on_delete=models.PROTECT)
    client = models.ForeignKey(Client, verbose_name=_('Client'), on_delete=models.PROTECT)
    role = models.ForeignKey(StaffRoles, verbose_name=_('Role'), limit_choices_to={'status': 2},
                             on_delete=models.PROTECT)
    valid_from = models.DateField(_('Valid From'), default=timezone.now)
    valid_to = models.DateField(_('Valid Until'), null=True, blank=True)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='team_member_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        unique_together = ('staff', 'client', 'status')
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')

    def __str__(self):
        return self.staff.last_name
        # return '%s - %s in Client %s' % (self.staff, self.role, self.client)


class HolidayList(models.Model):
    name = models.CharField(_('Description'), max_length=30)
    date_from = models.DateField(_('Date Start'), default=timezone.now)
    date_to = models.DateField(_('Date End'), default=timezone.now)
    notes = models.TextField(_('Notes'), null=True, blank=True)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='holiday_list_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Holiday')
        verbose_name_plural = _('Holidays')

    def __str__(self):
        return '%s - %s' % (self.name, self.date_from)


# endregion


# region Contract & Billing

class FeeGroup(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.CharField(_('Description'), max_length=255)
    status = models.IntegerField(_('Status'), choices=BaseStatus.choices,
                                 default=BaseStatus.new)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='fee_group_created',
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Fee Group')
        verbose_name_plural = _('Fee Groups')

    def __str__(self):
        return self.name


class FeeItem(models.Model):
    item = models.CharField(_('Item'), max_length=50)
    description = models.CharField(_('Description'), max_length=255)
    fee_group = models.ForeignKey(FeeGroup, verbose_name=_('Fee Group'), on_delete=models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Fee Item')
        verbose_name_plural = _('Fee Items')

    def __str__(self):
        return self.item


# endregion

# region Contract & Billing

class VineVendorImport(models.Model):
    vendor_code = models.CharField(_('Item'), max_length=50)
    name = models.CharField(_('Item'), max_length=50)
    addr1 = models.CharField(_('Item'), max_length=150)
    addr2 = models.CharField(_('Item'), max_length=150)
    addr3 = models.CharField(_('Item'), max_length=150)
    city = models.CharField(_('Item'), max_length=50)
    state = models.CharField(_('Item'), max_length=25)
    zipcode = models.CharField(_('Item'), max_length=25)
    phone = models.CharField(_('Item'), max_length=50)
    extension = models.CharField(_('Item'), max_length=50)
    salesperson_name = models.CharField(_('Item'), max_length=100)
    salesperson_email = models.CharField(_('Item'), max_length=100)
    salesperson_phone = models.CharField(_('Item'), max_length=50)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False, null=True)
    source = models.CharField(_('Item'), max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


def vine_upload_user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'vine_user_{0}/{1}'.format(instance.created_by.id, filename)


class VineVendorFile(models.Model):
    file = models.FileField(upload_to=vine_upload_user_directory_path)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name=_('Created By'), on_delete=models.PROTECT)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True, editable=False)
    # TODO - add processed bool to capture in pipeline files not yet processed

# endregion
