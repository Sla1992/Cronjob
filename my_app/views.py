from django import forms
from django.shortcuts import render, redirect


# Create your views here.
from my_app.forms import CronjobForm


def index(request):
    if request.method == "POST":
        form = CronjobForm(request.POST)
        if form.is_valid():
            form.save()

    form = CronjobForm()
    return render(request, 'index.html', {'form': form})







