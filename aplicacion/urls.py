from django.urls import path, include
from sitio import settings
from django.conf.urls.static import static
from .views import index, about, contact, gallery, testimonial, eliminarprod, editprod, catalogo, nuevosproductos, editarcompra, dashboard, nuevosreparaciones, catalogorep


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('gallery', gallery, name='gallery'),
    path('testimonial', testimonial, name='testimonial'),
    path('eliminarprod/<id>',eliminarprod, name='eliminarprod'),
    path('editprod/<id>', editprod, name='editprod'),
    path('catalogo/', catalogo, name='catalogo'),
    path('nuevosproductos/',nuevosproductos,name='nuevosproductos'),
    path('editarcompra/',editarcompra,name='editarcompra'),
    path('dashboard/',dashboard,name='dashboard'),
    path('nuevosreparaciones/',nuevosreparaciones,name='nuevosreparaciones'),
    path('catalogorep/',catalogorep, name='catalogorep'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)