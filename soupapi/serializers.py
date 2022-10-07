from django.contrib.auth.models import User, Group
from rest_framework import serializers

from soupui.models import OID, Device, Service


class ServiceSerializer(serializers.Serializer):
    ip = serializers.CharField(source="device.ip")
    port = serializers.IntegerField(source="device.port")
    community = serializers.CharField(source="device.community")
    identifier = serializers.CharField(source="oid.identifier")
    class Meta:
        model = Service
        fields = ['device__ip', 'device__port', 'device__community', 'oid__identifier']

