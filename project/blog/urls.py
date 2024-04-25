from django.urls import path, include
from . import views

urlpatterns = [
    path('home/<int:id>', views.home, name="home"),
    path('view/<int:id>', views.view, name="view"),
]