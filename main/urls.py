from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('workstation', views.workstation, name='workstation'),
    path('logout', views.logout),

]