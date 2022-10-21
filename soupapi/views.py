from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from soupui.models import Service, Transaction
from .serializers import ServiceSerializer


class ServiceList(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

class TransactionView(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, service_id=None):
        value = request.data['value']
        service = Service.objects.get(id=service_id)
        if service:
            Transaction.objects.create(service=service, value=value)
            return Response('', status=status.HTTP_201_CREATED)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)