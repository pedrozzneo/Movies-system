def file_exists(nome_arquivo): # Verifica existência de arquivo para construir dicionários
    # Importa biblioteca para lidar com arquivos no armazenamento do pc
    import os

    # Informa se o arquivo existe no computador
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

def menu(module):
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 6 or escolha < 1:
        # Exibe as opções e coleta a escolha do usuário no final
        print(f"\nSubmenu de {module}:")
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        print("6- Sair")
        
        # Permite o usuário escolher e valida
        escolha = valid_int(input_message="\nEscolha: ")
        if escolha > 6 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha

def valid_int(input_message): # Validação de dados (inteiros) para evitar erro de entrada
    # Loop em que só é possivel sair ao entra um inteiro válido
    while True:
        # Se a conversão para inteiro for bem sucedida, retorna
        try:
            # Tenta fazer a conversão e retorna se bem sucedida
            value = int(input(input_message))
            
            # Quebra de linha e retorna 
            return value
        
        # Se deu erro, informa!
        except:
            print("O valor deve ser um inteiro!")

def valid_date(input_message): # Validação de dados (data) para evitar erro de entrada
    # Importa biblioteca para lidar com datas
    from datetime import date

    # Loop em que só é possivel sair ao entra um date válido
    while True:
        # Se a conversão para date for bem sucedida, retorna o texto
        try:
            # Quebra cada informação de texto para verificar se é uma data válida
            values = input(f"{input_message}: ").split("-")
            date(int(values[2]), int(values[1]), int(values[0]))
            
            # Volta a data ao formato original de texto
            values = "-".join(values)

            # Retorna a data
            return values

         # Se deu erro, informa! 
        except:
            print("Valor deve ser uma data válida (DD-MM-AAAA)")

def valid_float(input_message):# Validação de dados (float) para evitar erro de entrada
    # Loop em que só é possivel sair ao entra um float válido
    while True:
        # Se a conversão para float for bem sucedida, retorna
        try:
            # Tenta fazer a conversão permitindo entrada com "," e "."
            value = float(input(input_message).replace(',','.'))
            # Quebra de linha e retorna 
            return value
        
        # Se deu erro, informa!
        except:
            print("O valor deve ser um número real!")

def format_cash(value): # Apenas para exibição em listagem
    value = f"R$ {value}".replace('.',',')
    return value

def turn_code_into_message(module, message): # Mensagens de status para Menu e Main
    if message == "SUCCESS":
        print("Operação realizada com sucesso!")
    if message == "CANCELLED":
        print("Operação cancelada!")
    if message == "NO_KEY":
        print(f"Chave não encontrada!")
    if message == "NO_FILM":
        print("ERRO: filme não cadastrado!")
    if message == "NO_ROOM":
        print("ERRO: sala não cadastrada!")
    if message == "USED_KEY":
        if module == "sessao":
            print("ERRO: Já existe uma sessão cadastrada com os mesmos dados!")
        else:
            print("ERRO: Código já cadastrado!")

# Utilidades de coleta/validação de key para reuso entre módulos
def ensure_key_exists_in_dict(dictionary):
    # Loop que garante a entrada de uma key existente (para estruturas com key simples)
    key = None
    while key not in dictionary:
        key = input("codigo: ").upper()
        if key not in dictionary:
            print("Chave não encontrada!")
    return key

def build_session_key_from_input():
    # Coleta e constrói a key composta de sessão
    filme = input("Código do filme: ").upper()
    sala = input("Código do sala: ").upper()
    print("Data (DD-MM-AAAA)", end="")
    data = valid_date()
    horario = input("Horario: ")
    return (filme, sala, data, horario)

def ensure_session_key_exists(sessao_dict):
    # Loop que garante a entrada de uma key composta existente (sessões)
    key = None
    while key not in sessao_dict:
        key = build_session_key_from_input()
        if key not in sessao_dict:
            print("Chave não encontrada!")
    return key

# Garante o retorno de um element que existe na list
# def element_in_list(list, tipo):
#     element = None
#     while element not in list:
#         # Recebe o element 
#         element = input(f"{tipo}: ").upper()

#         # Avisa que a key é repetida
#         if element not in dict:
#             print("Chave não encontrada!")