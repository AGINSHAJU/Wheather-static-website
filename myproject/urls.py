from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.index,name="index"),
   path('whether/', views.whether, name="whether"), 
   path('about/', views.about, name='about'),

]
