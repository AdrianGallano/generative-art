from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.ArtCreateView.as_view(), name='main'),
    path('success/', views.success, name='success'),
]