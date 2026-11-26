from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('procedimentos/', include('procedimentos.urls', namespace='procedimentos')),
    path('pessoas/', include('pessoas.urls', namespace='pessoas')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)