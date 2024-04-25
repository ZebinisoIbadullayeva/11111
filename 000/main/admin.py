from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import Keys,Person


admin.site.register([Person,Keys,Token])
