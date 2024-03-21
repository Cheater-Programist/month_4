from django.contrib import admin
from apps.base.models import *

# Register your models here.
class ContactFilterAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("name", )
    search_fields = ("name", )
    readonly_fields = ("message", )
admin.site.register(Contact, ContactFilterAdmin)