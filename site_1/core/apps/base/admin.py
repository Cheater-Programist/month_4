from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.base.models import InfoUser, Numbers, Service, Experience, Educations, Skills

# Register your models here.
admin.site.register(InfoUser)
admin.site.register(Numbers)
admin.site.register(Service)
admin.site.register(Experience)
admin.site.register(Educations)
admin.site.register(Skills)

admin.site.unregister(User)
admin.site.unregister(Group)