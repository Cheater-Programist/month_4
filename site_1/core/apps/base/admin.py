from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.base.models import InfoUser

# Register your models here.
admin.site.register(InfoUser)

admin.site.unregister(User)
admin.site.unregister(Group)