import utils

def build_dict_from_file(file_name): # Constrói dicionários através dos arquivos .txt
    # Declara o caminho para acessar o arquivo
    file_path = f"arquivos/{file_name}.txt"
    
    # Declara o dicionário
    dict = {}

    # Verifica se o arquivo existe
    if not utils.file_exists(file_path):
        return dict
    
    # Abre o arquivo e lê o conteúdo
    archive = open(file_path, "r")

    # Percorre cada linha do arquivo para montar o dict
    for line in archive:
        # Separa os dados pelo separador '/'
        parts = line.upper().replace("\n","").split("/")

        # Tratamento específico de sessao para construir suas keys e values
        if file_name == "sessao":
            key = (parts[0], parts[1], parts[2])
            value = [parts[3], parts[4]]

        # Tratamento específico de sala para construir suas keys e values
        elif file_name == "sala":
            key = parts[0]
            value = parts[1:]

        # Tratamento específico de filme para construir suas keys e values
        elif file_name == "filme":
            key = parts[0]
            parts[4] = parts[4].split(", ") # É pra ser uma lista de atores
            value = parts[1:]

        # Coloca na estrutura de dicionários
        dict[key] = value
        
    # Fecha o arquivo e retorna o dicionário
    archive.close()
    return dict

def save_dict_in_file(file_name, dict): # Exporta dicionários aos arquivos ao fechar cada submenu
    # Abre o arquivo para escrita
    file = open(f"arquivos/{file_name}.txt", "w")
    
    # Percorre todo o dicionário para codificar seus dados em strings no loop com contador e chave
    for i, key in enumerate(dict):
        # Converte os itens de sessao para texto no formato correto 
        if file_name == "sessao":
            line = f"{'/'.join(key)}/{dict[key][0]}/{dict[key][1]}"

        # Converte os itens de sala para texto no formato correto 
        elif file_name == "sala":
            line = f"{key}/{'/'.join(dict[key])}" 

        # Converte os itens de filme para texto no formato correto
        elif file_name == "filme":
            dict[key][3] = ", ".join(dict[key][3])
            line = f"{key}/{'/'.join(dict[key])}"

        # Coloca o '\n' desde que não seja o último item para evitar linhas em branco
        if i != len(dict) - 1:
            line += "\n"

        # Escreve a linha no arquivo
        file.write(line)
    
    # fecha o arquivo e retorna
    file.close()
    return True

def delete_element_in_dict(dict, key):
    # Verifica se o usuário realmente deseja confirmar a operação
    confirm = ""
    while confirm != "SIM" and confirm != "NAO":
        confirm = input(f"Confirma a exclusao dos elementos de código {key}? (entre apenas 'SIM' ou 'NAO'): ").upper()

    # Encerra a operação caso a resposta seja negativa
    if confirm == "NAO":
        return False

    # Atualiza o dicionário
    del dict[key]
    return True

def change_dict(dict, key, index, new_value):
   # Verifica se o usuário realmente deseja confirmar a operação
   confirm = ""
   while confirm != "SIM" and confirm != "NAO":
       confirm = input(f"{dict[key][index]} -> {new_value} \nConfirma essa troca? (entre apenas 'SIM' ou 'NAO'): ").upper()
   
   # Retorna caso o usuário escolheu interromper a operação
   if confirm == "NAO":
       return False
   
   # Atualiza o dicionário e retorna sucesso
   dict[key][index] = new_value
   return True

def element_exists_in_dict(key,module):
    # Constroi o dicionário do módulo
    module_dict = build_dict_from_file(module)
    
    # Retorna se a key existe ou não no dicionário
    if key in module_dict:
        return True
    else:
        return False
