from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    username = models.CharField(max_length=50, unique=True)
    # email = models.EmailField(max_length=127, unique=True, null=False, blank=False)
    date_joined = models.DateTimeField(editable=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
