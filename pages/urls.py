from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sidbar', views.sidbar, name='sidebar'),
    path('contact/', views.contact_us, name='contact'),
    path('about', views.about_us, name='about'),
]

