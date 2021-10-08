from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('workstation', views.workstation, name='workstation'),
    path('ingrediente', views.ingredienteviw, name='ingrediente'),
    path('stock', views.lista_ingredientes, name='stock'),
    path('editar-stock/<id>/', views.editar_stck, name='editar-stock'),
    path('delate-stock/<id>/', views.eliminar_ingrediente, name='delate-stock'),
    path('logout', views.logout),

]