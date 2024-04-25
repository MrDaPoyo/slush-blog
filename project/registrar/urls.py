from django.urls import path, include
from . import views
import django.contrib.auth.urls

urlpatterns = [
    path('', include("django.contrib.auth.urls"))
]