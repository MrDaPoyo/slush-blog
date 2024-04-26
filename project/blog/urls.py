from django.urls import path
from . import views
 
urlpatterns = [
    path('home/<int:id>', views.home, name="home"),
    path('home/', views.homeRedirect),
    path('', views.homeRedirect),
    path('view/<int:id>', views.view, name="view"),
]