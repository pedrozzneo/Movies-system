import utils

def build_dict_through_file(file_name): # Constrói dicionários ao abrir submenu
    # Declara o caminho para acessar o arquivo
    file_path = f"arquivos/{file_name}.txt"
    
    # Declara o dicionário
    dict = {}

    # Verifica se o arquivo existe
    if not utils.file_exists(file_path):
        return dict
    
    # Abre o arquivo e lê o conteúdo
    arquivo = open(file_path, "r")

    # Percorre cada linha do arquivo para montar o dict
    for linha in arquivo:
        # Separa os dados pelo separador '/'
        partes = linha.upper().replace("\n","").split("/")

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
            partes[4] = partes[4].split(", ") # É pra ser uma lista de atores
            value = partes[1:]

        # Coloca na estrutura de dicionários
        dict[key] = value
        
    # Fecha o arquivo e retorna o dicionário
    arquivo.close()
    return dict

def save_dict_to_file(file_name, dict): # Exporta dicionários aos arquivos ao fechar cada submenu
    # Abre o arquivo para escrita
    file = open(f"arquivos/{file_name}.txt", "w")
    
    # Percorre todo o dicionário para codificar seus dados em strings no loop com contador e chave
    for i, key in enumerate(dict):
        # Converte os itens de sessao para texto no formato correto 
        if file_name == "sessao":
            linha = f"{'/'.join(key)}/{dict[key][0]}"

        # Converte os itens de sala para texto no formato correto 
        elif file_name == "sala":
            linha = f"{key}/{'/'.join(dict[key])}" 

        # Converte os itens de filme para texto no formato correto
        elif file_name == "filme":
            dict[key][3] = ", ".join(dict[key][3])
            linha = f"{key}/{'/'.join(dict[key])}"

        # Coloca o '\n' desde que não seja o último item para evitar linhas em branco
        if i != len(dict) - 1:
            linha += "\n"

        # Escreve a linha no arquivo
        file.write(linha)
    
    # fecha o arquivo e retorna
    file.close()
    return True

def delete_element_in_dict(dict, key):
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao != "SIM" and confirmacao != "NAO":
        confirmacao = input(f"Confirma a exclusao dos elementos de código {key}? (entre apenas 'SIM' ou 'NAO'): ").upper()

    # Encerra a operação caso a resposta seja negativa
    if confirmacao == "NAO":
        return "CANCELLED"

    # Atualiza o dicionário
    del dict[key]
    return "SUCCESS"

def change_dict(dict, key, posicao, novo_valor):
    # Determina o valor atual apresentado na confirmação
    if posicao is not None:
        valor_atual = dict[key][posicao]
    else:
        valor_atual = dict[key]

    # Confirmação (SIM/NAO) em maiúsculas
    confirmacao = ""
    while confirmacao != "SIM" and confirmacao != "NAO":
        confirmacao = input(f"{valor_atual} -> {novo_valor} \nConfirma essa troca? (entre apenas 'SIM' ou 'NAO'): ").upper()

    if confirmacao == "NAO":
        return "CANCELLED"

    # Aplica a alteração (posicao é índice 0-based quando fornecido)
    if posicao is not None:
        dict[key][posicao] = novo_valor
    else:
        dict[key] = novo_valor

    return "SUCCESS"

def element_exists(KEY,element):
    dictionary = build_dict_through_file(element)
    if KEY not in dictionary.keys():
        return True
    else:
        return False

#def change_dict(dict, key, posicao, novo_valor):
#    # Verifica se o usuário realmente deseja confirmar a operação
#    confirmacao = ""
#    while confirmacao != "SIM" and confirmacao != "NAO":
#        confirmacao = input(f"{dict[key][posicao-1]} -> {novo_valor} \nConfirma essa troca? (entre apenas 'SIM' ou 'NAO'): ").upper()
#    
#    # Retorna caso o usuário escolheu interromper a operação
#    if confirmacao == "NAO":
#        return "CANCELLED"
#    
#    # Atualiza o dicionário e retorna sucesso
#    dict[key][posicao - 1] = novo_valor
#    return "SUCCESS"
#