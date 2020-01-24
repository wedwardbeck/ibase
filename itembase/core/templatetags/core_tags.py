from django.template import Library
from itembase.core.models import Client, Vendor
register = Library()

# TODO add in new filter for general status icons and same for priorities


@register.filter(name='fa_valid')
def fa_valid(value):

    if value == 2:
        element = '<i class="fas fa-check-circle fa-xs text-success" aria-hidden="true"></i>'
    elif value == 1:
        element = '<i class="fas fa-exclamation-triangle fa-xs text-warning" aria-hidden="true"></i>'
    elif value == 3:
        element = '<i class="fas fa-times-circle fa-xs text-warning" aria-hidden="true"></i>'
    else:
        element = ''

    return element


@register.filter("add_label_class")
# @silence_without_field
def add_label_class(field, css_class):
    return field.label_tag(attrs={'class': css_class})


@register.simple_tag
def get_latest_clients():
    latest_clients = Client.objects.order_by('-id')[:5]
    return latest_clients


@register.simple_tag()
def get_changed_clients():
    changed_clients = Client.history.all().order_by('-history_id')[:5]
    return changed_clients


@register.simple_tag
def get_latest_partners():
    latest_partners = Vendor.objects.select_related('created_by').order_by('-id')[:5]
    return latest_partners

#
# @register.simple_tag
# def get_latest_partners2():
#     latest_partners2 = Vendor.objects.filter().order_by('-id')[:5]
#     return latest_partners2


@register.simple_tag()
def get_changed_partners():
    changed_partners = Vendor.history.all().order_by('-history_id')[:5]
    return changed_partners
