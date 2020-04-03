from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('sign', views.sign, name='sign'),
]