from django.conf.urls import url, include
from home import views

app_name = 'home'

urlpatterns = [
    url('', views.home, name='home'),
    
    url('about', views.about, name='about'),
    url('cars', views.cars, name='cars'),
    url('contact', views.contact, name='contact'),
    url('service', views.service, name='service'),
    url('gallery', views.gallery, name='gallery'),
    url('elements', views.elements, name='element'),
    url('blog2', views.blog2, name='blog2'),
    url('blog1', views.blog1, name='blog1'),
   ]
 