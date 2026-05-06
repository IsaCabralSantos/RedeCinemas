from repository.filme_repository import FilmeRepository
from repository.sessao_repository import SessaoRepository

class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()
        self.sessao_repository = SessaoRepository()

    def cadastrar_filme(self, filme):
        """Cadastra um novo filme"""
        self.repository.salvar(filme)

    def obter_filme(self, filme_id):
        """Obtém um filme pelo ID"""
        return self.repository.obter_por_id(filme_id)

    def listar_filmes(self):
        """Lista todos os filmes"""
        return self.repository.listar()

    def atualizar_filme(self, filme):
        """Atualiza um filme"""
        self.repository.atualizar(filme)

    def deletar_filme(self, filme_id):
        """Deleta um filme (se não tiver sessões ativas)"""
        # RN07: Não é possível excluir um filme que tenha sessões cadastradas
        sessoes = self.sessao_repository.listar_por_filme(filme_id)
        if sessoes:
            raise ValueError(f"Não é possível deletar o filme. Existem {len(sessoes)} sessão(ões) cadastrada(s).")
        
        self.repository.deletar(filme_id)

    def obter_filmes_em_cartaz_por_cinema(self, cinema_id):
        """Obtém todos os filmes em cartaz em um cinema específico"""
        from repository.sessao_repository import SessaoRepository
        sessao_repo = SessaoRepository()
        sessoes = sessao_repo.listar_por_cinema(cinema_id)
        
        filmes_ids = set()
        filmes = []
        for sessao in sessoes:
            if sessao.filme_id not in filmes_ids:
                filme = self.obter_filme(sessao.filme_id)
                if filme:
                    filmes.append(filme)
                    filmes_ids.add(sessao.filme_id)
        
        return filmes

    def obter_publico_total_por_filme(self, filme_id):
        """Obtém o público total de um filme"""
        sessoes = self.sessao_repository.listar_por_filme(filme_id)
        return sum(sessao.publico for sessao in sessoes)