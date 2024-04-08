from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.views.generic import FormView, CreateView, View
from django.urls import reverse_lazy
from .models import Art
from .forms import ArtForm
from django.contrib.auth.mixins import LoginRequiredMixin

def success(request):
    return HttpResponse("Your art has been submitted successfully!")

class ArtCreateView(LoginRequiredMixin, View):
    def post(self, request):
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponsePermanentRedirect(reverse_lazy("core:success"))
        else:
            return render(request, 'art/main.html', {'form': form})

    def get(self, request):
        form = ArtForm()
        return render(request, 'art/main.html', {'form': form})
