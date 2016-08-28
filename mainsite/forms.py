from django import forms
# from captcha.fields import CaptchaField
from django.forms import ModelForm, model_to_dict, fields_for_model
from mainsite.models import ProblemImage, Problem


class ProblemSubmissionForm(ModelForm):
    """This object describes a free estimate submission form fields."""

    def __init__(self, instance=None, *args, **kwargs):
        _fields = 'attachment'
        _initial = model_to_dict(instance.problem, _fields) if instance is not None else {}
        super(ProblemSubmissionForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(ProblemImage, _fields))

    class Meta:
        model = Problem
        fields = '__all__'

    def save(self, *args, **kwargs):
        u = self.instance.problem
        u.attachment = self.cleaned_data['attachment']
        u.save()
        problem = super(ProblemSubmissionForm, self).save(*args,**kwargs)
        return problem

    solution_type_choices = (
        ('complete', 'Complete solution'),
        ('answers_only', 'Answers only'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    solution_type = forms.ChoiceField(choices=solution_type_choices, widget=forms.RadioSelect)
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}), max_length=500,
                               required=False)
    # captcha = CaptchaField()


class ContactUsForm(forms.Form):
    """This is a class for the contact us page form."""

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}), max_length=500)
    # captcha = CaptchaField()
