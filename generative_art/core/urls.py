from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.ArtCreateView.as_view(), name='art'),
    path('success/', views.success, name='art_success'),
]