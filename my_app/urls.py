from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cronjob-home'),
    path('about/', views.about, name='cronjob-about'),
    path('cronjob/', views.index, name='cronjob-cronjob')
]