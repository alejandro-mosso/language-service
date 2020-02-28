from django.urls import path
from . import views

urlpatterns = [
    path('youglish', views.YouglishApiView.as_view()),
]