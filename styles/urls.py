from django.conf.urls import patterns, url
from styles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>.+?)/details/$', views.detail, name='detail'),
    url(r'^results/$', views.results, name='results'),
    url(r'^list/$', views.list, name='list'),
    url(r'^countrys/$', views.countrys, name='countrys'),
    url(r'^country/(?P<name>.+?)/$', views.bycountry, name='bycountry'),
)
