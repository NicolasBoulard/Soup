from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class OID(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)


class Device(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    port = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(65535)]
    )
    community = models.CharField(max_length=255)


class Service(models.Model):
    oid = models.ForeignKey(OID, on_delete=models.CASCADE())
    device = models.ForeignKey(Device, on_delete=models.CASCADE())
