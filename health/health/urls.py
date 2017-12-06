

from django.conf.urls import include, url
from django.contrib import admin
from app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^nuevacita/', views.nuevacita),
    url(r'^paciente', views.paciente),
    url(r'^nuevopaciente/', views.nuevopaciente),
    url(r'^dashboard/', views.dashboard),
    url(r'^login/', views.login2),
    url(r'^citasjson/', views.citasjson),
    url(r'^citaspk/(\d+)', views.citaspk),
    url(r'^ingresar/',views.ingresar),
    url(r'^nuevomedico/',views.nuevomedico),
    url(r'^atencion/', views.atencion),
    url(r'^pagos/', views.pagos),
    url(r'^medico/', views.medico),
    url(r'^editpaciente/(\d+)', views.editpaciente),
    url(r'^editmedico/(\d+)', views.editmedico),
    url(r'^editcita/(\d+)', views.editcita),
    url(r'^citas/', views.citas),
    url(r'^busqueda/', views.busqueda),
    url(r'^busquedacita/', views.busquedacita),
    url(r'^busquedamedico/', views.busquedamedico),
    url(r'^fotos/', views.fotos),
    url(r'^consulta/', views.traeconsulta),
    url(r'^nuevaconsulta/', views.nuevaconsulta),
  ]


