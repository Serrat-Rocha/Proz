from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.landing_page, name='landing'),
    path('fazer_login', views.login_view, name='fazer_login'),
    path('novo_produto', views.novo_produto, name='novo_produto'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('logout', views.logout_view, name='logout'),
    path('registrar', views.register, name='registrar'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),

]