from django.urls import path
from . import views
 
urlpatterns = [
    path('home/<int:id>', views.home),
    path('home/', views.homeRedirect, name="home"),
    path('', views.homeRedirect),
    path('view/<int:id>', views.view, name="view"),
    path("delete_post/<int:id>", views.deletePost, name="delete_post")
]