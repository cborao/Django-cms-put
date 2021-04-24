from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:key>', views.get_content),
]
