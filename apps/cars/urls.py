from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^$', 'cars.views.main', name='main'),
)
urlpatterns += staticfiles_urlpatterns()
