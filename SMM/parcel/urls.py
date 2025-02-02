from django.urls import path 
from . import views 

app_name = "parcel"

urlpatterns = [
    path("", views.index, name="index"),
    path("choose", views.choose, name="choose"),
    path("add/<str:sender>", views.add, name="add"),
    path("search", views.search, name="search")
]