from django import forms

from my_app.models import Cronjob


class CronjobForm(forms.ModelForm):
    class Meta:
        model = Cronjob
        fields = ('title', 'url', 'authentification', 'username', 'password', 'auswahl')
