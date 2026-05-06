from services.cinema_service import CinemaService
from models.cinema import Cinema

class CinemaController:

    def __init__(self):
        self.service = CinemaService()

    def cadastrar(self, nome, cidade, estado, endereco, capacidade):
        """Cadastra um novo cinema"""
        cinema = Cinema(
            nome,
            cidade,
            estado,
            endereco,
            capacidade
        )
        self.service.cadastrar_cinema(cinema)

    def obter(self, cinema_id):
        """Obtém um cinema pelo ID"""
        return self.service.obter_cinema(cinema_id)

    def listar(self):
        """Lista todos os cinemas"""
        return self.service.listar_cinemas()

    def atualizar(self, cinema_id, nome, cidade, estado, endereco, capacidade):
        """Atualiza um cinema"""
        cinema = Cinema(
            nome,
            cidade,
            estado,
            endereco,
            capacidade,
            id=cinema_id
        )
        self.service.atualizar_cinema(cinema)

    def deletar(self, cinema_id):
        """Deleta um cinema"""
        self.service.deletar_cinema(cinema_id)

    def obter_publico_total(self, cinema_id):
        """Obtém público total de um cinema"""
        return self.service.obter_publico_total_por_cinema(cinema_id)

    def obter_ocupacao_media(self, cinema_id):
        """Obtém ocupação média de um cinema"""
        return self.service.obter_ocupacao_media_cinema(cinema_id)
