class Cinema:
    def __init__(self, nome, cidade, estado, endereco, capacidade, id=None):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco
        self.capacidade = capacidade

    def __repr__(self):
        return f"Cinema(id={self.id}, nome='{self.nome}', cidade='{self.cidade}', capacidade={self.capacidade})"
