import utils

def menu():
    #Força uma entrada válida
    escolha = 0
    while escolha > 6 or escolha < 1:
        print("\nMenu de filmes:")
        print("1- Listar todos os filmes")
        print("2- Exibir detalhes de um filme")
        print("3- Incluir filme ao catálogo")
        print("4- Alterar um filme do catálogo")
        print("5- Excluir filme do catálogo")
        print("6- Sair")

        escolha = int(input("\nEscolha: "))
        if escolha > 6 or escolha < 1:
            print("Opção inexistente (escolha de 1 a 6)!")
        else:
            return escolha

def list_dict(film_dict):# Lista os filmes, ordenados por inclusão no sistema
    for key in film_dict.keys():
        print(f"Código: {key}")
        print(f"\tTítulo: {film_dict[key][0]} // Ano de Lançamento: {film_dict[key][1]}")
        print(f"\tDiretor: {film_dict[key][2]} // Elenco principal: {film_dict[key][3]}\n")

def include_film(film_dict): # Inclui um novo filme no dicionário e registra em arquivo
    # Garante a entrada de um código único
    key = input("Código: ")
    while key in film_dict.keys():
        key = input("Código já em uso, insira outro: ")
    
    # Obtém os atributos do filme
    title = input("Informe o título do filme: ")
    year = input("Informe o ano de lançamento do filme: ")
    director = input("Informe o nome do diretor: ")

    # Obtém os nomes dos atores/atrizes e armazena em uma única string
    actors = []
    actors_length = int(input("Informe quantos atores/atrizes quer incluir no elenco: "))
    i=0
    while i < actors_length:
        i+=1
        actor_name = input(f"Informe o nome do {i}º Ator/Atriz: ")
        if i < actors_length:
            actors.append(actor_name + ", ")
        else:
            actors.append(actor_name)

    # Formata o conteúdo na estrutura do arquivo
    #film = "\n" + key + "/" + title + "/" + year + "/" + director + "/"
    
    #for a in actors
    #    film += a

    # Escreve no arquivo
    #file = open(file_name, "a")
    #file.write(film)
    #file.close()

    # Adiciona ao dicionário a nova chave e seus elementos
    film_dict[key] = [title, year, director, actors]
    list_film(film_dict,key)

def list_film(film_dict, key): # Exibe as informações de um filme
    if key in film_dict:
        print(f"Título: {film_dict[key][0]} // Ano de Lançamento: {film_dict[key][1]}\n\tDiretor: {film_dict[key][2]} // Elenco principal: {film_dict[key][3]}\n")
    else:
        print("Código não encontrado!")

def alterar_filme(film_dict, key, file_name): # Altera uma das informações de um filme
    list_film(film_dict,key)
    continua = 'sim'
    while continua.lower() == 'sim':
        print("\nMenu de alteração de filmes:\n\t1 - Título\n\t2 - Ano de lançamento\n\t3 - Diretor\n\t4 - Elenco")
        opc = int(input("Escolha um para alterar: "))
        while opc < 1 and opc > 4:
            opc = int(input("Opção inválida, escolha de 1 à 4! Escolha um para alterar: "))
        novo_valor = input("Digite o novo valor: ")
        film_dict[key][opc-1] = novo_valor
        continua = input("Alteração efetuada com sucesso, deseja efetuar outra alteração? (Entre com sim ou nao)\n")
        while continua.lower() != 'sim' and continua.lower() != 'nao':
            continua = input("ERRO: Digite apenas sim ou nao, deseja efetuar outra alteração? ")
        #arquivo = open(file_name,'w')
        #for key in film_dict.keys():
        #    arquivo.write(film_dict)
        #arquivo.close
        
def main():
    # Declara e monta o dicionário do filme
    file_name = "filme"
    film_dict = utils.build_dict_through_file(file_name)
    # build_dict(film_dict,file_name)

    # Oferece opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()
        if escolha == 1: # Listar todos os filmes no catálogo
            list_dict(film_dict)

        elif escolha == 2: # Listar um filme específico
            key = input("Informe o código do filme: ")
            while key not in film_dict.keys():
                key = input("Código inexistente! Informe o código do filme que deseja detalhar: ")
            list_film(film_dict, key)

        elif escolha == 3: # Incluir novo filme no catálogo
            include_film(film_dict)

        elif escolha == 4: # Alterar dados de um filme do catálogo (não é possível alterar Chave/Key/Código)
            key = input("Informe o código do filme que deseja alterar: ")
            while key not in film_dict.keys():
                key = input("Código inexistente! Informe o código do filme que deseja alterar: ")
            alterar_filme(film_dict,key,file_name)

        elif escolha == 5: # Excluir um filme do catálogo
            #excluir_filme(film_dict, key)
            print("Função em produção")
        elif escolha == 6:
            utils.save_dict_to_file(file_name, film_dict)
            return