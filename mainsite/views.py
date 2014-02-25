from django.shortcuts import render
from mainsite.models import Testimonial, ProblemCounter, ProblemsForm, Problems
from mainsite.forms import ProblemSubmissionForm
from random import choice
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.http import HttpResponseRedirect


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
        form = ProblemsForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the data in form.cleaned_data
            files = {}
            path = ''

            if 'attachment1' in request.FILES:
                files.update({
                    'attachment1': request.FILES['attachment1'],
                })
            if 'attachment2' in request.FILES:
                files.update({
                    'attachment2': request.FILES['attachment2'],
                })
            if 'attachment3' in request.FILES:
                files.update({
                    'attachment3': request.FILES['attachment3'],
                })
            # now lets pass dict to the handler
            if files:
                path = handleUploadedFiles(files)
                print path

            return HttpResponseRedirect('/thanks/')
        if form.errors:
            print form.errors

    else:
        form = ProblemSubmissionForm()

    context.update({
        'form': form,
    })

    return render(request, 'mainsite/estimate.html', context)


def handleUploadedFiles(files):
    """This function handles uploaded files."""

    return '/path/'

