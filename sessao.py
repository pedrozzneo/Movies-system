import utils

def listar_todos(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False
    
    # Exibe todas as sessões sem distinção 
    for key in sessao_dict.keys():
        print(f"Código do Filme: {key[0]} // Código da Sala: {key[1]} // Data: {key[2]} // Horário: {key[3]} // Preço do Ingresso: {sessao_dict[key]}")
    return True

def listar_especifico(sessao_dict, key=None):
    # Constrói a chave que o usuário deseja exibir caso já não tenha sido passado por parâmetro (função alterar)
    if key == None:
        filme = input("Código do filme: ")
        sala = input("Código do sala: ")
        data = input("Data: ")
        horario = input("Horario: ")
        key = (filme, sala, data, horario)

    # Exibe caso o codigo exista no dicionário
    if key in sessao_dict:
        print(f"Preço do Ingresso: {sessao_dict[key]}")
        return True
    else:
        return False

def incluir(sessao_dict):
    # Constrói a key
    filme = input("Código do filme: ")
    sala = input("Código do sala: ")
    data = input("Data: ")
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Retorna caso essa key já esteja em uso
    if key in sessao_dict.keys():
        return False
    
    # Obtém o preco associado a essa key
    preco = input("Preço do Ingresso: ")

    # Adiciona ao dicionário a nova chave e seus elementos
    sessao_dict[key] = preco
    return True

def alterar(sessao_dict):
    # Constrói a key
    filme = input("Código do filme: ")
    sala = input("Código do sala: ")
    data = input("Data: ")
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Retorna caso essa key não exista no dicionário
    if key not in sessao_dict.keys():
        return "NO_DATA"
    
    # Exibe o preco atual associado a essa key
    print(f"Preço do Ingresso: {sessao_dict[key]}")

    # Coleta o valor que vai substituir o anterior
    novo_preco = input("Digite o novo valor: ")
    
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao != "sim" and confirmacao != "nao":
        confirmacao = (input(f"{sessao_dict[key]} -> {novo_preco} \nConfirma essa troca? (entre apenas 'sim' ou 'nao'): ")).lower()
    
    # Encerra a operação caso a resposta seja negativa
    if confirmacao == "nao":
        return "CANCELLED"
    
    # Atualiza o dicionário e retorna sucesso
    sessao_dict[key] = novo_preco
    return "SUCCESS"

def excluir(sessao_dict):
    # Constrói a key
    filme = input("Código do filme: ")
    sala = input("Código do sala: ")
    data = input("Data: ")
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Verifica se a key existe no dicionário
    if key not in sessao_dict.keys():
        return "NO_DATA"

    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"Confirma a exclusao de todos os dados dessa chave? (entre apenas 'sim' ou 'nao'): ")

    # Encerra a operação caso a resposta seja negativa
    if confirmacao.lower() == "nao":
        return "CANCELLED"

    # Atualiza o dicionário
    del sessao_dict[key]
    return "SUCCESS"

def main():
    # Declara e monta o dicionário de sessões 
    sessao_dict = utils.build_dict_through_file("sessao")

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        # Coleta a escolha do usuário a partir do menu
        escolha = utils.menu("sessao")

        # Trata a escolha de listar todos
        if escolha == 1:
            result = listar_todos(sessao_dict)
            if not result:
                print("Lista de sessões está vazia")

        # Trata a escolha de listar um elemento específico
        elif escolha == 2:
            result = listar_especifico(sessao_dict)
            if not result:
                print("Sessão não encontrada")

        # Trata a escolha de incluir um novo elemento
        elif escolha == 3:
            result = incluir(sessao_dict)
            if result:
                print("Sessão incluída com sucesso")
            elif not result:
                print("Chave já em uso!")

        # Trata a escolha de alterar um elemento existente
        elif escolha == 4:
            result = alterar(sessao_dict)
            if result == "NO_DATA":
                print("Sessão não encontrada")
            elif result == "CANCELLED":
                print("Operação cancelada")
            elif result == "SUCCESS":
                print("Alteração realizada com sucesso")

        # Trata a escolha de excluir um elemento existente
        elif escolha == 5:
            result = excluir(sessao_dict)
            if result == "NO_DATA":
                print("Sessão não encontrada")
            elif result == "CANCELLED":
                print("Operação cancelada")
            elif result == "SUCCESS":
                print("Exclusão realizada com sucesso")

        # Trata a escolha de sair
        elif escolha == 6:
            # Salva todas as alterações no arquivo antes de sair
            utils.save_dict_to_file("sessao", sessao_dict)
            return "EXIT"