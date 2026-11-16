
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Aplicativos principais.
    path('', include('core.urls', namespace='core')),
    path('especialidades/', include('especialidades.urls', namespace='especialidades')),
    path('procedimentos/', include('procedimentos.urls', namespace='procedimentos')),

    # Aplicativos desenvolvidos pelo Joshua.
    path('estacoes/', include('estacoes.urls', namespace='estacoes')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
