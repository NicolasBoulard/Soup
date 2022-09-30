from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Community(models.Model):
    pass


class OID(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)

class (models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE(),)
    oid = models.M
class Device(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    port = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(65535)]
    )
