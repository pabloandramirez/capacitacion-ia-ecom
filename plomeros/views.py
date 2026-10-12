from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import PlomeroBusquedaForm, PlomeroForm, PlomeroUpdateForm
from .models import Plomero


class PlomeroListView(ListView):
    model = Plomero
    template_name = "plomeros/plomero_list.html"
    context_object_name = "plomeros"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = ctx["plomeros"]
        ctx["total"] = qs.count()
        sucursales = list(
            qs.order_by("sucursal")
            .values_list("sucursal", flat=True)
            .distinct()
        )
        ctx["sucursal"] = sucursales[0] if len(sucursales) == 1 else "Todas"
        return ctx


class PlomeroCreateView(CreateView):
    model = Plomero
    form_class = PlomeroForm
    template_name = "plomeros/plomero_form.html"
    success_url = reverse_lazy("plomeros:list")
    extra_context = {
        "titulo": "Alta de plomero",
        "bajada": "Cargá un nuevo plomero en el registro. La sucursal y el CUIL identifican el legajo.",
        "accion": "Guardar plomero",
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Plomero {self.object.nombre} dado de alta.")
        return response


class PlomeroUpdateView(UpdateView):
    model = Plomero
    form_class = PlomeroUpdateForm
    template_name = "plomeros/plomero_form.html"
    success_url = reverse_lazy("plomeros:list")
    extra_context = {
        "titulo": "Modificar plomero",
        "bajada": "La sucursal y el CUIL no se editan: identifican el legajo.",
        "accion": "Guardar cambios",
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Plomero {self.object.nombre} actualizado.")
        return response


class PlomeroDeleteView(DeleteView):
    model = Plomero
    template_name = "plomeros/plomero_confirm_delete.html"
    success_url = reverse_lazy("plomeros:list")

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Plomero {nombre} eliminado.")
        return response


class PlomeroSearchView(ListView):
    model = Plomero
    template_name = "plomeros/plomero_search.html"
    context_object_name = "resultados"

    def get_queryset(self):
        self.form = PlomeroBusquedaForm(self.request.GET)
        qs = Plomero.objects.all()
        if not self.form.is_valid():
            return qs.none()
        d = self.form.cleaned_data
        if d.get("sucursal") is not None:
            qs = qs.filter(sucursal__gte=d["sucursal"])
        if d.get("cuil") is not None:
            qs = qs.filter(cuil__gte=d["cuil"])
        if d.get("nombre"):
            qs = qs.filter(nombre__icontains=d["nombre"])
        if d.get("desde") is not None:
            qs = qs.filter(desde__gte=d["desde"])
        if d.get("hasta") is not None:
            qs = qs.filter(hasta__gte=d["hasta"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = self.form
        ctx["coincidencias"] = ctx["resultados"].count()
        return ctx
