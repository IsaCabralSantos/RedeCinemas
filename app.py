from repository.filme_repository import FilmeRepository
from repository.cinema_repository import CinemaRepository
from repository.sessao_repository import SessaoRepository
from views.filme_view import menu_filmes
from views.cinema_view import menu_cinemas
from views.sessao_view import menu_sessoes

# Inicializar tabelas
filme_repo = FilmeRepository()
cinema_repo = CinemaRepository()
sessao_repo = SessaoRepository()

filme_repo.criar_tabela()
cinema_repo.criar_tabela()
sessao_repo.criar_tabela()

def menu_principal():
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE REDE DE CINEMAS".center(50))
        print("="*50)
        print("\n1 - Gerenciar Cinemas")
        print("2 - Gerenciar Filmes")
        print("3 - Gerenciar Sessões")
        print("4 - Relatórios")
        print("0 - Sair")
        print("\n" + "-"*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_cinemas()
        elif opcao == "2":
            menu_filmes()
        elif opcao == "3":
            menu_sessoes()
        elif opcao == "4":
            relatorios()
        elif opcao == "0":
            print("\nObrigado por usar o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida!")

def relatorios():
    from controllers.cinema_controller import CinemaController
    from controllers.filme_controller import FilmeController
    from controllers.sessao_controller import SessaoController
    
    cinema_ctrl = CinemaController()
    filme_ctrl = FilmeController()
    sessao_ctrl = SessaoController()
    
    while True:
        print("\n" + "="*50)
        print("RELATÓRIOS".center(50))
        print("="*50)
        print("\n1 - Público por Sessão")
        print("2 - Público Total por Filme")
        print("3 - Público Total por Cinema")
        print("4 - Ocupação por Sessão")
        print("0 - Voltar")
        print("\n" + "-"*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                sessoes = sessao_ctrl.listar()
                if not sessoes:
                    print("\nNenhuma sessão cadastrada!")
                else:
                    print("\n" + "-"*50)
                    print("PÚBLICO POR SESSÃO".center(50))
                    print("-"*50)
                    for sessao in sessoes:
                        cinema = cinema_ctrl.obter(sessao.cinema_id)
                        filme = filme_ctrl.obter(sessao.filme_id)
                        print(f"\nSessão {sessao.id}:")
                        print(f"  Cinema: {cinema.nome if cinema else 'N/A'}")
                        print(f"  Filme: {filme.titulo if filme else 'N/A'}")
                        print(f"  Data/Hora: {sessao.data_hora}")
                        print(f"  Público: {sessao.publico}")
            except Exception as e:
                print(f"\nErro: {e}")
        
        elif opcao == "2":
            try:
                filmes = filme_ctrl.listar()
                if not filmes:
                    print("\nNenhum filme cadastrado!")
                else:
                    print("\n" + "-"*50)
                    print("PÚBLICO TOTAL POR FILME".center(50))
                    print("-"*50)
                    for filme in filmes:
                        publico_total = filme_ctrl.obter_publico_total(filme.id)
                        print(f"\n{filme.titulo}: {publico_total} espectadores")
            except Exception as e:
                print(f"\nErro: {e}")
        
        elif opcao == "3":
            try:
                cinemas = cinema_ctrl.listar()
                if not cinemas:
                    print("\nNenhum cinema cadastrado!")
                else:
                    print("\n" + "-"*50)
                    print("PÚBLICO TOTAL POR CINEMA".center(50))
                    print("-"*50)
                    for cinema in cinemas:
                        publico_total = cinema_ctrl.obter_publico_total(cinema.id)
                        print(f"\n{cinema.nome}: {publico_total} espectadores")
            except Exception as e:
                print(f"\nErro: {e}")
        
        elif opcao == "4":
            try:
                sessoes = sessao_ctrl.listar()
                if not sessoes:
                    print("\nNenhuma sessão cadastrada!")
                else:
                    print("\n" + "-"*50)
                    print("OCUPAÇÃO POR SESSÃO".center(50))
                    print("-"*50)
                    for sessao in sessoes:
                        ocupacao = sessao_ctrl.obter_ocupacao(sessao.id)
                        cinema = cinema_ctrl.obter(sessao.cinema_id)
                        filme = filme_ctrl.obter(sessao.filme_id)
                        print(f"\nSessão {sessao.id}:")
                        print(f"  Cinema: {cinema.nome if cinema else 'N/A'}")
                        print(f"  Filme: {filme.titulo if filme else 'N/A'}")
                        print(f"  Ocupação: {ocupacao:.1f}%")
            except Exception as e:
                print(f"\nErro: {e}")
        
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    menu_principal()