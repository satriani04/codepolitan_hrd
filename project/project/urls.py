"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from homepage.views import login_view, logout_view
from karyawan.views import profil
from kehadiran.views import kehadiran_view, pengajuan_izin, izin_view, report

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profil, name='profile'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^kehadiran/$', kehadiran_view, name='kehadiran'),
    url(r'^pengajuan-izin/$', pengajuan_izin, name='pengajuan-izin'),
    url(r'^izin/$', izin_view, name='izin'),
    url(r'^grafik/(?P<bulan>\d+)/(?P<tahun>\d+)$', report, name='grafik'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)