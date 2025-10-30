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
        partes = linha.replace("\n","").split("/")

        # Tratamento específico de sessao para construir suas keys e values
        if file_name == "sessao":
            key = (partes[0], partes[1], partes[2], partes[3])
            value = partes[4]

        # Tratamento específico de sala para construir suas keys e values
        elif file_name == "sala":
            key = partes[0]
            value = partes[1:]

        # Tratamento específico de filme para construir suas keys e values
        elif file_name == "filme":
            key = partes[0]
            partes[4] = value[partes[4]].split(", ") # É pra ser uma lista de atores
            value = partes[1:]

        # Coloca na estrutura de dicionários
        dict[key] = value
        
    # Fecha o arquivo e retorna o dicionário
    arquivo.close()
    return dict

def save_dict_to_file(file_name, dict):
    # Abre o arquivo para escrita
    file = open(f"arquivos/{file_name}.txt", "w")
    
    # Percorre todo o dicionário para codificar seus dados em strings no loop de contador e chave
    for i, key in enumerate(dict):
        # Converte os itens de sessao para texto no formato correto 
        if file_name == "sessao":
            linha = f"{"/".join(key)}/{dict[key]}"

        # Converte os itens de sala para texto no formato correto 
        elif file_name == "sala":
            linha = f"{key}/{"/".join(dict[key])}" 

        # Converte os itens de filme para texto no formato correto
        elif file_name == "filme":
            dict[key][3] = ", ".join(dict[key][3])
            linha = f"{key}/{"/".join(dict[key])}"

        # Coloca o '\n' desde que não seja o último item para evitar linhas em branco
        if i != len(dict) - 1:
            linha += "\n"

        # Escreve a linha no arquivo
        file.write(linha)
    
    # fecha o arquivo e retorna
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
        
        # Permite o usuário escolher e valida
        escolha = int(input("\nEscolha: "))
        if escolha > 6 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha

def valid_int():
    # Loop em que só é possivel sair ao entra um inteiro válido
    while True:
        # Se a conversão para inteiro for bem sucedida, retorna
        try:
            return int(input(": "))
        
        # Se deu erro, informa!
        except:
            print("valor deve ser um inteiro!")

def valid_date():
    # Importa biblioteca para lidar com datas
    from datetime import date

    # Loop em que só é possivel sair ao entra um date válido
    while True:
        # Se a conversão para date for bem sucedida, retorna
        try:
            values = input(": ").split("-")
            return date(int(values[2]), int(values[1]), int(values[0]))

         # Se deu erro, informa! 
        except:
            print("valor deve ser uma data válida (DD-MM-AAAA)")
    
        