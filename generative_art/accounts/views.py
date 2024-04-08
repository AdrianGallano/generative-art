from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
)
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.views.generic import View
from django.contrib.auth.models import User



class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("core:art"))
        
        form = RegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:registration_successful"))
        else:
            return render(request, "accounts/register.html", {"form":form})
        
    @staticmethod
    def success(request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("core:art"))
        
        return render(request, "accounts/registration_successful.html", {})

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponsePermanentRedirect(reverse("core:art"))

        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user  = User.objects.get(username=request.POST["username"])
            login(request, user)
            return HttpResponsePermanentRedirect(reverse("core:art"))

        return render(request, "accounts/login.html", {"form": form})
    
    @staticmethod
    def user_logout(request):
        logout(request)
        return HttpResponsePermanentRedirect(reverse("accounts:login"))



