from django.contrib import admin

from .models import User, Warnin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Warnin)
