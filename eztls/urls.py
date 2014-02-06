from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eztls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^config', 'app.views.config_input'),
    url(r'^yourconfig', 'app.views.config_result'),
    url(r'^/?$', 'app.views.index'),
)
