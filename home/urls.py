from django.urls import path
from .views import *
# urls.py
urlpatterns = [
    path("",index,name='index'),
    path("index",index,name='index'),
    path("about",about,name='about'),
    path("courses",courses,name='courses'),
    path("services",services,name='services'),
    path("pricing",pricing,name='pricing'),
    path("gallery",gallery,name='gallery'),
    path("contact",contact,name='contact'),
]
