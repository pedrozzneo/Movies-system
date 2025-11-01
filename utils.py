# Menu comum entre módulos
def menu(module):
    # Força uma entrada válida para escolha
    option = 0
    while option > 6 or option < 1:
        # Exibe as opções e coleta a escolha do usuário no final
        print(f"\nSubmenu de {module}:")
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        print("6- Sair")
        
        # Permite o usuário escolher e valida
        option = valid_int(input_message="\nEscolha: ")
        if option > 6 or option < 1:
            print("Escolha inválida")
        else:
            return option

# Validação de dados (inteiros) para evitar erro de entrada
def valid_int(input_message):
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

# Validação de dados (data) para evitar erro de entrada
def valid_date(input_message):
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

# Validação de dados (float) para evitar erro de entrada
def valid_float(input_message):
    # Loop em que só é possivel sair ao entra um float válido
    while True:
        # Se a conversão para float for bem sucedida, retorna
        try:
            # Recebe o valor e substitui "," por "." caso o usuário tenha utilizado
            value = input(input_message).replace(',','.')

            # Tenta fazer a conversão permitindo entrada com "," e "."
            float(value)
            
            # Se conversao for possivel, retorna o valor
            return value
        
        # Se deu erro, informa!
        except:
            print("O valor deve ser um número real!")

# Formata valores em R$XX,XX - Apenas para exibição em listagem
def format_cash(value):
    value = f"R$ {value}".replace('.',',')
    return value
