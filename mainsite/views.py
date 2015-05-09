from django.shortcuts import render
from mainsite.models import Testimonial, ProblemCounter, ProblemForm, TestimonialForm
from mainsite.forms import ContactUsForm
from random import choice
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.http import HttpResponseRedirect
from django.core.mail import mail_admins


def home(request):
    """This is home page of the site."""

    username = None
    language_code = request.LANGUAGE_CODE

    # we need to get testimonials in the users language
    all_testimonials = Testimonial.objects.filter(language=language_code)

    context = {
        'testimonial': choice(all_testimonials),
    }

    # we also need to get problems counter
    counter = ProblemCounter.objects.get(pk=1)
    # lets see if we need to increase counter
    if counter.next_update > datetime.utcnow().replace(tzinfo=utc):
        # not yet
        context.update({
            'counter': counter.count,
        })
    else:
        # time to increase counter and set new time
        new_counter = counter.count + 1
        new_update_time = datetime.utcnow().replace(tzinfo=utc) + timedelta(hours=choice(range(4, 16)))
        counter.count = new_counter
        counter.next_update = new_update_time
        counter.save()
        context.update({
            'counter': new_counter,
        })

    return render(request, 'mainsite/index.html', context)


def get_estimate(request):
    """On this page user submits a problem for cost evaluation."""

    context = {}

    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # now lets send email to the admins
            mail_admins('New problem submitted', 'New problem has been submitted.', fail_silently=False)

            return HttpResponseRedirect('/thank-you/')
        if form.errors:
            print form.errors

    else:
        form = ProblemForm()

    context.update({
        'form': form,
    })

    return render(request, 'mainsite/estimate.html', context)


def add_testimonial(request):
    """Renders a page where user can add testimonial."""

    context = {}

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()

            # now lets send email to the admins
            mail_admins('New testimonial added', 'New testimonial has been submitted.', fail_silently=False)

            return HttpResponseRedirect('/thank-you/')
        if form.errors:
            print form.errors

    else:
        form = TestimonialForm()

    context.update({
        'form': form,
    })

    return render(request, 'mainsite/add_testimonial.html', context)


def contact_us(request):
    """Renders a page with contact us form."""

    context = {}

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['text']

            # now lets send email to the admins
            mail_admins('[Contact Us] ' + subject, 'From: ' + name + ', ' + email + '\n' + message, fail_silently=False)

            return HttpResponseRedirect('/thank-you/')
        if form.errors:
            print form.errors

    else:
        form = ContactUsForm()

    context.update({
        'form': form,
    })

    return render(request, 'mainsite/contact_us.html', context)


def testimonials(request):
    """This page renders all testimonials in users language."""

    context = {}
    language_code = request.LANGUAGE_CODE

    # we need to get testimonials in the users language
    all_testimonials = Testimonial.objects.filter(language=language_code)

    context.update({
        'testimonials': all_testimonials,
    })

    return render(request, 'mainsite/testimonials.html', context)
