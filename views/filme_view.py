from controllers.filme_controller import FilmeController

controller = FilmeController()

def menu_filmes():
    while True:
        print("\n" + "="*50)
        print("GERENCIAR FILMES".center(50))
        print("="*50)
        print("\n1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Atualizar Filme")
        print("4 - Deletar Filme")
        print("0 - Voltar")
        print("\n" + "-"*50)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            try:
                print("\n--- CADASTRO DE FILME ---")
                titulo = input("Título: ").strip()
                duracao = int(input("Duração (minutos): "))
                genero = input("Gênero: ").strip()
                diretor = input("Diretor: ").strip()
                elenco = input("Elenco: ").strip()

                controller.cadastrar(titulo, duracao, genero, diretor, elenco)
                print("\n✓ Filme cadastrado com sucesso!")
            except ValueError as e:
                print(f"\nErro: {e}")
            except Exception as e:
                print(f"\nErro ao cadastrar: {e}")

        elif opcao == "2":
            try:
                filmes = controller.listar()
                if not filmes:
                    print("\nNenhum filme cadastrado!")
                else:
                    print("\n" + "-"*50)
                    print("FILMES CADASTRADOS".center(50))
                    print("-"*50)
                    for filme in filmes:
                        print(f"\nID: {filme.id}")
                        print(f"  Título: {filme.titulo}")
                        print(f"  Duração: {filme.duracao} minutos")
                        print(f"  Gênero: {filme.genero}")
                        print(f"  Diretor: {filme.diretor}")
                        print(f"  Elenco: {filme.elenco}")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "3":
            try:
                filme_id = int(input("\nID do filme a atualizar: "))
                filme = controller.obter(filme_id)
                if not filme:
                    print("\nFilme não encontrado!")
                else:
                    print("\n--- ATUALIZAR FILME ---")
                    titulo = input(f"Título ({filme.titulo}): ").strip() or filme.titulo
                    duracao = input(f"Duração ({filme.duracao}): ").strip()
                    duracao = int(duracao) if duracao else filme.duracao
                    genero = input(f"Gênero ({filme.genero}): ").strip() or filme.genero
                    diretor = input(f"Diretor ({filme.diretor}): ").strip() or filme.diretor
                    elenco = input(f"Elenco ({filme.elenco}): ").strip() or filme.elenco

                    controller.atualizar(filme_id, titulo, duracao, genero, diretor, elenco)
                    print("\n✓ Filme atualizado com sucesso!")
            except ValueError:
                print("\nID ou duração inválido!")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "4":
            try:
                filme_id = int(input("\nID do filme a deletar: "))
                controller.deletar(filme_id)
                print("\n✓ Filme deletado com sucesso!")
            except ValueError:
                print("\nID inválido!")
            except ValueError as e:
                print(f"\n✗ {e}")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!")