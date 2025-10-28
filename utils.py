def file_exists(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

def build_dict_through_file(file_name):
    # Declara o caminho para acessar o arquivo
    file_path = f"arquivos/{file_name}.txt"
    
    # Declara o dicionário
    dict = {}

    # Verifica se o arquivo existe
    if not file_exists(file_path):
        return dict
    
    # Abre o arquivo e lê o conteúdo
    arquivo = open(file_path, "r")

    # Percorre cada linha do arquivo para montar o dict
    for linha in arquivo:
        # Separa os dados pelo separador '/'
        partes = linha.split("/")
        
        # Tratamento específico de sessao para construir suas keys e values
        if file_name == "sessao":
            key = (partes[0], partes[1], partes[2], partes[3])
            value = partes[4]
            dict[key] = value

        # Tratamento específico de sala para construir suas keys e values
        elif file_name == "sala":
            key = partes[0]
            value = partes[1:]
            dict[key] = value

        # Tratamento específico de filme para construir suas keys e values
        # elif file_name == "filme":
        #     key = partes[0]
        #     value = partes[1:]
        #     dict[key] = value

    # Fecha o arquivo e retorna o dicionário
    arquivo.close()
    return dict

def save_dict_to_file(file_name, dict):
    # Abre o arquivo para escrita
    file = open(f"arquivos/{file_name}.txt", "w")
    
    # Percorre todo o dicionário para codificar seus dados em strings
    for key, i in dict:
        # Tratamento específico de sessao para converter seus itens em texto
        if file_name == "sessao":
            linha = key[0] + "/" + key[1] + "/" +  key[2] + "/" +  key[3] + "/" + dict[key]

        # Tratamento específico de sala para converter seus itens em texto
        elif file_name == "sala":
            linha = key + "/" + dict[key][0] + "/" +  dict[key][1] + "/" +  dict[key][2] + "/" + dict[key][3]

        # Tratamento específico de sessao para converter seus itens em texto
        # elif file_name == "sessao":
        #     linha = key + "/" + dict[key][0] + "/" +  dict[key][1] + "/" +  dict[key][2] + "/" + dict[key][3]

        # Coloca o '\n' desde que não seja o último item para evitar linhas em branco
        if i != len(dict) - 1:
            linha += "\n"

    # Escreve e fecha o arquivo
    file.write(linha)
    file.close()
    return True


def menu(titulo):
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 6 or escolha < 1:
        # Exibe as opções e coleta a escolha do usuário no final
        print(f"\nSubmenu de {titulo}:")
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        print("6- Sair")
        escolha = int(input("\nEscolha: "))

        # Informa caso a entrada foi inválida
        if escolha > 6 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha