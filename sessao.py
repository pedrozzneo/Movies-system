import utils
import dict_utils

def key_exists_in_sessao_dict(sessao_dict):
    # Loop que garante a entrada de uma key composta existente (sessão)
    key = None
    while key not in sessao_dict:
        # Coleta os dados da key (sala, data, horário)
        sala = input("Código do sala: ").upper()
        data = utils.valid_date(input_message = "Data (DD-MM-AAAA)")
        horario = input("Horario: ")
        key = (sala, data, horario)

        # Se a key não existe, avisa e continua o loop
        if key not in sessao_dict:
            print("Chave não encontrada!")
    return key

def new_key_in_sessao_dict(sessao_dict):
    # Garante uma sala que exista no 'banco de dados' de salas
    sala = element_exists_in_DB(DB = "sala", input_message = "Código do sala: ")
    
    # Garante uma data que seja válida
    data = utils.valid_date(input_message = "Data (DD-MM-AAAA)")
    
    # Coleta o horário
    horario = input("Horario: ")

    # Constroi a key composta e retorna
    key = (sala, data, horario)

    # Se a key já existe, iterativamente chama a mesma função
    if key in sessao_dict:
        print("Chave já em uso!, insira novamente!")
        return new_key_in_sessao_dict(sessao_dict)

    # Retorna a key composta
    return key

def listar_todos(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False
    
    # Exibe todas as sessões sem distinção 
    for key in sessao_dict.keys():
        print(f"Código da Sala: {key[0]} // Data: {key[1]} // Horário: {key[2]} // Código do Filme: {sessao_dict[key][0]} // Preço do Ingresso: {utils.format_cash(sessao_dict[key][1])}")
    return True

def listar_especifico(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False

    # Garante uma key existente neste módulo
    key = key_exists_in_sessao_dict(sessao_dict)

    # Exibe as informações da sessão e retorna True
    print(f"Código do Filme: {sessao_dict[key][0]} // Preço do Ingresso: {utils.format_cash(sessao_dict[key][1])}")
    return True

def element_exists_in_DB(DB, input_message):
    # Loop que garante a entrada de um elemento que exista no 'banco de dados' do módulo
    exists = False
    while not exists:
        # Coleta o elemento
        element = input(input_message).upper()
        
        if dict_utils.element_exists_in_dict(element, DB):
            exists = True
        else:
            print("Elemento não encontrado!")
    return element

def incluir(sessao_dict):
    # Garante a entrada de uma nova key 
    key = new_key_in_sessao_dict(sessao_dict)

    # Garante a entrada de um filme que exista no 'banco de dados' de filmes
    filme = element_exists_in_DB(DB = "filme", input_message = "Código do filme: ")
    
    # Obtém o preço associado a essa key
    print("Preço do Ingresso", end="")
    preco = utils.valid_float()

    # Adiciona a nova key e seus elementos ao dicionário
    sessao_dict[key] = [filme, preco]
    return True

def alterar(sessao_dict):
    # Garante uma key composta existente neste módulo
    key = key_exists_in_sessao_dict(sessao_dict)
    
    # Exibe as opções que podem ser trocadas da key escolhida pela posição
    print(f"\nQual dado deseja mudar?\n1- Código do Filme: {sessao_dict[key][0]} // 2- Preço do Ingresso: {utils.format_cash(sessao_dict[key][1])}")

    # Força uma posição válida para alterar
    index = -1
    while index < 0 or index > 1:
        # Coleta a posição computacional do dado que o usuário quer alterar
        index = int(input(f"\nEscolha: ")) - 1

        # Verifica se a posição é inválida
        if index < 0 or index > 1:
            print("Posição inválida!")

    # Coleta o novo valor que vai substituir o anterior
    if index == 0:  # Se for filme
        novo_valor = input("Código do filme: ").upper()
        if not utils.element_exists(novo_valor, "filme"):
            print("Filme não encontrado!")
            return False
    else:  # Se for preço
        print("Preço do Ingresso", end="")
        novo_valor = utils.valid_float()

    # Aplica as alterações no dicionário a partir dos dados coletados
    return dict_utils.change_dict(sessao_dict, key, index, novo_valor)

def excluir(sessao_dict):
    # Garante uma key composta existente neste módulo
    key = key_exists_in_sessao_dict(sessao_dict)

    # Deleta o item com aquela key do dicionário a partir dos dados coletados
    return dict_utils.delete_element_in_dict(sessao_dict, key)

def main():
    # Declara o módulo que as operações se referem neste arquivo python
    module = "sessao"
    
    # Declara e monta o dicionário de sessões 
    sessao_dict = dict_utils.build_dict_from_file(module)

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        # Coleta a escolha do usuário a partir do menu
        escolha = utils.menu(module)

        # Trata a escolha de listar todos
        if escolha == 1:
            if not listar_todos(sessao_dict):
                print("Lista vazia!")

        # Trata a escolha de listar um elemento específico
        elif escolha == 2:
            if not listar_especifico(sessao_dict):
                print("Lista vazia!")

        # Trata a escolha de incluir um novo elemento
        elif escolha == 3:
            if not incluir(sessao_dict):
                print("Chave já em uso!")

        # Trata a escolha de alterar um elemento existente com status pois há mais possibilidades
        elif escolha == 4:
            if not alterar(sessao_dict):
                print("Operação cancelada!")
            else:
                print("Operação bem sucedida!")
    
        # Trata a escolha de excluir um elemento existente com status pois há mais possibilidades
        elif escolha == 5:
            if not excluir(sessao_dict):
                print("Operação cancelada!")
            else:
                print("Operação bem sucedida!")

        # Trata a escolha de sair e salvar as alterações no arquivo
        elif escolha == 6:
            dict_utils.save_dict_in_file(module, sessao_dict)