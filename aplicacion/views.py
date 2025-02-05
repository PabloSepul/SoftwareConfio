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

def filtro(request):
    return render(request, 'aplicacion/filtro.html')

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
            return redirect(to="productos_filtrados")
        
    return render(request,'aplicacion/editprod.html', datos)

def editrep(request, id):
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
            messages.warning(request,'Reparacion modificada exitosamente')
            return redirect(to="catalogorep")
        
    return render(request,'aplicacion/editrep.html', datos)
    
def nuevosproductos(request):
    
    form=ProductoForm()
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request,'Producto agregado exitosamente')
            return redirect(to="productos_filtrados")
        
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
        if producto.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+producto.imagen.url))
        producto.delete()
        messages.error(request, 'Producto eliminado exitosamente')
        return redirect(to='productos_filtrados')
    
    return render(request, 'aplicacion/eliminarprod.html',datos)


def eliminarep(request, id):
    reparacion=get_object_or_404(Reparacion, id=id)
    
    datos={
        "reparacion":reparacion
    }
    
    if request.method=="POST":
        if reparacion.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+reparacion.imagen.url))
        reparacion.delete()
        messages.error(request, 'Reparación eliminada exitosamente')
        return redirect(to='catalogorep')
    
    return render(request, 'aplicacion/eliminarep.html',datos)

def completar(request,id):
    reparacion=get_object_or_404(Reparacion, id=id)
    
    datos={
        "reparacion":reparacion
    }
    
    if request.method=="POST":
        if reparacion.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+reparacion.imagen.url))
        reparacion.delete()
        messages.error(request, 'Reparación completada exitosamente')
        return redirect(to='catalogorep')
    
    return render(request, 'aplicacion/completar.html',datos)

def productos_filtrados(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(stock=query).order_by('stock')
    else:
        productos = Producto.objects.order_by('stock')
    return render(request, 'aplicacion/productos_filtrados.html', {'productos': productos, 'query': query})