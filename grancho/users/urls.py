from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path('home', views.home),
    path('logout', views.logout_user),
]
