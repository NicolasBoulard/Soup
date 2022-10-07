from django.contrib import admin

from soupui.models import OID, Service, Device

# Register your models here.
admin.site.register(OID)
admin.site.register(Device)
admin.site.register(Service)
