from django.urls import path
from . import views

app_name = 'viajes'

urlpatterns = [
    path('', views.lista_viajes, name='lista'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('toggle-validado/<int:vehiculo_id>/', views.toggle_validado, name='toggle_validado'),
    path('exportar/', views.exportar_datos, name='exportar'),
]
