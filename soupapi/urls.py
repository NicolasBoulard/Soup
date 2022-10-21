from django.urls import path, include
from rest_framework import routers

from . import views
from .views import TransactionView

router = routers.DefaultRouter()
router.register(r"services", views.ServiceList)

urlpatterns = [
    path("transaction/<int:service_id>/", TransactionView.as_view(), name="transaction_add"),
    path("", include(router.urls)),
]
