from django.shortcuts import render


def home(request):
    username = None

    if request.user.is_authenticated():
        username = request.user.username

    context = {
        'username': username
    }
    return render(request, 'base.html', context)
 