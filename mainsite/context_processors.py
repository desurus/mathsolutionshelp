from django.conf import settings  # import the settings file
from mainsite.models import Testimonial
import random


def get_email_address(request):
    return {'CONTACTS_EMAIL_ADDRESS': settings.EMAIL_ADDRESS}


def get_testimonials(request):
    language_code = request.LANGUAGE_CODE
    all_testimonials = Testimonial.objects.filter(language=language_code)
    return {'random_testimonials': random.sample(all_testimonials, 3)}
