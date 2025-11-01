import utils
import dict_utils

def include(film_dict):
    # Garante uma key que não existe neste módulo
    key = dict_utils.ensure_key_dont_exists_in_dict(film_dict)
    
    # Obtém os atributos do filme
    title = input("Informe o título do filme: ").upper()
    year = str(utils.valid_int(input_message="Informe o ano de lançamento do filme: "))
    director = input("Informe o nome do diretor: ").upper()

    # Obtém os nomes dos atores/atrizes e armazena em lista de str
    actors = []
    actors_length = utils.valid_int(input_message="Informe quantos atores/atrizes quer incluir no elenco: ")
    for i in range(actors_length):
        actor_name = input(f"Informe o nome do {i+1}º Ator/Atriz: ").upper()
        actors.append(actor_name)

    # Adiciona a nova key e seus elementos ao dicionário
    film_dict[key] = [title, year, director, actors]
    return True

def list_dict(film_dict):
    # Confere se a lista está vazia
    if len(film_dict) == 0:
        return False

    for key in film_dict.keys():
        print(f"Código: {key}")
        list_element(film_dict, key)
        print()
    return True

# Exibe as informações de um filme
def list_element(film_dict, key):
    # Confere se a lista está vazia
    if len(film_dict) == 0:
        return False

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
        return True
    else:
        print("Código não encontrado!")
        return False

# Altera uma das informações de um filme
def edit(film_dict):
    # Confere se a lista está vazia
    if len(film_dict) == 0:
        return False

    # Garante uma key existente neste módulo
    key = dict_utils.ensure_key_exists_in_dict(film_dict)

    # Exibe as opções que podem ser trocadas da key escolhida pela posicao
    print(f"\nQual dado deseja mudar?\n\t1- Título: {film_dict[key][0]} // 2- Lançamento: {film_dict[key][1]}")
    print(f"\t3- Diretor: {film_dict[key][2]} // 4- Elenco: {', '.join(film_dict[key][3])}")
    option = utils.valid_int(input_message="Escolha: ")
    
    # Força entrada válida
    while option < 1 and option > 4:
        option = utils.valid_int(input_message="Escolha: ")
        if option < 1 and option > 4:
            print("\nPosição inválida, escolha de 1 a 4!")
    
    # Se opção for atores, cria lista com atores
    if option == 4:
        new = []
        actors_length = utils.valid_int(input_message="Informe quantos atores/atrizes quer incluir no elenco: ")
        for i in range(actors_length):
            actor_name = input(f"Informe o nome do {i+1}º Ator/Atriz: ").upper()
            new.append(actor_name)
    
    # Se opção for ano de lançamento, força entrada em inteiros
    if option == 2:
        new = utils.valid_int(input_message="Informe o novo valor: ")
    
    # Se opção for Título ou Diretor, preenche com texto
    if option == 1 or option == 3:
        new = input("Informe o novo valor: ")
    
    return dict_utils.change_dict(film_dict, key, option-1, new)

def delete(film_dict):
    # Confere se a lista está vazia
    if len(film_dict) == 0:
        return False

    # Garante uma key existente neste módulo
    key = dict_utils.ensure_key_exists_in_dict(film_dict)

    # Deleta o item com aquela key do dicionário a partir dos dados coletados
    return dict_utils.delete_element_in_dict(film_dict, key)
    
def main():
    # Declara e monta o dicionário do filme
    module = "filme"
    film_dict = dict_utils.build_dict_from_file(module)

    # Oferece opções até o usuário decidir sair (6)
    option = 0
    while option != 6:
        option = utils.menu(module)
        if option == 1:  # Listar todos os filmes no catálogo
            if not list_dict(film_dict):
                print("Lista vazia!")

        elif option == 2:  # Listar um filme específico
            # Confere se a lista está vazia
            if len(film_dict) == 0:
                print("Lista vazia!")
            else:
                # Garante uma key existente neste módulo
                key = dict_utils.ensure_key_exists_in_dict(film_dict)
                list_element(film_dict, key)

        elif option == 3:  # Incluir novo filme no catálogo
            include(film_dict)

        elif option == 4:  # Alterar dados de um filme do catálogo (não é possível alterar Chave/Key/Código)
            if not edit(film_dict):
                print("Operação cancelada ou lista vazia!")
            else:
                print("Operação bem sucedida!")

        elif option == 5:  # Excluir um filme do catálogo
            if not delete(film_dict):
                print("Operação cancelada ou lista vazia!")
            else:
                print("Operação bem sucedida!")

        elif option == 6:
            dict_utils.save_dict_in_file(module,film_dict)
            return