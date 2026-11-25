
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AutenticacaoTest(TestCase):

    def setUp(self):
        # Cria um usuário de teste para validar a autenticação.
        User = get_user_model()
        self.usuario = User.objects.create_user(
            username='usuario_teste',
            password='senha_teste_123'
        )

    # Verifica se usuários não autenticados são redirecionados ao login.
    def test_home_redireciona_usuario_nao_autenticado(self):
        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('core:login'), response.url)

    # Verifica se usuários autenticados conseguem acessar a página inicial.
    def test_home_acessivel_usuario_autenticado(self):
        self.client.login(
            username='usuario_teste',
            password='senha_teste_123'
        )

        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)

    # Verifica se a tela de login permanece pública.
    def test_login_acessivel_sem_autenticacao(self):
        response = self.client.get(reverse('core:login'))

        self.assertEqual(response.status_code, 200)
