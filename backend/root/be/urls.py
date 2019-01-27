from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BEView.as_view(), name='BEView'),
]
