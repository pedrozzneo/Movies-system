import sala
import filme
import relatorio
import sessao
import utils

def menu():
    # Força uma entrada válida de "escolha"
    option = 0
    while option > 5 or option < 1:
        # Exibe as opções para receber a escolha
        print("\nMenu principal:")
        print("1- Submenu de Salas")
        print("2- Submenu de Filmes")
        print("3- Submenu de Sessões")
        print("4- Submenu de Relatórios")
        print("5- Sair")
        
        option = utils.valid_int(input_message="\nEscolha: ")
        # Trata a escolha do usuário
        if option > 5 or option < 1:
            print("escolha inválida")
        else:
            return option

def main():
    option = 0
    # Fica oferecendo as opções até o usuário decidir sair com valor 5
    while option != 5:
        # Exibe o menu e coleta a escolha do usuário
        option = menu()

        # Atribui a escolha do usuário a uma função
        if option == 1:
            sala.main()
        elif option == 2:
            filme.main()
        elif option == 3:
            sessao.main()
        elif option == 4:
            relatorio.main()
        elif option == 5:
            print("saindo...")
main()