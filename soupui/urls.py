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
    path("", views.index),
]
