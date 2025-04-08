from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path('home', views.home),
    path('users/table/', views.table_view, name='user_table'),
    path('logout', views.logout_user),
]
