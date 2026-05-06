from repository.sessao_repository import SessaoRepository
from repository.cinema_repository import CinemaRepository
from repository.filme_repository import FilmeRepository
from datetime import datetime, timedelta

class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()
        self.cinema_repository = CinemaRepository()
        self.filme_repository = FilmeRepository()

    def cadastrar_sessao(self, sessao):
        """Cadastra uma nova sessão com validações"""
        # Validações
        self._validar_sessao(sessao)
        
        self.repository.salvar(sessao)

    def _validar_sessao(self, sessao):
        """Valida as regras de negócio da sessão"""
        # RN03: Verificar se o público não ultrapassa a capacidade
        cinema = self.cinema_repository.obter_por_id(sessao.cinema_id)
        if not cinema:
            raise ValueError(f"Cinema com ID {sessao.cinema_id} não encontrado")
        
        if sessao.publico > cinema.capacidade:
            raise ValueError(f"Público ({sessao.publico}) não pode ultrapassar a capacidade ({cinema.capacidade})")
        
        # RN04: Verificar intervalo mínimo entre sessões
        sessoes_cinema = self.repository.listar_por_cinema(sessao.cinema_id)
        self._validar_intervalo_sessoes(sessao, sessoes_cinema)
        
        # Verificar se o filme existe
        filme = self.filme_repository.obter_por_id(sessao.filme_id)
        if not filme:
            raise ValueError(f"Filme com ID {sessao.filme_id} não encontrado")

    def _validar_intervalo_sessoes(self, sessao_nova, sessoes_existentes):
        """Valida intervalo mínimo de 15 minutos entre sessões"""
        try:
            data_hora_nova = datetime.strptime(sessao_nova.data_hora, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Formato de data_hora inválido. Use: YYYY-MM-DD HH:MM")
        
        for sessao_existente in sessoes_existentes:
            data_hora_existente = datetime.strptime(sessao_existente.data_hora, "%Y-%m-%d %H:%M")
            
            # Calcular duração do filme
            filme = self.filme_repository.obter_por_id(sessao_existente.filme_id)
            if filme:
                fim_sessao = data_hora_existente + timedelta(minutes=filme.duracao)
                
                # Verificar se há conflito
                diferenca = abs((data_hora_nova - fim_sessao).total_seconds() / 60)
                if diferenca < 15 and data_hora_nova >= data_hora_existente:
                    raise ValueError(f"Intervalo mínimo de 15 minutos entre sessões não respeitado")

    def obter_sessao(self, sessao_id):
        """Obtém uma sessão pelo ID"""
        return self.repository.obter_por_id(sessao_id)

    def listar_sessoes(self):
        """Lista todas as sessões"""
        return self.repository.listar()

    def listar_sessoes_por_cinema(self, cinema_id):
        """Lista sessões de um cinema"""
        return self.repository.listar_por_cinema(cinema_id)

    def listar_sessoes_por_filme(self, filme_id):
        """Lista sessões de um filme"""
        return self.repository.listar_por_filme(filme_id)

    def registrar_publico(self, sessao_id, publico):
        """Registra o público de uma sessão"""
        sessao = self.obter_sessao(sessao_id)
        if not sessao:
            raise ValueError(f"Sessão com ID {sessao_id} não encontrado")
        
        cinema = self.cinema_repository.obter_por_id(sessao.cinema_id)
        
        # RN03: Validar capacidade
        if publico > cinema.capacidade:
            raise ValueError(f"Público ({publico}) não pode ultrapassar a capacidade ({cinema.capacidade})")
        
        sessao.publico = publico
        self.repository.atualizar(sessao)

    def atualizar_sessao(self, sessao):
        """Atualiza uma sessão"""
        self._validar_sessao(sessao)
        self.repository.atualizar(sessao)

    def deletar_sessao(self, sessao_id):
        """Deleta uma sessão"""
        self.repository.deletar(sessao_id)

    def obter_publico_por_sessao(self, sessao_id):
        """Obtém o público de uma sessão específica"""
        sessao = self.obter_sessao(sessao_id)
        return sessao.publico if sessao else 0

    def obter_ocupacao_sessao(self, sessao_id):
        """Calcula a ocupação de uma sessão"""
        sessao = self.obter_sessao(sessao_id)
        if not sessao:
            return 0
        
        cinema = self.cinema_repository.obter_por_id(sessao.cinema_id)
        if not cinema:
            return 0
        
        return sessao.calcular_ocupacao(cinema.capacidade)
