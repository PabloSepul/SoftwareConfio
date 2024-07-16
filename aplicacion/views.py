from django.shortcuts import render
from .models import Producto,Reparacion
from .forms import ProductoForm, UpdateProductoForm, ReparacionForm, UpdateReparacionForm
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
from os import path, remove

# Create your views here.

def index(request):
    return render(request, 'aplicacion/index.html')

def about(request):
    return render(request, 'aplicacion/about.html')

def contact(request):
    return render(request, 'aplicacion/contact.html')

def gallery(request):
    return render(request, 'aplicacion/gallery.html')

def testimonial(request):
    return render(request, 'aplicacion/testimonial.html')

def editarcompra(request):
    return render(request,'aplicacion/editarcompra.html')

def dashboard(request):
    return render(request,'aplicacion/dashboard.html')

def catalogorep(request):
    reparacion=Reparacion.objects.all()
    
    datos={
        "reparacion":reparacion
    }
    return render(request,'aplicacion/catalogorep.html', datos)

def editprod(request, id):
    producto=get_object_or_404(Producto, id=id)
    
    form=UpdateProductoForm(instance=producto)
    datos={
        "form":form,
        "producto":producto
    }
    
    if request.method=="POST":
        form=UpdateProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.warning(request,'Producto modificado exitosamente')
            return redirect(to="catalogo")
        
    return render(request,'aplicacion/editprod.html', datos)
    
def nuevosproductos(request):
    
    form=ProductoForm()
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request,'Producto agregado exitosamente')
            return redirect(to="catalogo")
        
    datos={
        "form":form
    }
    return render(request,'aplicacion/nuevosproductos.html', datos)

def nuevosreparaciones(request):
    
    form=ReparacionForm()
    
    if request.method=="POST":
        form=ReparacionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request,'Reparacion agregada exitosamente')
            return redirect(to="catalogorep")
    
    datos={
        "form":form
    }
    return render(request,'aplicacion/nuevosreparaciones.html', datos)

def editprod(request, id):
    reparacion=get_object_or_404(Reparacion, id=id)
    
    form=UpdateReparacionForm(instance=reparacion)
    datos={
        "form":form,
        "reparacion":reparacion
    }
    
    if request.method=="POST":
        form=UpdateReparacionForm(data=request.POST, files=request.FILES, instance=reparacion)
        if form.is_valid():
            form.save()
            messages.warning(request,'Reparacion Modificada Exitosamente')
            return redirect(to="catalogorep") #Remplazar por catalogo reparaciones
        
    return render(request,'aplicacion/editprod.html', datos) #Remplazar por editar reparaciones
    

def catalogo(request):
    producto=Producto.objects.all()
    
    datos={
        "producto":producto
    }
    return render(request, 'aplicacion/catalogo.html', datos)

def eliminarprod(request, id):
    producto=get_object_or_404(Producto, id=id)
    
    datos={
        "producto":producto
    }
    
    if request.method=="POST":
        if productos.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+productos.imagen.url))
        productos.delete()
        messages.error(request, 'Producto eliminado exitosamente')
        return redirect(to='catalogo')
    
    return render(request, 'aplicacion/eliminarprod.html',datos)