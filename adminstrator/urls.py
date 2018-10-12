from . import views
from django.urls import path, include

app_name = 'adminstrator'

urlpatterns = [
   
    path('dashboard', views.dashboard, name='dashboard'),
    path('icons', views.icons, name='icons'),
    path('maps', views.maps, name='maps'),
    
    path('carlist', views.carlist, name='carlist'),
   
    path('typography', views.typography, name='typography'),
    path('table', views.table, name='table'),
    path('notification', views.notification, name='notification'),
    path('user', views.user, name='user'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('addcar', views.addcar, name='addcar'),
    path('editcar/<int:carid>', views.addcar, name='addcar'),
    path('updatecar', views.updatecar, name='updatecar'),
    path('delete/<int:carid>', views.deletecar, name='deletecar'),
]