from django.db import models
from django.conf import settings
from django.forms import ModelForm
from captcha.fields import CaptchaField


class Testimonial(models.Model):
    """This class is for testimonials table and data."""

    lang = getattr(settings, "LANGUAGES", None)

    text = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    language = models.CharField(max_length=2, choices=lang)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '[' + self.language + '] ' + self.text


class ProblemCounter(models.Model):
    """This class is for the problems solved to date counter on the home page"""

    count = models.PositiveSmallIntegerField()
    next_update = models.DateTimeField()


class Problems(models.Model):
    """This class is for problem submitted by the user via form."""

    solution_type_choices = (
        ('complete', 'Complete solution'),
        ('answers_only', 'Answers only'),
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    deadline = models.DateField()
    solution_type = models.CharField(choices=solution_type_choices)
    comments = models.TextField(blank=True, max_length=500)
    attachment1 = models.ImageField(upload_to="test", blank=True)
    attachment2 = models.ImageField(upload_to="test", blank=True)
    attachment3 = models.ImageField(upload_to="test", blank=True)


class ProblemsForm(ModelForm):
    """Problems Form object for our Problems class."""

    captcha = CaptchaField()

    class Meta:
        model = Problems
        fields = ['name', 'email', 'deadline', 'solution_type', 'comments', 'attachment1', 'attachment2', 'attachment3']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'deadline': DateInput(attrs={'class': 'form-control'}),
            'solution_type': RadioSelect(),
            'comments': Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }
