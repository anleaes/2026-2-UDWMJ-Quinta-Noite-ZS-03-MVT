from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('procedimentos/', include('procedimentos.urls', namespace='procedimentos')),
    path('avaliacoes/', include('avaliacoes.urls', namespace='avaliacoes')),
    path('agendamentos/', include('agendamentos.urls', namespace='agendamentos')),
    path('atendimentos/', include('atendimentos.urls', namespace='atendimentos')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('profissionais/', include('profissionais.urls', namespace='profissionais')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
