from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.weather, name='weather'),  # Updated to match the view function name
    path('about/', views.about, name='about'),

]

