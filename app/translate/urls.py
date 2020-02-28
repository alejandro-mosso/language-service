from django.urls import path
from . import views

urlpatterns = [
    path('translate', views.TranslateApiView.as_view()),
]