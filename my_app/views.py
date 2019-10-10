import value as value
from django.shortcuts import render, redirect


# Create your views here.


# def index(request):
#     if request.method == "POST":
#         form = CronjobForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     form = CronjobForm()
#     return render(request, 'index.html', {'form': form})
from my_app.models import Cronjob


def index(request):
    if request.method == "POST":
        tablefill = Cronjob()
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
        if choice1 == '2':
            hour = request.POST.get('hour')
            tablefill.hour = hour
            minute = request.POST.get('minutetwo')
            tablefill.minute = minute
        if choice1 == '3':
            day = request.POST.get('day')
            tablefill.day = day
            hour = request.POST.get('hourtwo')
            tablefill.hour = hour
            minute = request.POST.get('minutethree')
            tablefill.minute = minute

        tablefill.title = title
        tablefill.url = url
        tablefill.username = username
        tablefill.password = password
        tablefill.authentification = authentification

        tablefill.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')







