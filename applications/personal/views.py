from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from .models import Empleado


class InicioView(TemplateView):
    """vista que carga la pagina views"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = "personal/list_all.html"
    paginate_by = 4
    ordering = "first_name"
    model = Empleado


class ListByAreaEmpleado(ListView):
    template_name = "personal/listar-by-area.html"

    def get_queryset(self):
        area = self.kwargs["shortname"]
        queryset = Empleado.objects.filter(departamento__name=area)
        return queryset


class ListByJobEmpleado(ListView):
    template_name = "personal/listar-by-job.html"

    def get_queryset(self):
        job_employee = self.kwargs["shortname"]
        queryset = Empleado.objects.filter(job=job_employee)
        return queryset


class ListEmpleadosByKword(ListView):
    template_name = "personal/by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        print("**************")
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(first_name=palabra_clave)
        print("lista resultado:", lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = "personal/habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", None)
        lista = Empleado.objects.filter(id=palabra_clave)
        return lista


class EmpleadoDetailView(DetailView):
    model = (
        Empleado  # se debe indicar siempre el modelo sobre el que se hace el detalle
    )
    template_name = "personal/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = "Empleado del mes"
        return context


class SuccessView(TemplateView):
    template_name = "personal/success.html"


class EmpleadoCreateView(CreateView):
    # 4 parametros necesarios para CreatedView
    template_name = "personal/add.html"
    model = Empleado
    # the function ('__all__') add every field to the form
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
        "hoja_vida",
    ]
    success_url = reverse_lazy(
        "personal_app:correcto"
    )  # '.' recarga la misma pagin. '/success' recarga una url definida

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "personal/update.html"
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
        "hoja_vida",
    ]
    success_url = reverse_lazy("personal_app:correcto")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("******metodo POSt*******")
        print("========================")
        print(request.POST)
        print(request.POST["last_name"])
        return super().post(request, *args, *kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'personal/delete.html'
    success_url = reverse_lazy("personal_app:correcto")
