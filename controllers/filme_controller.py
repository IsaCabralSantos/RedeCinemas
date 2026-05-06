from services.filme_service import FilmeService
from models.filme import Filme

class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrar(self, titulo, duracao, genero, diretor, elenco):
        """Cadastra um novo filme"""
        filme = Filme(
            titulo,
            duracao,
            genero,
            diretor,
            elenco
        )
        self.service.cadastrar_filme(filme)

    def obter(self, filme_id):
        """Obtém um filme pelo ID"""
        return self.service.obter_filme(filme_id)

    def listar(self):
        """Lista todos os filmes"""
        return self.service.listar_filmes()

    def atualizar(self, filme_id, titulo, duracao, genero, diretor, elenco):
        """Atualiza um filme"""
        filme = Filme(
            titulo,
            duracao,
            genero,
            diretor,
            elenco,
            id=filme_id
        )
        self.service.atualizar_filme(filme)

    def deletar(self, filme_id):
        """Deleta um filme"""
        self.service.deletar_filme(filme_id)

    def obter_filmes_em_cartaz(self, cinema_id):
        """Obtém filmes em cartaz em um cinema"""
        return self.service.obter_filmes_em_cartaz_por_cinema(cinema_id)

    def obter_publico_total(self, filme_id):
        """Obtém público total de um filme"""
        return self.service.obter_publico_total_por_filme(filme_id)