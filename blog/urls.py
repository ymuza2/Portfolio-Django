from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),  #acá buscamos un entero despues de la barra, para guardarlo como blog ID (para posteriormente buscar un blog por numero en la url)
]
