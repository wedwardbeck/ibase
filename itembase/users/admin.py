from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from itembase.users.forms import UserChangeForm, UserCreationForm
from itembase.users.models import User

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = (("User", {"fields": ("name", "is_active", "is_superuser")}),) # + auth_admin.UserAdmin.fieldsets
    list_display = ["email", "is_active", "name", "is_superuser"]
    ordering = ('id', 'email',)
    search_fields = ["name"]
