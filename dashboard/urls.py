from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.Home', name='home'),
)
