from controllers.sessao_controller import SessaoController
from controllers.cinema_controller import CinemaController
from controllers.filme_controller import FilmeController

sessao_ctrl = SessaoController()
cinema_ctrl = CinemaController()
filme_ctrl = FilmeController()

def menu_sessoes():
    while True:
        print("\n" + "="*50)
        print("GERENCIAR SESSÕES".center(50))
        print("="*50)
        print("\n1 - Cadastrar Sessão")
        print("2 - Listar Sessões")
        print("3 - Registrar Público")
        print("4 - Atualizar Sessão")
        print("5 - Deletar Sessão")
        print("0 - Voltar")
        print("\n" + "-"*50)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            try:
                print("\n--- CADASTRO DE SESSÃO ---")
                
                # Listar cinemas
                cinemas = cinema_ctrl.listar()
                if not cinemas:
                    print("Nenhum cinema cadastrado!")
                    continue
                
                print("\nCinemas disponíveis:")
                for cinema in cinemas:
                    print(f"  {cinema.id} - {cinema.nome} (Cap: {cinema.capacidade})")
                
                cinema_id = int(input("ID do cinema: "))
                
                # Listar filmes
                filmes = filme_ctrl.listar()
                if not filmes:
                    print("Nenhum filme cadastrado!")
                    continue
                
                print("\nFilmes disponíveis:")
                for filme in filmes:
                    print(f"  {filme.id} - {filme.titulo} ({filme.duracao}min)")
                
                filme_id = int(input("ID do filme: "))
                data_hora = input("Data e hora (YYYY-MM-DD HH:MM): ").strip()

                sessao_ctrl.cadastrar(cinema_id, filme_id, data_hora)
                print("\n✓ Sessão cadastrada com sucesso!")
            except ValueError as e:
                print(f"\nErro: {e}")
            except Exception as e:
                print(f"\nErro ao cadastrar: {e}")

        elif opcao == "2":
            try:
                sessoes = sessao_ctrl.listar()
                if not sessoes:
                    print("\nNenhuma sessão cadastrada!")
                else:
                    print("\n" + "-"*50)
                    print("SESSÕES CADASTRADAS".center(50))
                    print("-"*50)
                    for sessao in sessoes:
                        cinema = cinema_ctrl.obter(sessao.cinema_id)
                        filme = filme_ctrl.obter(sessao.filme_id)
                        print(f"\nSessão {sessao.id}:")
                        print(f"  Cinema: {cinema.nome if cinema else 'N/A'}")
                        print(f"  Filme: {filme.titulo if filme else 'N/A'}")
                        print(f"  Data/Hora: {sessao.data_hora}")
                        print(f"  Público: {sessao.publico}")
                        ocupacao = sessao_ctrl.obter_ocupacao(sessao.id)
                        print(f"  Ocupação: {ocupacao:.1f}%")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "3":
            try:
                sessao_id = int(input("\nID da sessão: "))
                publico = int(input("Quantidade de público: "))
                sessao_ctrl.registrar_publico(sessao_id, publico)
                print("\n✓ Público registrado com sucesso!")
            except ValueError:
                print("\nID ou público inválido!")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "4":
            try:
                sessao_id = int(input("\nID da sessão a atualizar: "))
                sessao = sessao_ctrl.obter(sessao_id)
                if not sessao:
                    print("\nSessão não encontrada!")
                else:
                    cinema = cinema_ctrl.obter(sessao.cinema_id)
                    filme = filme_ctrl.obter(sessao.filme_id)
                    
                    print("\n--- ATUALIZAR SESSÃO ---")
                    print(f"Cinema atual: {cinema.nome if cinema else 'N/A'}")
                    print(f"Filme atual: {filme.titulo if filme else 'N/A'}")
                    print(f"Data/Hora atual: {sessao.data_hora}")
                    
                    cinema_id = input("Novo cinema (Enter para manter): ").strip()
                    cinema_id = int(cinema_id) if cinema_id else sessao.cinema_id
                    
                    filme_id = input("Novo filme (Enter para manter): ").strip()
                    filme_id = int(filme_id) if filme_id else sessao.filme_id
                    
                    data_hora = input("Nova data e hora (Enter para manter): ").strip()
                    data_hora = data_hora if data_hora else sessao.data_hora
                    
                    publico = input("Novo público (Enter para manter): ").strip()
                    publico = int(publico) if publico else sessao.publico

                    sessao_ctrl.atualizar(sessao_id, cinema_id, filme_id, data_hora, publico)
                    print("\n✓ Sessão atualizada com sucesso!")
            except ValueError as e:
                print(f"\nErro: {e}")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "5":
            try:
                sessao_id = int(input("\nID da sessão a deletar: "))
                sessao_ctrl.deletar(sessao_id)
                print("\n✓ Sessão deletada com sucesso!")
            except ValueError:
                print("\nID inválido!")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!")
