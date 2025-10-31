def file_exists(nome_arquivo): # Verifica existência de arquivo para construir dicionários
    # Importa biblioteca para lidar com arquivos no armazenamento do pc
    import os

    # Informa se o arquivo existe no computador
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False


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
        print("\nEscolha", end="")
        escolha = valid_int()
        if escolha > 6 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha

def valid_int(): # Validação de dados (inteiros) para evitar erro de entrada
    # Loop em que só é possivel sair ao entra um inteiro válido
    while True:
        # Se a conversão para inteiro for bem sucedida, retorna
        try:
            # Tenta fazer a conversão
            value = int(input(": "))
            
            # Quebra de linha e retorna 
            print()
            return value
        
        # Se deu erro, informa!
        except:
            print("Valor deve ser um inteiro!")

def valid_date(): # Validação de dados (data) para evitar erro de entrada
    # Importa biblioteca para lidar com datas
    from datetime import date

    # Loop em que só é possivel sair ao entra um date válido
    while True:
        # Se a conversão para date for bem sucedida, retorna o texto
        try:
            # Quebra cada informação de texto para verificar se é uma data válida
            values = input(": ").split("-")
            date(int(values[2]), int(values[1]), int(values[0]))
            
            # Volta a data ao formato original de texto
            values = "-".join(values)

            # Retorna a data
            return values

         # Se deu erro, informa! 
        except:
            print("Valor deve ser uma data válida (DD-MM-AAAA)")

def valid_float():# Validação de dados (float) para evitar erro de entrada
    # Loop em que só é possivel sair ao entra um float válido
    while True:
        # Se a conversão para float for bem sucedida, retorna
        try:
            # Tenta fazer a conversão permitindo entrada com "," e "."
            value = float(input(": ").replace(',','.'))
            # Quebra de linha e retorna 
            print()
            return value
        
        # Se deu erro, informa!
        except:
            print("Valor deve ser um número real!")

def format_cash(value): # Apenas para exibição em listagem
    value = f"R$ {value}".replace('.',',')
    return value

def status(module,message): # Mensagens de status para Menu e Main
    if message == "SUCCESS":
        print("Operação realizada com sucesso!")
    if message == "CANCELLED":
        print("Operação cancelada!")
    if message == "NO_DATA":
        print(f"ERRO: {module} não encontrado(a)!")
    if message == "NO_FILM":
        print("ERRO: filme não cadastrado!")
    if message == "NO_ROOM":
        print("ERRO: sala não cadastrada!")
    if message == "USED_KEY":
        if module == "sessao":
            print("ERRO: Já existe uma sessão cadastrada com os mesmos dados!")
        else:
            print("ERRO: Código já cadastrado!")

# change_dict foi movido para dict.py (dict_utils.change_dict)
# build_dict_through_file foi movido para dict.py (dict_utils.change_dict)
# element_exists foi movido para dict.py (dict_utils.change_dict)