from django.contrib import admin

from soupui.models import OID, Service, Device, Transaction, Criticality, Threshold

# Register your models here.
admin.site.register(OID)
admin.site.register(Device)
admin.site.register(Service)
admin.site.register(Transaction)
admin.site.register(Criticality)
admin.site.register(Threshold)
