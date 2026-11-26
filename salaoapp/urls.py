
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial e autenticação
    path('', include('core.urls', namespace='core')),

    # Cadastros e catálogo
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('procedimentos/', include('procedimentos.urls', namespace='procedimentos')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('pessoas/', include('pessoas.urls', namespace='pessoas')),

    # Operacional
    path('avaliacoes/', include('avaliacoes.urls', namespace='avaliacoes')),
    path('agendamentos/', include('agendamentos.urls', namespace='agendamentos')),
    path('atendimentos/', include('atendimentos.urls', namespace='atendimentos')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
    path('profissionais/', include('profissionais.urls', namespace='profissionais')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
