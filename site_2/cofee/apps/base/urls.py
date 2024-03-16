from django.urls import path
from apps.base.views import *

urlpatterns = [
    path('', index, name="index_url"),
    path('about-us/', about, name="about_us_url"),
]