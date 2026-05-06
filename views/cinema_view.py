from controllers.cinema_controller import CinemaController

controller = CinemaController()

def menu_cinemas():
    while True:
        print("\n" + "="*50)
        print("GERENCIAR CINEMAS".center(50))
        print("="*50)
        print("\n1 - Cadastrar Cinema")
        print("2 - Listar Cinemas")
        print("3 - Atualizar Cinema")
        print("4 - Deletar Cinema")
        print("0 - Voltar")
        print("\n" + "-"*50)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            try:
                print("\n--- CADASTRO DE CINEMA ---")
                nome = input("Nome: ").strip()
                cidade = input("Cidade: ").strip()
                estado = input("Estado (sigla): ").strip()
                endereco = input("Endereço: ").strip()
                capacidade = int(input("Capacidade de público: "))

                controller.cadastrar(nome, cidade, estado, endereco, capacidade)
                print("\n✓ Cinema cadastrado com sucesso!")
            except ValueError:
                print("\nCapacidade deve ser um número!")
            except Exception as e:
                print(f"\nErro ao cadastrar: {e}")

        elif opcao == "2":
            try:
                cinemas = controller.listar()
                if not cinemas:
                    print("\nNenhum cinema cadastrado!")
                else:
                    print("\n" + "-"*50)
                    print("CINEMAS CADASTRADOS".center(50))
                    print("-"*50)
                    for cinema in cinemas:
                        print(f"\nID: {cinema.id}")
                        print(f"  Nome: {cinema.nome}")
                        print(f"  Localização: {cinema.cidade}, {cinema.estado}")
                        print(f"  Endereço: {cinema.endereco}")
                        print(f"  Capacidade: {cinema.capacidade} pessoas")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "3":
            try:
                cinema_id = int(input("\nID do cinema a atualizar: "))
                cinema = controller.obter(cinema_id)
                if not cinema:
                    print("\nCinema não encontrado!")
                else:
                    print("\n--- ATUALIZAR CINEMA ---")
                    nome = input(f"Nome ({cinema.nome}): ").strip() or cinema.nome
                    cidade = input(f"Cidade ({cinema.cidade}): ").strip() or cinema.cidade
                    estado = input(f"Estado ({cinema.estado}): ").strip() or cinema.estado
                    endereco = input(f"Endereço ({cinema.endereco}): ").strip() or cinema.endereco
                    capacidade = input(f"Capacidade ({cinema.capacidade}): ").strip()
                    capacidade = int(capacidade) if capacidade else cinema.capacidade

                    controller.atualizar(cinema_id, nome, cidade, estado, endereco, capacidade)
                    print("\n✓ Cinema atualizado com sucesso!")
            except ValueError:
                print("\nID ou capacidade inválido!")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "4":
            try:
                cinema_id = int(input("\nID do cinema a deletar: "))
                controller.deletar(cinema_id)
                print("\n✓ Cinema deletado com sucesso!")
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
