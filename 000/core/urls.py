from django.contrib import admin
from django.urls import path

from main.views import CreateToken,CheckKey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getkey/',CreateToken.as_view()),
    path('check/',CheckKey.as_view())
]
