from django.urls import path

from . import views

app_name = "plomeros"

urlpatterns = [
    path("", views.PlomeroListView.as_view(), name="list"),
    path("plomeros/buscar/", views.PlomeroSearchView.as_view(), name="search"),
    path("plomeros/nuevo/", views.PlomeroCreateView.as_view(), name="create"),
    path("plomeros/<int:pk>/editar/", views.PlomeroUpdateView.as_view(), name="update"),
    path("plomeros/<int:pk>/eliminar/", views.PlomeroDeleteView.as_view(), name="delete"),
]
