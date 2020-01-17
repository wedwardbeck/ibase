from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, BooleanField, DateTimeField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractUser):
    #
    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})

    username = None
    email = EmailField(_('email address'), unique=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    is_active = BooleanField(default=True)
    date_joined = DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
