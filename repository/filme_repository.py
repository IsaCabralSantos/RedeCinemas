from database import conectar
from models.filme import Filme

class FilmeRepository:

    def criar_tabela(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            duracao INTEGER NOT NULL,
            genero TEXT NOT NULL,
            diretor TEXT NOT NULL,
            elenco TEXT NOT NULL
        )
        """)

        conn.commit()
        conn.close()

    def salvar(self, filme):
        """Insere um novo filme no banco"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO filmes (titulo, duracao, genero, diretor, elenco)
        VALUES (?, ?, ?, ?, ?)
        """, (
            filme.titulo,
            filme.duracao,
            filme.genero,
            filme.diretor,
            filme.elenco
        ))

        conn.commit()
        conn.close()

    def obter_por_id(self, filme_id):
        """Obtém um filme pelo ID"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM filmes WHERE id = ?", (filme_id,))
        
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return Filme(
                titulo=resultado[1],
                duracao=resultado[2],
                genero=resultado[3],
                diretor=resultado[4],
                elenco=resultado[5],
                id=resultado[0]
            )
        return None

    def listar(self):
        """Lista todos os filmes"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM filmes")

        filmes = []
        for resultado in cursor.fetchall():
            filme = Filme(
                titulo=resultado[1],
                duracao=resultado[2],
                genero=resultado[3],
                diretor=resultado[4],
                elenco=resultado[5],
                id=resultado[0]
            )
            filmes.append(filme)

        conn.close()

        return filmes

    def atualizar(self, filme):
        """Atualiza um filme existente"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE filmes 
        SET titulo = ?, duracao = ?, genero = ?, diretor = ?, elenco = ?
        WHERE id = ?
        """, (
            filme.titulo,
            filme.duracao,
            filme.genero,
            filme.diretor,
            filme.elenco,
            filme.id
        ))

        conn.commit()
        conn.close()

    def deletar(self, filme_id):
        """Deleta um filme"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM filmes WHERE id = ?", (filme_id,))

        conn.commit()
        conn.close()