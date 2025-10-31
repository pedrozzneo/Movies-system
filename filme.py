import utils
import dict_utils

def ensure_key_exists_in_filme_dict(film_dict):
    # Loop que garante a entrada de uma key existente (filme)
    key = None
    while key not in film_dict:
        key = input("Código: ").upper()
        if key not in film_dict:
            print("Chave não encontrada!")
    return key

def ensure_key_dont_exists_in_filme_dict(film_dict):
    # Loop que garante a entrada de uma key que não existe (filme)
    key = input("Código: ").upper()
    while key in film_dict:
        # Avisa que a key é repetida
        print("Chave já em uso!")
        
        # Coleta uma nova key
        key = input("Código: ").upper()
    return key

def include_film(film_dict): # Inclui um novo filme no dicionário e registra em arquivo
    # Garante uma key que não existe neste módulo
    key = ensure_key_dont_exists_in_filme_dict(film_dict)
    
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

def edit_film(film_dict): # Altera uma das informações de um filme
    # Recebe a key código
    key = input("Código: ").upper()
    
    # Retorna caso essa key não exista no dicionário
    if key not in film_dict:
        return "NO_DATA"

    # Exibe as opções que podem ser trocadas da key escolhida pela posicao
    print(f"\nQual dado deseja mudar?\n\t1- Título: {film_dict[key][0]} // 2- Lançamento: {film_dict[key][1]}")
    print(f"\t3- Diretor: {film_dict[key][2]} // 4- Elenco: {','.join(film_dict[key][3])}")
    opcao = utils.valid_int(input_message="Escolha: ")
    # Força entrada válida
    while opcao < 1 and opcao > 4:
        opcao = utils.valid_int(input_message="Escolha: ")
        if opcao < 1 and opcao > 4:
            print("\nPosição inválida, escolha de 1 a 4!")
    # Se opção for atores, cria lista com atores
    if opcao == 4:
        new = []
        actors_length = utils.valid_int(input_message="Informe quantos atores/atrizes quer incluir no elenco: ")
        for i in range(actors_length):
            actor_name = input(f"Informe o nome do {i+1}º Ator/Atriz: ").upper()
            new.append(actor_name)
    # Se opção for ano de lançamento, força entrada em inteiros
    if opcao == 2:
        new = utils.valid_int(input_message="Informe o novo valor: ")
    # Se opção for Título ou Diretor, preenche com texto
    if opcao == 1 or opcao == 3:
        new = input("Informe o novo valor: ")
    dict_utils.change_dict(film_dict,key,opcao-1,new)
    
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
            # Garante uma key existente neste módulo
            key = ensure_key_exists_in_filme_dict(film_dict)
            list_film(film_dict, key)

        elif escolha == 3: # Incluir novo filme no catálogo
            include_film(film_dict)

        elif escolha == 4: # Alterar dados de um filme do catálogo (não é possível alterar Chave/Key/Código)
            # Garante uma key existente neste módulo
            key = ensure_key_exists_in_filme_dict(film_dict)
            alterar_filme(film_dict,key)

        elif escolha == 5: # Excluir um filme do catálogo
            # Garante uma key existente neste módulo
            key = ensure_key_exists_in_filme_dict(film_dict)
            
            # Deleta o item com aquela key do dicionário a partir dos dados coletados
            if not dict_utils.delete_element_in_dict(film_dict, key):
                print("Operação cancelada!")
            else:
                print("Operação bem sucedida!")

        elif escolha == 6:
            dict_utils.save_dict_in_file(module,film_dict)
            return