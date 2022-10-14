from django.urls import path

from . import views
from django.contrib.auth import views as authviews
from .forms import UserLoginForm

urlpatterns = [
    path('login/', authviews.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
            ),
        name='login'),
    path('', views.index),
]
