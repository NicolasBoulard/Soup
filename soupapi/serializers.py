from rest_framework import serializers

from soupui.models import Service


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ip = serializers.CharField(source="device.ip")
    port = serializers.IntegerField(source="device.port")
    community = serializers.CharField(source="device.community")
    identifier = serializers.CharField(source="oid.identifier")

    class Meta:
        model = Service
        fields = ["device__ip", "device__port", "device__community", "oid__identifier"]
