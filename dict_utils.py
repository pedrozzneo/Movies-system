import utils

# Constrói dicionários através dos arquivos .txt
def build_dict_from_file(file_name):
    # Declara o caminho para acessar o arquivo e o dicionário
    file_path = f"arquivos/{file_name}.txt"
    dict = {}

    # Verifica se o arquivo existe
    import os
    if not os.path.exists(file_path):
        return dict
    
    # Abre o arquivo e lê o conteúdo
    file = open(file_path, "r", encoding="utf-8")

    # Percorre cada linha do arquivo para montar o dict
    for line in file:
        # Separa os dados pelo separador '/', tira o '\n' e coloca em maiúsculo
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
    file.close()
    return dict

# Exporta dicionários aos arquivos ao fechar cada submenu
def save_dict_in_file(file_name, dict):
    # Abre o arquivo para escrita
    file = open(f"arquivos/{file_name}.txt", "w", encoding="utf-8")
    
    # Percorre todo o dicionário para codificar seus dados em strings no loop com contador e chave
    for i, key in enumerate(dict):
        # Converte os itens de sessao para texto no formato correto 
        if file_name == "sessao":
            # Junta tudo com "/"
            line = f"{'/'.join(key)}/{'/'.join(dict[key])}"

        # Converte os itens de sala para texto no formato correto 
        elif file_name == "sala":
            # Junta tudo com "/"
            line = f"{key}/{'/'.join(dict[key])}" 

        # Converte os itens de filme para texto no formato correto
        elif file_name == "filme":
            # Primeiro junta os atores em uma string com ", " e depois junta tudo com "/"
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

# Deleta um elemento do dicionário
def delete_element_in_dict(dict, key):
    # Verifica se o usuário realmente deseja confirmar a operação
    confirm = ""
    while confirm != "SIM" and confirm != "NAO":
        confirm = input(f"Confirma a exclusao dos elementos de código {key}? (entre apenas 'sim' ou 'não'): ").upper()

    # Encerra a operação caso a resposta seja negativa
    if confirm == "NAO":
        return False

    # Atualiza o dicionário
    del dict[key]
    return True

# Altera um elemento do dicionário
def change_dict(dict, key, index, new_value):
    # Verifica se o usuário realmente deseja confirmar a operação
    confirm = ""
    while confirm != "SIM" and confirm != "NAO":
        confirm = input(f"{dict[key][index]} -> {new_value} \nConfirma essa troca? (entre apenas 'sim' ou 'não'): ").upper()
    
    # Retorna caso o usuário escolheu interromper a operação
    if confirm == "NAO":
        return False
    
    # Atualiza o dicionário e retorna sucesso
    dict[key][index] = new_value
    return True

# Verifica se um elemento existe no dicionário
def element_exists_in_dict(key,module):
    # Constroi o dicionário do módulo
    module_dict = build_dict_from_file(module)
    
    # Retorna se a key existe ou não no dicionário
    if key in module_dict:
        return True
    else:
        return False

# Retorna uma key existente dos dicionários de filme e sala
def ensure_key_exists_in_dict(dictionary):
    # Inicializa a key como None para entrar no loop
    key = None

    # Loop que garante a entrada de uma key existente
    while key not in dictionary:
        # Coleta a key
        key = input("Código: ").upper()

        # Se a key não existe, avisa e continua o loop
        if key not in dictionary:
            print("Código não encontrado!")

    # Retorna a key existente
    return key

# Retorna uma key Não Existente dos dicionários de filme e sala
def ensure_key_dont_exists_in_dict(dictionary):
    # Coleta a key
    key = input("Código: ").upper()

    # Loop que garante a entrada de uma key que não existe
    while key in dictionary:
        # Se a key existe, avisa e continua o loop
        if key in dictionary:
            print("Código já em uso!")
            
        # Coleta a key
        key = input("Código: ").upper()
    return key

# Retorna uma key composta existente dos dicionários de sessão
def existing_key_in_dict(dict):
    # Inicializa a key como None para entrar no loop
    key = None
   
    # Loop que garante a entrada de uma key composta existente
    while key not in dict:
        # Coleta os dados da key (sala, data, horário)
        sala = input("Código do sala: ").upper()
        data = utils.valid_date(input_message="Data (DD-MM-AAAA)")
        horario = input("Horario: ")
        key = (sala, data, horario)

        # Se a key não existe, avisa e continua o loop
        if key not in dict:
            print("Chave não encontrada!")

    # Retorna a key composta existente
    return key

# Retorna uma key composta Não Existente dos dicionários de sessão
def new_key_in_dict(dict):
    # Inicializa a flag de existência como False para entrar no loop
    exists = False

    # Garante uma sala que exista no 'banco de dados' de salas
    while not exists:
        # Coleta a sala
        sala = input("Código do sala: ").upper()

        # Verifica se a sala existe no 'banco de dados' de salas
        if element_exists_in_dict(sala, "sala"):
            exists = True
        else:
            print("Sala não encontrada!")
    
    # Garante uma data que seja válida e coleta o horário
    data = utils.valid_date(input_message="Data (DD-MM-AAAA)")
    horario = input("Horario: ")

    # Constroi a key composta e retorna
    key = (sala, data, horario)

    # Se a key já existe, iterativamente chama a mesma função até encontrar uma key válida
    if key in dict:
        print("Chave já em uso!, insira novamente!")
        return new_key_in_dict(dict)

    # Retorna a nova key composta
    return key

# Retorna o tamanho de um dicionário
def length_of_dict(file_name):
    # Constroi o dicionário do módulo
    module_dict = build_dict_from_file(file_name)

    # Retorna o tamanho do dicionário
    return len(module_dict)