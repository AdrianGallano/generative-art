from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view() , name="register"),
    path("registration_successful/", views.RegisterView.success , name="registration_successful"),
    path("login/", views.LoginView.as_view() , name="login"),
    path("logout/", views.LoginView.user_logout, name="logout"),
]