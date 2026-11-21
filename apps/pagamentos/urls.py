
from django.urls import path
from pagamentos import views

app_name = 'pagamentos'

urlpatterns = [
    path('listar/', views.listar_pagamentos, name='listar_pagamentos'),
    path('cadastrar/', views.criar_pagamento, name='criar_pagamento'),
    path('editar/<int:id>/', views.editar_pagamento, name='editar_pagamento'),
    path('excluir/<int:id>/', views.excluir_pagamento, name='excluir_pagamento'),
]
