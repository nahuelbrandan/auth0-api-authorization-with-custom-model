from django.contrib import admin

from auth0authorization.models import CustomUser

admin.site.register(CustomUser)