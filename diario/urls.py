from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='diario'),
    path('escrever/', views.escrever, name='escrever'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('dia/', views.dia, name='dia'),
    path('excluir_dia', views.excluir_dia, name='excluir_dia')
]
