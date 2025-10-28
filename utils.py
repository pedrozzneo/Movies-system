def build_dict_through_file(file_name):
    # Declara o caminho para acessar o arquivo
    file_path = f"arquivos/{file_name}.txt"
    
    # Verifica se o arquivo existe
    import os
    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado. Dados vazios serão usados.")
        return {}
    
    # Abre o arquivo e lê o conteúdo
    arquivo = open(file_path, "r")

    # Monta o dicionário a partir do arquivo
    data_dict = {}
    for linha in arquivo:
        partes = linha.strip().split("/")
        if not partes or partes == ['']:
            continue
        if file_name == "sessao":
            if len(partes) < 5:
                # Linha inválida para sessao; ignora
                continue
            key = (partes[0], partes[1], partes[2], partes[3])
            resto = partes[4:]
            value = resto[0] if len(resto) == 1 else resto
            data_dict[key] = value
        else:
            key = partes[0]
            value = partes[1:]
            data_dict[key] = value

    # Fecha o arquivo e retorna o dicionário
    arquivo.close()
    return data_dict

def save_dict_to_file(file_path, data_dict):
    # Abre o arquivo para escrita
    file = open(file_path, "w")
    
    # Escreve cada linha diretamente no arquivo
    first_line_written = False
    for key in data_dict:
        if isinstance(key, tuple):
            # Sessao: chave com 4 partes
            value = data_dict[key]
            if isinstance(value, list):
                partes = list(key) + value
            else:
                partes = list(key) + [value]
            linha = "/".join(partes)
        else:
            # Demais: chave string + lista de valores
            partes = [key] + data_dict[key]
            linha = "/".join(partes)
        if first_line_written:
            file.write("\n")
        file.write(linha)
        first_line_written = True
    
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