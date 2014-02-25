from django import forms
from captcha.fields import CaptchaField


class ProblemSubmissionForm(forms.Form):
    """This object describes a free estimate submission form fields."""

    solution_type_choices = (
        ('complete', 'Complete solution'),
        ('answers_only', 'Answers only'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    solution_type = forms.ChoiceField(choices=solution_type_choices, widget=forms.RadioSelect)
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}), max_length=500, required=False)
    attachment1 = forms.ImageField(required=False)
    attachment2 = forms.ImageField(required=False)
    attachment3 = forms.ImageField(required=False)
    captcha = CaptchaField()
