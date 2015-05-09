from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from mainsite import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'mainsite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(_(r'^get-estimate/$'), 'mainsite.views.get_estimate', name='get_estimate'),
    url(_(r'^add-testimonial/$'), 'mainsite.views.add_testimonial', name='add_testimonial'),
    url(_(r'^contact-us/$'), 'mainsite.views.contact_us', name='contact_us'),
    url(_(r'^testimonials/$'), 'mainsite.views.testimonials', name='testimonials'),
)

urlpatterns += i18n_patterns('django.contrib.flatpages.views',
    url(_(r'^about-us/$'), 'flatpage', {'url': '/about-us/'}, name='about'),
    url(_(r'^problem-solving-service/$'), 'flatpage', {'url': '/problem-solving-service/'}, name='problem_solving'),
    url(_(r'^our-experts/$'), 'flatpage', {'url': '/our-experts/'}, name='experts'),
    url(_(r'^terms-of-service/$'), 'flatpage', {'url': '/terms-of-service/'}, name='terms'),
    url(_(r'^privacy-policy/$'), 'flatpage', {'url': '/privacy-policy/'}, name='privacy_policy'),
    url(_(r'^money-back-guarantee/$'), 'flatpage', {'url': '/money-back-guarantee/'}, name='moneyback'),
    url(_(r'^thank-you/$'), 'flatpage', {'url': '/thank-you/'}, name='thankyou'),
)
