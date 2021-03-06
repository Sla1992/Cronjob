from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from my_app.models import Cronjob
from .models import Neuigkeiten
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    context = {
        'neuigkeiten': Neuigkeiten.objects.all()
    }

    return render(request, 'cronjobtemplates/home.html', context)


def about(request):
    return render(request, 'cronjobtemplates/about.html', {'title': 'About'})


def login(request):
    return render(request, 'base.html')


def crontable(request):
    all_user_records = Cronjob.objects.filter(user_id=request.user.id)
    return render(request, 'cronjobtemplates/crontable.html', {'all_records': all_user_records})


def index(request):
    if request.method == "POST":
        tablefill = Cronjob()
        tablefill.user_id = request.user.id
        title = request.POST.get('Titel')
        url = request.POST.get('Url')
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        authentification = request.POST.get('onoffswitch')
        if authentification is None:
            authentification = False
        choice1 = request.POST.get('oneChoice')

        if choice1 == '1':
            minute = request.POST.get('minute')
            tablefill.minute = minute
            tablefill.cronjob = minute + " " + " * * * *"
        if choice1 == '2':
            hour = request.POST.get('hour')
            tablefill.hour = hour
            minute = request.POST.get('minutetwo')
            tablefill.minute = minute
            tablefill.cronjob = minute + " " + hour + " * * *"
        if choice1 == '3':
            day = request.POST.get('day')
            tablefill.day = day
            hour = request.POST.get('hourtwo')
            tablefill.hour = hour
            minute = request.POST.get('minutethree')
            tablefill.minute = minute
            tablefill.cronjob = minute + " " + hour + " " + day + " * *"

        tablefill.title = title
        tablefill.url = url
        tablefill.username = username
        tablefill.password = password
        tablefill.authentification = authentification


        tablefill.save()
        return render(request, 'cronjobtemplates/cronjob.html')
    else:
        return render(request, 'cronjobtemplates/cronjob.html')











