from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('not_found/', views.not_found, name='not_found'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]