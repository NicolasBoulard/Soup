from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
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


class Criticality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)
    index = models.IntegerField(unique=True)

    class Meta:
        ordering = ["index"]

    def __str__(self):
        return f"{self.name} - {self.index}"


class Threshold(models.Model):
    class Function(models.TextChoices):
        MIN = "MIN", _("Minimum")
        EQUAL = "EQUAL", _("Equal")
        MAX = "MAX", _("Maximum")

    function = models.CharField(
        max_length=5,
        choices=Function.choices,
        default=Function.EQUAL,
    )
    value = models.CharField(max_length=255)
    criticality = models.ForeignKey(Criticality, on_delete=models.CASCADE)

    def get_criticality_code(self, transaction):
        if self.function == "EQUAL":
            if transaction.value == self.value:
                return self.criticality
        if self.function == "MIN":
            if transaction.value <= self.value:
                return self.criticality
        if self.function == "MAX":
            if transaction.value >= self.value:
                return self.criticality
        return None


class Service(models.Model):
    name = models.CharField(max_length=255, default="")
    oid = models.ForeignKey(OID, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    threshold = models.ManyToManyField(Threshold)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.name}"


class Transaction(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=255)
    viewed = models.BooleanField(default=False)
