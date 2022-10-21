from django.urls import path

from . import views
from django.contrib.auth import views as authviews
from .forms import UserLoginForm

urlpatterns = [
    path(
        "login/",
        authviews.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm,
            next_page="/",
        ),
        name="login",
    ),
    path(
        "logout/",
        authviews.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("service", views.service, name="service"),
    path("service/device", views.device, name="device"),
    path("service/device/add", views.device_add, name="device_add"),
    path("service/device/edit/<int:device_id>/", views.device_edit, name="device_edit"),
    path("service/device/remove", views.device_remove, name="device_remove"),
    path("service/OID", views.oid, name="oid"),
]
