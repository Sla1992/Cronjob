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
        title = request.POST.get('Titel')
        url = request.POST.get('Url')
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        authentification = request.POST.get('onoffswitch')

        tablefill = Cronjob()

        tablefill.title = title
        tablefill.url = url
        tablefill.username = username
        tablefill.password = password
        tablefill.authentification = authentification
        tablefill.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')







