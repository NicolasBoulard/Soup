from rest_framework import viewsets
from rest_framework import permissions

from soupui.models import Service
from .serializers import ServiceSerializer




class ServiceList(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAuthenticated]
