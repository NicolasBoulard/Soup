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
    path("dashboard/<int:device_id>/", views.dashboard_device, name="dashboard_device"),
    path("log", views.log, {"view_all": False}, name="log"),
    path("log/all", views.log, {"view_all": True}, name="log_all"),
    path("log/<int:log_id>/", views.log_detail, name="log_detail"),
    path("log/<int:log_id>/<int:threshold_id>/", views.log_detail, name="log_detail"),
    path("service/device", views.device, name="device"),
    path("service/device/add", views.device_add, name="device_add"),
    path("service/device/edit/<int:device_id>/", views.device_edit, name="device_edit"),
    path("service/device/remove", views.device_remove, name="device_remove"),
    path("service/OID", views.oid, name="oid"),
    path("service/OID/add", views.oid_add, name="oid_add"),
    path("service/OID/edit/<int:oid_id>/", views.oid_edit, name="oid_edit"),
    path("service/OID/remove", views.oid_remove, name="oid_remove"),
    path("service", views.service, name="service"),
    path("service/add", views.service_add, name="service_add"),
    path("service/edit/<int:service_id>/", views.service_edit, name="service_edit"),
    path("service/remove", views.service_remove, name="service_remove"),
    path("transaction/viewed/<int:transaction_id>/<int:threshold_id>/", views.transaction_check, name="transaction_check"),
    path("transaction/viewed/all/", views.transaction_all_check, name="transaction_all_check"),
]
