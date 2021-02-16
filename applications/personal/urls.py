from django.contrib import admin
from django.urls import path

from . import views

app_name = "personal_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path("listar-todo-empleados/", views.ListAllEmpleados.as_view()),
    path("listar-by-area/<shortname>/", views.ListByAreaEmpleado.as_view()),
    path("listar-by-job/<shortname>/", views.ListByJobEmpleado.as_view()),
    path("buscar-empleado/", views.ListEmpleadosByKword.as_view()),
    path("lista-habilidades-empleado/", views.ListHabilidadesEmpleado.as_view()),
    path("ver-empleado/<pk>/", views.EmpleadoDetailView.as_view()),
    path("add-empleado/", views.EmpleadoCreateView.as_view()),
    path(
        "success/", 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        "update-empleado/<pk>/", 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
    ),
    path(
        "delete-empleado/<pk>/", 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
    ),
]
