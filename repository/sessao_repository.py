from database import conectar
from models.sessao import Sessao

class SessaoRepository:

    def criar_tabela(self):
        """Cria a tabela de sessões se não existir"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id INTEGER NOT NULL,
            filme_id INTEGER NOT NULL,
            data_hora TEXT NOT NULL,
            publico INTEGER DEFAULT 0,
            FOREIGN KEY (cinema_id) REFERENCES cinemas(id),
            FOREIGN KEY (filme_id) REFERENCES filmes(id)
        )
        """)

        conn.commit()
        conn.close()

    def salvar(self, sessao):
        """Insere uma nova sessão no banco"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO sessoes (cinema_id, filme_id, data_hora, publico)
        VALUES (?, ?, ?, ?)
        """, (
            sessao.cinema_id,
            sessao.filme_id,
            sessao.data_hora,
            sessao.publico
        ))

        conn.commit()
        conn.close()

    def obter_por_id(self, sessao_id):
        """Obtém uma sessão pelo ID"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sessoes WHERE id = ?", (sessao_id,))
        
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return Sessao(
                cinema_id=resultado[1],
                filme_id=resultado[2],
                data_hora=resultado[3],
                publico=resultado[4],
                id=resultado[0]
            )
        return None

    def listar(self):
        """Lista todas as sessões"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sessoes")

        sessoes = []
        for resultado in cursor.fetchall():
            sessao = Sessao(
                cinema_id=resultado[1],
                filme_id=resultado[2],
                data_hora=resultado[3],
                publico=resultado[4],
                id=resultado[0]
            )
            sessoes.append(sessao)

        conn.close()

        return sessoes

    def listar_por_cinema(self, cinema_id):
        """Lista todas as sessões de um cinema"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sessoes WHERE cinema_id = ? ORDER BY data_hora", (cinema_id,))

        sessoes = []
        for resultado in cursor.fetchall():
            sessao = Sessao(
                cinema_id=resultado[1],
                filme_id=resultado[2],
                data_hora=resultado[3],
                publico=resultado[4],
                id=resultado[0]
            )
            sessoes.append(sessao)

        conn.close()

        return sessoes

    def listar_por_filme(self, filme_id):
        """Lista todas as sessões de um filme"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sessoes WHERE filme_id = ? ORDER BY data_hora", (filme_id,))

        sessoes = []
        for resultado in cursor.fetchall():
            sessao = Sessao(
                cinema_id=resultado[1],
                filme_id=resultado[2],
                data_hora=resultado[3],
                publico=resultado[4],
                id=resultado[0]
            )
            sessoes.append(sessao)

        conn.close()

        return sessoes

    def atualizar(self, sessao):
        """Atualiza uma sessão existente"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE sessoes 
        SET cinema_id = ?, filme_id = ?, data_hora = ?, publico = ?
        WHERE id = ?
        """, (
            sessao.cinema_id,
            sessao.filme_id,
            sessao.data_hora,
            sessao.publico,
            sessao.id
        ))

        conn.commit()
        conn.close()

    def deletar(self, sessao_id):
        """Deleta uma sessão"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM sessoes WHERE id = ?", (sessao_id,))

        conn.commit()
        conn.close()

    def contar_sessoes_por_cinema(self, cinema_id):
        """Conta quantas sessões um cinema possui"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM sessoes WHERE cinema_id = ?", (cinema_id,))
        
        resultado = cursor.fetchone()
        conn.close()

        return resultado[0] if resultado else 0

    def contar_sessoes_por_filme(self, filme_id):
        """Conta quantas sessões um filme possui"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM sessoes WHERE filme_id = ?", (filme_id,))
        
        resultado = cursor.fetchone()
        conn.close()

        return resultado[0] if resultado else 0
