app_name="second"

from django.urls import path
from app2.views import *

urlpatterns = [
    path("index2/",index2,name="index2"),
    path("new2/",new2,name="new2"),
]
