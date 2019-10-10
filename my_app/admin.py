from django.contrib import admin

from my_app.models import Cronjob
from my_app.models import Friend


admin.site.register(Cronjob)
admin.site.register(Friend)


