from django.contrib import admin

from .models import Caveat, CaveatManager

admin.site.register(Caveat)
admin.site.register(CaveatManager)
