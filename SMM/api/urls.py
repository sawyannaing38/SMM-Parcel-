from django.urls import path 
from . import views 

urlpatterns = [
    path("take/<int:id>", views.take, name="take"),
    path("create/", views.create, name="create")
]