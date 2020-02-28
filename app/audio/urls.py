from django.urls import path
from . import views

urlpatterns = [
    path('audio', views.AudioApiView.as_view()),
]