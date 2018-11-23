from . import views
from django.urls import path, include

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('gallery', views.gallery, name='gallery'),
    path('elements', views.elements, name='element'),
    path('blog2', views.blog2, name='blog2'),
    path('blog1', views.blog1, name='blog1'),
   ]