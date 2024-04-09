from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.views.generic import FormView, CreateView, View
from django.urls import reverse_lazy
from .models import Art
from .forms import ArtForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .patterns import Pattern

def success(request):
    return HttpResponse("Your art has been submitted successfully!")

class ArtCreateView(LoginRequiredMixin, View):
    def post(self, request):
        form = ArtForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user

            title = form.cleaned_data.get('title')
            resolution_width = form.cleaned_data.get('resolution_width')
            resolution_height = form.cleaned_data.get('resolution_height')
            no_of_circles = form.cleaned_data.get('no_of_circles')
            max_color_cycle = form.cleaned_data.get('max_color_cycle')
            parameters = [form.cleaned_data.get(f'parameter_{i}') for i in range(1, 6)]
            
            image_path = Pattern.create(
                user_id=request.user.id,
                title=title,
                image_size=(resolution_width, resolution_height),
                num_circles=no_of_circles,
                max_color_cycle=max_color_cycle,
                parameters=parameters
            )

            form.instance.image = image_path
            form.save()
            return HttpResponsePermanentRedirect(reverse_lazy("core:main") + f'?image_path={image_path}')
        else:
            return render(request, 'art/main.html', {'form': form})

    def get(self, request):
        form = ArtForm()

        if request.GET.get("image_path") is not None:
            image_path = request.GET["image_path"]
            return render(request, 'art/main.html', {'form':form, 'image_path': image_path})

        return render(request, 'art/main.html', {'form': form})



