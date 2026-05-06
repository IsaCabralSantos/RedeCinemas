class Filme:
    def __init__(self, titulo, duracao, genero, diretor, elenco, id=None):
        self.id = id
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero
        self.diretor = diretor
        self.elenco = elenco

    def __repr__(self):
        return f"Filme(id={self.id}, titulo='{self.titulo}', duracao={self.duracao}min, genero='{self.genero}')"