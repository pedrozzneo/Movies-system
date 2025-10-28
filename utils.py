def file_exists(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

def build_dict_through_file(file_name):
    # Declara o caminho para acessar o arquivo
    file_path = f"arquivos/{file_name}.txt"
    
    # Verifica se o arquivo existe
    if not file_exists(file_path):
        print(f"Arquivo {file_path} não encontrado. Dados vazios serão usados.")
        return {}
    
    # Abre o arquivo e lê o conteúdo
    arquivo = open(file_path, "r")

    # Monta o dicionário a partir do arquivo
    dict = {}
    for linha in arquivo:
        # Separa os dados pelo separador '/'
        partes = linha.split("/")
        
        # Tratamento específico do sessao
        if file_name == "sessao":
            # Constrói a key e o value para colocar no dict
            key = (partes[0], partes[1], partes[2], partes[3])
            value = partes[4]
            dict[key] = value

        # Tratamento específico de sala
        elif file_name == "sala":
            key = partes[0]
            value = partes[1:]
            dict[key] = value

        # Tratamento específico de filme
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
    
    # Tratamento específico do sessao
    if file_name == "sessao":
        # Escreve cada linha diretamente no arquivo
        for key in dict:
            # Converte key e value para texto separados por "/"
            linha = key[0] + "/" key[1] + "/" +  key[2] + "/" +  key[3] + "/" + dict[key]
            dict[key] = value

    # Os outros seguem o mesmo padrão
    else:
        key = partes[0]
        value = partes[1:]
        dict[key] = value
    
    # Fecha o arquivo
    file.close()
    return True


def menu(titulo):
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 6 or escolha < 1:
        print(f"\nSubmenu de {titulo}:")
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        print("6- Sair")
        escolha = int(input("\nEscolha: "))

        if escolha > 6 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha