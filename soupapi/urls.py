from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'service/all', views.ServiceList)

urlpatterns = [
    path('', include(router.urls)),
]
