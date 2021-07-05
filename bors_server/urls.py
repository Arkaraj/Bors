from bors_server import api
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.users, name="users"),
    path("api/v1/dogs/", api.getAllDogs),
    path("api/v1/dogs/<int:id>", api.getSpecificDog),
    path("api/v1/dogs/add", api.addDog),
    path("api/v1/dogs/add/<int:id>", api.addOwnerToDog),
    path("api/v1/dogs/delete/<int:id>", api.removeDog),
    path("api/v1/users/", api.getAllUsers),
    path("api/v1/users/<int:id>", api.getSpecificUser),
    path("api/v1/users/add", api.addUser),
]
