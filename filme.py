import utils
import dict_utils

def include_film(film_dict): # Inclui um novo filme no dicionário e registra em arquivo
    # Garante a entrada de um código único
    key = input("Código: ").upper()
    while key in film_dict.keys():
        key = input("Código já em uso, insira outro: ").upper()
    
    # Obtém os atributos do filme
    title = input("Informe o título do filme: ").upper()
    print("Informe o ano de lançamento do filme", end="")
    year = str(utils.valid_int())
    director = input("Informe o nome do diretor: ").upper()

    # Obtém os nomes dos atores/atrizes e armazena em lista de str
    actors = []
    print("Informe quantos atores/atrizes quer incluir no elenco", end="")
    actors_length = utils.valid_int()
    i=0
    while i < actors_length:
        i+=1
        actor_name = input(f"Informe o nome do {i}º Ator/Atriz: ").upper()
        actors.append(actor_name)

    # Adiciona ao dicionário a nova chave e seus elementos
    film_dict[key] = [title, year, director, actors]
    list_film(film_dict,key)

def list_dict(film_dict):# Lista os filmes, ordenados por inclusão no sistema
    for key in film_dict.keys():
        print(key)
        print(f"\tTítulo: {film_dict[key][0]} // Ano de Lançamento: {film_dict[key][1]}")
        print(f"\tDiretor: {film_dict[key][2]}\n\tElenco: ", end="")
        i=0
        while i < len(film_dict[key][3]):
            i+=1
            if i == len(film_dict[key][3]): # Se for último troca ", " por "."
                print(f"{film_dict[key][3][i-1]}", end=".\n")
            else:
                print(f"{film_dict[key][3][i-1]}", end=", ")
        print()

def list_film(film_dict, key): # Exibe as informações de um filme
    if key in film_dict:
        print(f"\tTítulo: {film_dict[key][0]} // Ano de Lançamento: {film_dict[key][1]}")
        print(f"\tDiretor: {film_dict[key][2]}\n\tElenco: ", end="")
        i=0
        while i < len(film_dict[key][3]):
            i+=1
            if i == len(film_dict[key][3]): # Se for último troca ", " por "."
                print(f"{film_dict[key][3][i-1]}", end=".\n")
            else:
                print(f"{film_dict[key][3][i-1]}", end=", ")
    else:
        print("Código não encontrado!")

def alterar_filme(film_dict, key): # Altera uma das informações de um filme
    list_film(film_dict,key)
    continua = 'SIM'
    while continua == 'SIM':
        print("\nMenu de alteração de filmes:\n\t1 - Título\n\t2 - Ano de lançamento\n\t3 - Diretor\n\t4 - Elenco")
        print("Escolha um para alterar", end="")
        opc = utils.valid_int()
        while opc < 1 and opc > 4:
            print("Opção inválida, escolha de 1 à 4! Escolha um para alterar", end="")
            opc = utils.valid_int()
        if opc == 4: # Se for atores/atrizes preenche nova lista
            actors = []
            print("Informe quantos atores/atrizes quer incluir no elenco", end="") 
            actors_length = utils.valid_int()
            i=0
            while i < actors_length:
                i+=1
                actor_name = input(f"Informe o nome do {i}º Ator/Atriz: ").upper()
                if i < actors_length:
                    actors.append(actor_name)
                else:
                    actors.append(actor_name)
            film_dict[key][3] = actors
        else:
            if opc == 1 or opc == 3: # Se for Título ou Diretor entra como .upper()
                new_value = input("Digite o novo valor: ")
                new_value = new_value.upper()
            else: # Se for ano, entra como inteiro (evita letras), depois converte para string.
                print("Digite o novo valor: ", end="")
                new_value = str(utils.valid_int())
            film_dict[key][opc-1] = new_value
        continua = input("Alteração efetuada com sucesso, deseja efetuar outra alteração? (Entre com SIM ou NAO)\n").upper()
        while continua != 'SIM' and continua != 'NAO':
            continua = input("ERRO: Digite apenas SIM ou NAO, deseja efetuar outra alteração? ").upper()

def main():
    # Declara e monta o dicionário do filme
    module = "filme"
    film_dict = dict_utils.build_dict_from_file(module)

    # Oferece opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = utils.menu(module)
        if escolha == 1: # Listar todos os filmes no catálogo
            list_dict(film_dict)

        elif escolha == 2: # Listar um filme específico
            key = input("Informe o código do filme que deseja detalhar: ").upper()
            while key not in film_dict.keys():
                key = input("Código inexistente! Informe um código existente: ").upper()
            list_film(film_dict, key)

        elif escolha == 3: # Incluir novo filme no catálogo
            include_film(film_dict)

        elif escolha == 4: # Alterar dados de um filme do catálogo (não é possível alterar Chave/Key/Código)
            key = input("Informe o código do filme que deseja alterar: ").upper()
            while key not in film_dict.keys():
                key = input("Código inexistente! Informe o código do filme que deseja alterar: ").upper()
            alterar_filme(film_dict,key)

        elif escolha == 5: # Excluir um filme do catálogo
            utils.turn_code_into_message(module,dict_utils.delete_element_in_dict(film_dict))

        elif escolha == 6:
            dict_utils.save_dict_in_file(module,film_dict)
            return