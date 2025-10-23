import sala
import filme
import relatorio
import sessao

def menu():
    # Força uma entrada válida de "escolha"
    escolha = 0
    while escolha > 5 or escolha < 1:
        print("\nMenu principal:")
        print("1- Submenu de Salas")
        print("2- Submenu de Filmes")
        print("3- Submenu de Sessões")
        print("4- Submenu de Relatórios")
        print("5- Sair")
        escolha = int(input("\nEscolha: "))

        if escolha > 5 or escolha < 1:
            print("escolha inválida")
        else:
            return escolha

def main():
    escolha = 0
    # Fica oferecendo as opções até o usuário decidir sair com valor 5
    while escolha != 5:
        escolha = menu()
        
        if escolha == 1:
            sala.main()
        elif escolha == 2:
            filme.main()
        elif escolha == 3:
            sessao.main()
        elif escolha == 4:
            relatorio.main()
main()