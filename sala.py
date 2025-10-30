import utils

def listar_todos(sala_dict):
    # Confere se a lista está vazia
    if len(sala_dict) == 0:
        return False

    # Exibe todas as salas sem distinção 
    for key in sala_dict.keys():
        print(f"Código: {key} // Nome: {sala_dict[key][0]} // Capacidade: {sala_dict[key][1]} // Tipo de exibição: {sala_dict[key][2]} // Acessível: {sala_dict[key][3]}")
    return True

def listar_especifico(sala_dict):
    # Coleta o código que o usuário deseja exibir 
    codigo = input("Código: ")

    # Exibe caso o codigo exista no dicionário
    if codigo in sala_dict:
        print(f"Nome: {sala_dict[codigo][0]} // Capacidade: {sala_dict[codigo][1]} // Tipo de exibição: {sala_dict[codigo][2]} // Acessível: {sala_dict[codigo][3]}")
        return True
    else:
        return False

def incluir(dict):
    # Recebe a key código
    key = input("codigo: ")
    
    # Retorna caso essa key já esteja em uso
    if key in dict.keys():
        return False
    
    # Obtém todos os valores
    nome = input("Nome: ")
    print("Capacidade", end = "")
    capacidade = utils.valid_int()
    exibicao = input("Tipo de exibição: ")
    acessivel = input("Acessível: ")

    # Adiciona ao dicionário a nova chave e seus elementos
    dict[key] = [nome, str(capacidade), exibicao, acessivel]
    return True

def alterar(dict):
    # Recebe a key código
    key = input("codigo: ")
    
    # Retorna caso essa key não exista no dicionário
    if key not in dict:
        return "NO_DATA"

    # Exibe as opções que podem ser trocadas da key escolhida pela posicao
    print(f"\nQual dado deseja mudar?\n1- Nome: {dict[key][0]} // 2- Capacidade: {dict[key][1]} // 3- Tipo de exibição: {dict[key][2]} // 4- Acessível: {dict[key][3]}")

    # Força uma posição válida para alterar
    posicao = 0
    while posicao < 1 or posicao > 4:
        # Coleta a posição do dado que o usuário quer alterar
        posicao = int(input(f"\nEscolha: "))

        # Verifica se a posição é inválida
        if posicao < 1 or posicao > 4:
            print("Posição inválida!")

    # Coleta o novo valor que vai substituir o anterior
    novo_valor = input("Digite o novo valor: ")
    
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao != "sim" and confirmacao != "nao":
        confirmacao = input(f"{dict[key][posicao-1]} -> {novo_valor} \nConfirma essa troca? (entre apenas 'sim' ou 'nao'): ").lower()
    
    # Retorna caso o usuário escolheu interromper a operação
    if confirmacao == "nao":
        return "CANCELLED"
    
    # Atualiza o dicionário e retorna sucesso
    dict[key][posicao - 1] = novo_valor
    return "SUCCESS"

def excluir(sala_dict):
    # Força uma entrada válida de código para continuar com a operação
    codigo = input("Código: ")
    if codigo not in sala_dict.keys():
        return "NO_DATA"

    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao != "sim" and confirmacao != "nao":
        confirmacao = input(f"Confirma a exclusao dos elementos de código {codigo}? (entre apenas 'sim' ou 'nao'): ").lower()

    # Encerra a operação caso a resposta seja negativa
    if confirmacao == "nao":
        return "CANCELLED"

    # Atualiza o dicionário
    del sala_dict[codigo]
    return "SUCCESS"

def main():
    # Declara e monta o dicionário da sala 
    sala_dict = utils.build_dict_through_file("sala")

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        # Coleta a escolha do usuário a partir do menu
        escolha = utils.menu("salas")

        # Trata a escolha de listar todos
        if escolha == 1:
            status = listar_todos(sala_dict)
            if not status:
                print("Lista de salas está vazia")

        # Trata a escolha de listar um elemento específico
        elif escolha == 2:
            status = listar_especifico(sala_dict)
            if not status:
                print("Código não encontrado")

        # Trata a escolha de incluir um novo elemento
        elif escolha == 3:
            status = incluir(sala_dict)
            if status:
                print("Sala incluída com sucesso")
        
        # Trata a escolha de alterar um elemento existente
        elif escolha == 4:
            status = alterar(sala_dict)
            if status == "NO_DATA":
                print("Código não encontrado")
            elif status == "CANCELLED":
                print("Operação cancelada")
            elif status == "SUCCESS":
                print("Alteração realizada com sucesso")
        
        # Trata a escolha de excluir um elemento existente
        elif escolha == 5:
            status = excluir(sala_dict)
            if status == "NO_DATA":
                print("Código não encontrado")
            elif status == "CANCELLED":
                print("Operação cancelada")
            elif status == "SUCCESS":
                print("Exclusão realizada com sucesso")
        
        # Trata a escolha de sair
        elif escolha == 6:
            # Salva todas as alterações no arquivo antes de sair
            utils.save_dict_to_file("sala", sala_dict)
            return "EXIT"