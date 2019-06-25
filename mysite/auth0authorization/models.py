from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class ApplicationManager(BaseUserManager):
    def create_app(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class Application(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=70, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = ApplicationManager()

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_long_name(self):
        return self.username
