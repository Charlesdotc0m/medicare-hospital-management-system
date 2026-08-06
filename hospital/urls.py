from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('department/', views.department, name='department'),
    path('doctor/', views.doctor, name='doctor'),
    path('register/', views.register, name='register'),
    path('appointments/', views.appointments, name='appointments'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
]