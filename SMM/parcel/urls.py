from django.urls import path 
from . import views 

app_name = "parcel"

urlpatterns = [
    path("", views.index, name="index")
]