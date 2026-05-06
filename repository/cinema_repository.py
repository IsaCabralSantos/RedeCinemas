from database import conectar
from models.cinema import Cinema

class CinemaRepository:

    def criar_tabela(self):
        """Cria a tabela de cinemas se não existir"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            endereco TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        )
        """)

        conn.commit()
        conn.close()

    def salvar(self, cinema):
        """Insere um novo cinema no banco"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO cinemas (nome, cidade, estado, endereco, capacidade)
        VALUES (?, ?, ?, ?, ?)
        """, (
            cinema.nome,
            cinema.cidade,
            cinema.estado,
            cinema.endereco,
            cinema.capacidade
        ))

        conn.commit()
        conn.close()

    def obter_por_id(self, cinema_id):
        """Obtém um cinema pelo ID"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM cinemas WHERE id = ?", (cinema_id,))
        
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return Cinema(
                nome=resultado[1],
                cidade=resultado[2],
                estado=resultado[3],
                endereco=resultado[4],
                capacidade=resultado[5],
                id=resultado[0]
            )
        return None

    def listar(self):
        """Lista todos os cinemas"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM cinemas")

        cinemas = []
        for resultado in cursor.fetchall():
            cinema = Cinema(
                nome=resultado[1],
                cidade=resultado[2],
                estado=resultado[3],
                endereco=resultado[4],
                capacidade=resultado[5],
                id=resultado[0]
            )
            cinemas.append(cinema)

        conn.close()

        return cinemas

    def atualizar(self, cinema):
        """Atualiza um cinema existente"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE cinemas 
        SET nome = ?, cidade = ?, estado = ?, endereco = ?, capacidade = ?
        WHERE id = ?
        """, (
            cinema.nome,
            cinema.cidade,
            cinema.estado,
            cinema.endereco,
            cinema.capacidade,
            cinema.id
        ))

        conn.commit()
        conn.close()

    def deletar(self, cinema_id):
        """Deleta um cinema"""
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM cinemas WHERE id = ?", (cinema_id,))

        conn.commit()
        conn.close()
