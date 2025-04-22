from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('fazer_login', auth_views.LoginView.as_view(template_name='usuarios/fazer_login.html'), name='fazer_login'),
    path('logout', views.logout_view, name='logout'),
    path('registrar', views.register, name='registrar'),
]