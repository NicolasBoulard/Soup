from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class OID(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.name}"


class Device(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    port = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(65535)], default=161
    )
    community = models.CharField(max_length=255)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.name}"


class Service(models.Model):
    name = models.CharField(max_length=255, default="")
    oid = models.ForeignKey(OID, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.name}"


class Transaction(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=255)
