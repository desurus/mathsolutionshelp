from django.conf.urls import patterns, include, url
from mainsite import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mainsite.views.home', name='home'),
    url(r'^get-estimate/$', 'mainsite.views.get_estimate', name='get_estimate'),
    url(r'^add-testimonial/$', 'mainsite.views.add_testimonial', name='add_testimonial'),
    url(r'^contact-us/$', 'mainsite.views.contact_us', name='contact_us'),
    url(r'^testimonials/$', 'mainsite.views.testimonials', name='testimonials'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)
