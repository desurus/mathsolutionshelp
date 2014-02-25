from django.conf.urls import patterns, include, url
from mainsite import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mainsite.views.home', name='home'),
    url(r'^get-estimate/$', 'mainsite.views.get_estimate', name='get_estimate'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
)
