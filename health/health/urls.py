

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', 'app.views.home'),
    url(r'^nuevacita/', 'app.views.nuevacita'),
    url(r'^paciente/', 'app.views.paciente'),
    url(r'^nuevopaciente/', 'app.views.nuevopaciente'),
    url(r'^dashboard/', 'app.views.dashboard'),
    url(r'^login/', 'app.views.login'),
    url(r'^calendar/', 'app.views.calendar'),
    url(r'^citasjson/', 'app.views.citasjson'),
    url(r'^citaspk/(\d+)', 'app.views.citaspk'),
    url(r'^nuevomedico/', 'app.views.nuevomedico'),
  ]


