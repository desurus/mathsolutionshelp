import string
import random
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django import forms
from django.conf import settings
from django.forms import ModelForm
# from captcha.fields import CaptchaField


class Testimonial(models.Model):
    """This class is for testimonials table and data."""

    lang = getattr(settings, "LANGUAGES", None)
    status_choices = (
        ('submitted', 'Just submitted by user'),
        ('approved', 'Has been approved and published'),
    )

    status = models.CharField(choices=status_choices, max_length=50, default='submitted')
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    source = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=2, choices=lang)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '[' + self.language + '] ' + self.text


class TestimonialForm(ModelForm):
    """Testimonial form for the add testimonial page."""

    # captcha = CaptchaField()

    class Meta:
        model = Testimonial
        fields = ['author', 'email', 'source', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }


class ProblemCounter(models.Model):
    """This class is for the problems solved to date counter on the home page"""

    count = models.PositiveSmallIntegerField()
    next_update = models.DateTimeField()


class Problem(models.Model):
    """This class is for problem submitted by the user via form."""

    solution_type_choices = (
        ('complete', 'Complete solution'),
        ('answers_only', 'Answers only'),
    )
    status_choices = (
        ('submitted', 'Just submitted'),
        ('estimating', 'Calculating estimation'),
        ('estimation_sent', 'Price estimation sent to user'),
        ('in_progress', 'Expert working on finding solution'),
        ('solution_sent', 'Solution sent to user'),
        ('reopened', 'User claimed solution is wrong'),
        ('refunded', 'Cost refunded to user'),
        ('closed', 'Closed'),
    )

    status = models.CharField(choices=status_choices, max_length=50, default='submitted')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    deadline = models.DateField()
    solution_type = models.CharField(choices=solution_type_choices, max_length=20, default=0)
    comments = models.TextField(blank=True, max_length=500)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '[' + unicode(self.date_created.strftime("%d/%m/%y, %H:%M")) + '] ' + self.email


class ProblemImage(models.Model):
    """This class is for storing images for the problem."""

    # lets generate random string for the file storage dir
    folder = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))

    problem = models.ForeignKey(Problem)
    attachment = models.ImageField(upload_to=folder, blank=True)


class ExtendedFlatPage(FlatPage):
    """This custom flatpage extends default one by adding a language field."""

    lang = getattr(settings, "LANGUAGES", None)

    language = models.CharField(max_length=2, choices=lang)

