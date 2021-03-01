from django import forms
from django.forms import ModelForm
from .models import Datosbanesco

#se utiliza en form para seleccionar la fecha 
class Entrada_de_fecha(forms.DateInput):
   input_type = 'date'

class FormularioNombre(ModelForm):
    class Meta:
        model = Datosbanesco
        fields = ['nombre', 'fecha_up', 'archivo']
        widgets = {'fecha_up': Entrada_de_fecha() }


#class FormularioNombre(forms.Form):
#    nombre_archivo = forms.CharField(label="Identificador:",  max_length=100)
#    fecha = forms.DateField(label="fecha de subida:",widget=Entrada_de_fecha)
#    archivo = forms.FileField(label="ruta del archivo")
    