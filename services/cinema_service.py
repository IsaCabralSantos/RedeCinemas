from repository.cinema_repository import CinemaRepository
from repository.sessao_repository import SessaoRepository

class CinemaService:

    def __init__(self):
        self.repository = CinemaRepository()
        self.sessao_repository = SessaoRepository()

    def cadastrar_cinema(self, cinema):
        """Cadastra um novo cinema"""
        self.repository.salvar(cinema)

    def obter_cinema(self, cinema_id):
        """Obtém um cinema pelo ID"""
        return self.repository.obter_por_id(cinema_id)

    def listar_cinemas(self):
        """Lista todos os cinemas"""
        return self.repository.listar()

    def atualizar_cinema(self, cinema):
        """Atualiza um cinema"""
        self.repository.atualizar(cinema)

    def deletar_cinema(self, cinema_id):
        """Deleta um cinema (se não tiver sessões ativas)"""
        # RN07: Não é possível excluir um cinema que tenha sessões cadastradas
        sessoes = self.sessao_repository.listar_por_cinema(cinema_id)
        if sessoes:
            raise ValueError(f"Não é possível deletar o cinema. Existem {len(sessoes)} sessão(ões) cadastrada(s).")
        
        self.repository.deletar(cinema_id)

    def obter_publico_total_por_cinema(self, cinema_id):
        """Obtém o público total de um cinema"""
        sessoes = self.sessao_repository.listar_por_cinema(cinema_id)
        return sum(sessao.publico for sessao in sessoes)

    def obter_ocupacao_media_cinema(self, cinema_id):
        """Calcula a ocupação média de um cinema"""
        cinema = self.obter_cinema(cinema_id)
        if not cinema:
            return 0
        
        sessoes = self.sessao_repository.listar_por_cinema(cinema_id)
        if not sessoes:
            return 0
        
        ocupacoes = [sessao.calcular_ocupacao(cinema.capacidade) for sessao in sessoes]
        return sum(ocupacoes) / len(ocupacoes)
