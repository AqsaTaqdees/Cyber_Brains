#url.py is added by self
from django.urls import path
from home import views
urlpatterns = [
    #means if someone randomly visits our website with blank path; then he/she will go ad visit the index function of views and the name of the that path is home.
    path('', views.index, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]