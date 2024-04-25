from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view/<int:id>', views.view, name="view"),
]