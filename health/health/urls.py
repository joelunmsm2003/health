

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', 'app.views.home'),
    url(r'^nuevacita/', 'app.views.nuevacita'),
    url(r'^paciente', 'app.views.paciente'),
    url(r'^nuevopaciente/', 'app.views.nuevopaciente'),
    url(r'^dashboard/', 'app.views.dashboard'),
    url(r'^login/', 'app.views.login2'),
    url(r'^calendar/', 'app.views.calendar'),
    url(r'^citasjson/', 'app.views.citasjson'),
    url(r'^citaspk/(\d+)', 'app.views.citaspk'),
    url(r'^ingresar/', 'app.views.ingresar'),
    url(r'^nuevomedico/', 'app.views.nuevomedico'),
    url(r'^atencion/', 'app.views.atencion'),
    url(r'^pagos/', 'app.views.pagos'),
    url(r'^medico/', 'app.views.medico'),
    url(r'^editpaciente/(\d+)', 'app.views.editpaciente'),
    url(r'^editmedico/(\d+)', 'app.views.editmedico'),
    url(r'^editcita/(\d+)', 'app.views.editcita'),
  ]


