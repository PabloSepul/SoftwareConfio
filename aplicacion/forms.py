from django import forms
from .models import Producto,Reparacion

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','stock', 'precio','imagen']
        

class UpdateProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion','stock', 'precio', 'imagen']
        

class ReparacionForm(forms.ModelForm):
    
    class Meta:
        model = Reparacion
        fields = ['nombre','descripcion', 'costo','imagen']
        

class UpdateReparacionForm(forms.ModelForm):
    
    class Meta:
        model = Reparacion
        fields = ['nombre', 'descripcion', 'costo', 'imagen']