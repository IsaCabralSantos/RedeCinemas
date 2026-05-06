from services.sessao_service import SessaoService
from models.sessao import Sessao

class SessaoController:

    def __init__(self):
        self.service = SessaoService()

    def cadastrar(self, cinema_id, filme_id, data_hora):
        """Cadastra uma nova sessão"""
        sessao = Sessao(
            cinema_id,
            filme_id,
            data_hora
        )
        self.service.cadastrar_sessao(sessao)

    def obter(self, sessao_id):
        """Obtém uma sessão pelo ID"""
        return self.service.obter_sessao(sessao_id)

    def listar(self):
        """Lista todas as sessões"""
        return self.service.listar_sessoes()

    def listar_por_cinema(self, cinema_id):
        """Lista sessões de um cinema"""
        return self.service.listar_sessoes_por_cinema(cinema_id)

    def listar_por_filme(self, filme_id):
        """Lista sessões de um filme"""
        return self.service.listar_sessoes_por_filme(filme_id)

    def registrar_publico(self, sessao_id, publico):
        """Registra o público de uma sessão"""
        self.service.registrar_publico(sessao_id, publico)

    def atualizar(self, sessao_id, cinema_id, filme_id, data_hora, publico):
        """Atualiza uma sessão"""
        sessao = Sessao(
            cinema_id,
            filme_id,
            data_hora,
            publico,
            id=sessao_id
        )
        self.service.atualizar_sessao(sessao)

    def deletar(self, sessao_id):
        """Deleta uma sessão"""
        self.service.deletar_sessao(sessao_id)

    def obter_publico(self, sessao_id):
        """Obtém o público de uma sessão"""
        return self.service.obter_publico_por_sessao(sessao_id)

    def obter_ocupacao(self, sessao_id):
        """Obtém a ocupação de uma sessão"""
        return self.service.obter_ocupacao_sessao(sessao_id)
