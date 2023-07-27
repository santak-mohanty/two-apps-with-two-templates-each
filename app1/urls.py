app_name="first"

from django.urls import path
from app1.views import *

urlpatterns=[
    path("index1/",index1,name="index1"),
    path("new1/",new1,name="new1"),
]