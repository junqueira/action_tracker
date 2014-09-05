from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',

    #Public view
    url(r'^$', 'public.views.Home', name='home'), #puclic view

    #Dashboard
    url(r'^dashboard/', include('dashboard.urls',namespace='dashboard')),

    #Users
    url(r'^users/', include('users.urls',namespace='users')),

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
