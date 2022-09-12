from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name = 'index'),
path('amigos/', views.amigos, name = 'amigos'),
path('familia/', views.familia, name = 'familia'),
path('empresa/', views.empresa, name = 'empresa'),
path('cadastro/', views.cadastrar_contato, name='cadastrar contato'),
path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]