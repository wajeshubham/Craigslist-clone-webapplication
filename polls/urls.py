from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.home, name='home page'),
    path('new_search', views.new_search, name='new_search'),
    path('about',views.about,name='about'),
    path('contact_us',views.contact_us,name="contact_us")
]
