from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'autoscrapper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'autoscrapper.views.index', name='index'),
    url(r'^extract/', 'autoscrapper.views.extract', name='extract'),
    url(r'^output/', 'autoscrapper.views.output', name='output'),
    url(r'^admin/', include(admin.site.urls)),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


