from django.contrib import admin

from auth0login.models import CustomUser

admin.site.register(CustomUser)