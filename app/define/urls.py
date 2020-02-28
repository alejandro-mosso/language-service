from django.urls import path
from . import views

urlpatterns = [
    path('define', views.DefineApiView.as_view()),
]