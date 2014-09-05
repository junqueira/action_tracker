from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.Home', name='home'),
    url(r'new/$', 'users.views.New', name='new'),
    url(r'^edit/(?P<user_id>\d+)/$', 'users.views.Edit',name='edit'),
    url(r'^delete/(?P<user_id>\d+)/$', 'users.views.Delete',name='delete'),
    url(r'^login/$', 'users.views.Login', name='login'),
    url(r'^password/$', 'users.views.Password', name='password'),
    url(r'^logout/$', 'users.views.Logout', name='logout'),

)
