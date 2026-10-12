from django import forms
from django.utils import timezone

from .models import Plomero


class PlomeroForm(forms.ModelForm):
    desde = forms.DateField(
        required=False,
        label="Vigencia desde",
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
    )
    hasta = forms.DateField(
        required=False,
        label="Vigencia hasta",
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = Plomero
        fields = ["sucursal", "cuil", "nombre", "desde", "hasta"]
        widgets = {
            "sucursal": forms.NumberInput(attrs={"min": 0, "max": 99}),
            "cuil": forms.NumberInput(attrs={"inputmode": "numeric"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields["desde"].initial = timezone.localdate()

    def clean(self):
        cleaned = super().clean()
        sucursal = cleaned.get("sucursal")
        cuil = cleaned.get("cuil")
        if sucursal is not None and cuil is not None:
            qs = Plomero.objects.filter(sucursal=sucursal, cuil=cuil)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError(
                    "Ya existe un plomero con esa sucursal y CUIL."
                )
        return cleaned


class PlomeroUpdateForm(PlomeroForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sucursal"].disabled = True
        self.fields["cuil"].disabled = True


class PlomeroBusquedaForm(forms.Form):
    sucursal = forms.IntegerField(
        required=False,
        label="Sucursal",
        help_text="Igual o mayor a este número.",
        widget=forms.NumberInput(attrs={"min": 0}),
    )
    cuil = forms.IntegerField(
        required=False,
        label="CUIL",
        help_text="Igual o mayor a este número.",
        widget=forms.NumberInput(attrs={"inputmode": "numeric"}),
    )
    nombre = forms.CharField(
        required=False,
        label="Apellido y nombre",
        help_text="Contiene el texto indicado.",
    )
    desde = forms.DateField(
        required=False,
        label="Vigencia desde",
        help_text="Igual o posterior a esta fecha.",
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
    )
    hasta = forms.DateField(
        required=False,
        label="Vigencia hasta",
        help_text="Igual o posterior a esta fecha.",
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
    )
