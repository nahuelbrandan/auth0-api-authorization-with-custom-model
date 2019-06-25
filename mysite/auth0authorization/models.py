from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ugettext_lazy as _


class ApplicationManager(models.Manager):
    def create_app(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class Application(models.Model):
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

    def get_natural_key(self):
        return [self.username]

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_not_anonymous(self):
        return True
