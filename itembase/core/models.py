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


# Create your models here.
#
# def client_logo_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/clients/logos/slug_client_<id>/<filename>
#     # return 'resources/res_None/{1}'.format(filename)
#     return 'clients/logos/{0}/{1}'.format(instance.slug, filename)
#

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


class FeeStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    billed = ChoiceItem(2, _('Billed'))
    partial = ChoiceItem(3, _('Partially Paid'))
    paid = ChoiceItem(4, _('Paid'))


class ItemStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    validated = ChoiceItem(2, _('Valid'))
    inactive = ChoiceItem(3, _('Inactive'))


class VendorStatus(DjangoChoices):
    new = ChoiceItem(1, _('New'))
    validated = ChoiceItem(2, _('Valid'))
    inactive = ChoiceItem(3, _('Inactive'))


class EngagementType(models.Model):
    service_description = models.CharField(max_length=100, verbose_name='Service')
    service_abbreviation = models.CharField(max_length=10)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Engagement Type'
        verbose_name_plural = 'Engagement Types'

    def __str__(self):
        return self.service_description


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
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = "Clients"

    def get_absolute_url(self):
        return reverse('clients:view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.client_name


class Vendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name1 = models.CharField(_('Primary Name'), max_length=150)
    name2 = models.CharField(_('Additional Name '), max_length=100, blank=True)
    taxid = models.CharField(_('Tax ID'), max_length=15, blank=True)
    status = models.SmallIntegerField(_('Status'), choices=VendorStatus.choices,
                                      default=VendorStatus.new)
    parent = models.ForeignKey('self', verbose_name=_('Parent Vendor'), null=True, blank=True,
                               on_delete=models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   related_name='vendor_created', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def full_name(self):
        if self.name2 is None:
            return self.name1
        else:
            return ' '.join([self.name1, self.name2, ])

    def __str__(self):
        return self.name1

    def get_absolute_url(self):
        return reverse('vendors:view', kwargs={'pk': self.pk})


class UnitOfMeasure(models.Model):
    name = models.CharField(_('Unit'), max_length=50, unique=True)
    abbreviation = models.CharField(_('Abbreviation'), max_length=15)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created By'),
                                   related_name='uom_created', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Unit of Measure'
        verbose_name_plural = 'Units of Measure'

    def __str__(self):
        return self.name


class ItemData(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_number = models.CharField(_('Item Number'), max_length=100)
    description = models.CharField(_('Description'), max_length=255)
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vendor',
                               verbose_name=_('Vendor'), on_delete=models.PROTECT, null=False)
    uom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unitofmeasure',
                            verbose_name=_('UOM'), on_delete=models.PROTECT, null=False)
    pack_count = models.CharField(_('Package Count'), max_length=50)
    status = models.CharField(_('Status'), choices=ItemStatus.choices,
                              default=ItemStatus.new, max_length=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='item_created',
                                   verbose_name=_('created by'), on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Item Data'
        verbose_name_plural = 'Item Data'

    def __str__(self):
        return '%s - %s - %s' % (self.vendor, self.item_number, self.description)


class Location(models.Model):
    loc_id = models.CharField(_('Location ID'), max_length=50)
    name = models.CharField(_('Primary Name'), max_length=150)
    client = models.ForeignKey(Client, verbose_name=_('Client'), on_delete=models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_created',
                                   verbose_name=_('created by'), on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()


# region Address Models

class AddressType(models.Model):
    address_type = models.CharField(_('Address Type'), max_length=20)
    usage = models.CharField(_('Gender'), max_length=1, choices=AddressUsage.choices)
    fa_string = models.CharField(_('FA String'), max_length=50, blank=True, null=True)
    status = models.CharField(_('Status'), choices=BaseStatus.choices,
                              default=BaseStatus.new, max_length=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='address_type_created',
                                   verbose_name=_('created by'), on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
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
    status = models.CharField(_('Status'), choices=BaseStatus.choices,
                              default=BaseStatus.new, max_length=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_address_created',
                                   verbose_name=_('created by'), on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
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
                               null=True, blank=True, on_delete=models.PROTECT)
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
    status = models.CharField(_('Status'), choices=BaseStatus.choices,
                              default=BaseStatus.new, max_length=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vendor_address_created',
                                   verbose_name=_('created by'), on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
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

# endregion
