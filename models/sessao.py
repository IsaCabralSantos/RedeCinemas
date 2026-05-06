from datetime import datetime

class Sessao:
    def __init__(self, cinema_id, filme_id, data_hora, publico=0, id=None):
        self.id = id
        self.cinema_id = cinema_id
        self.filme_id = filme_id
        self.data_hora = data_hora  # formato: "2026-05-06 19:30"
        self.publico = publico

    def calcular_ocupacao(self, capacidade_cinema):
        """Calcula a ocupação percentual da sessão"""
        if capacidade_cinema == 0:
            return 0
        return (self.publico / capacidade_cinema) * 100

    def __repr__(self):
        return f"Sessao(id={self.id}, cinema_id={self.cinema_id}, filme_id={self.filme_id}, data_hora='{self.data_hora}', publico={self.publico})"
