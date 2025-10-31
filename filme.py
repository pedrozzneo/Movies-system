import utils
import dict as dict_utils

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
    print("Escolha", end='')
    opcao = utils.valid_int()
    # Força entrada válida
    while opcao < 1 and opcao > 4:
        print("Escolha", end='')
        opcao = utils.valid_int()
        if opcao < 1 and opcao > 4:
            print("\nPosição inválida, escolha de 1 a 4!")
    # Se opção for atores, cria lista com atores
    if opcao == 4:
        new = []
        print("Informe quantos atores/atrizes quer incluir no elenco", end="")
        actors_length = utils.valid_int()
        for i in range(actors_length):
            actor_name = input(f"Informe o nome do {i+1}º Ator/Atriz: ").upper()
            new.append(actor_name)
    # Se opção for ano de lançamento, força entrada em inteiros
    if opcao == 2:
        print("Informe o novo valor", end='')
        new = utils.valid_int()
    # Se opção for Título ou Diretor, preenche com texto
    if opcao == 1 or opcao == 3:
        new = input("Informe o novo valor: ")
    dict_utils.change_dict(film_dict,key,opcao-1,new)
    
def main():
    # Declara e monta o dicionário do filme
    module = "filme"
    film_dict = dict_utils.build_dict_through_file(module)

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
            utils.status(module,edit_film(film_dict))

        elif escolha == 5: # Excluir um filme do catálogo
            utils.status(module,dict_utils.delete_element_in_dict(film_dict,key))

        elif escolha == 6:
            dict_utils.save_dict_to_file(module,film_dict)
            return