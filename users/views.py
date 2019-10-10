from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_vaild():
            username = form.cleaned_date.get('username')
            messages.success(request, f'account created for {username}!')
            return redirect('homepage')

    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
