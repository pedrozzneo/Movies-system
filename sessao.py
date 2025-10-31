import utils
import dict_utils

def listar_todos(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False
    
    # Exibe todas as sessões sem distinção 
    for key in sessao_dict.keys():
        print(f"Código do Filme: {key[0]} // Código da Sala: {key[1]} // Data: {key[2]} // Horário: {key[3]} // Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")
    return True

def listar_especifico(sessao_dict):
    # Coleta os dados da chave
    filme = input("Código do filme: ").upper()
    sala = input("Código do sala: ").upper()
    print("Data (DD-MM-AAAA)", end="")
    data = utils.valid_date()
    horario = input("Horario: ")

    # Constrói a chave
    key = (filme, sala, data, horario)

    # Exibe caso o codigo exista no dicionário
    if key in sessao_dict:
        print(f"Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")
        return True
    else:
        return False

def incluir(sessao_dict):
    # Coleta
    filme = input("Código do filme: ").upper()
    if not utils.element_exists(filme,"filme"):
        return "NO_FILM"
    sala = input("Código do sala: ").upper()
    if not utils.element_exists(sala,"sala"):
        return "NO_ROOM"
    print("Data", end = "")
    data = utils.valid_date()
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Retorna caso essa key já esteja em uso
    if key in sessao_dict.keys():
        return "USED_KEY"
    
    # Obtém o preco associado a essa key
    print("Preço do Ingresso", end="")
    preco = utils.valid_float()

    # Adiciona ao dicionário a nova chave e seus elementos
    sessao_dict[key] = [preco]
    return "SUCCESS"

def alterar(sessao_dict):
    # Loop que garante a entrada de uma key existente
    key = None
    while key not in sessao_dict:
        # Coleta os dados da chave
        filme = input("Código do filme: ").upper()
        sala = input("Código do sala: ").upper()
        print("Data (DD-MM-AAAA)", end="")
        data = utils.valid_date()
        horario = input("Horario: ")

        # Constrói a key
        key = (filme, sala, data, horario)

        # Avisa caso a key não exista
        if key not in sessao_dict:
            print("Código não encontrado!")
    
    # Exibe o preco atual associado a essa key
    print(f"Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")

    # Coleta o valor que vai substituir o anterior
    novo_preco = input("Digite o novo valor: ")

    # Confirma e aplica via utilitário compartilhado (posicao 0 para lista de 1 elemento)
    result = dict_utils.change_dict(sessao_dict, key, 0, novo_preco)
    return result == "SUCCESS"

def excluir(sessao_dict):
    # Constrói a key
    filme = input("Código do filme: ").upper()
    sala = input("Código do sala: ").upper()
    print("Data (DD-MM-AAAA)", end="")
    data = utils.valid_date()
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Verifica se a key existe no dicionário
    if key not in sessao_dict.keys():
        return "NO_KEY"

    # Delegar confirmação e exclusão para função compartilhada
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
                print("Chave não encontrada!")

        # Trata a escolha de incluir um novo elemento
        elif escolha == 3:
            utils.turn_code_into_message(module, incluir(sessao_dict))

        # Trata a escolha de alterar um elemento existente com status pois há mais possibilidades
        elif escolha == 4:
            if not alterar(sessao_dict):
                print("Operação cancelada!")
            else:
                print("Operação bem sucedida!")

        # Trata a escolha de excluir um elemento existente
        elif escolha == 5:
            # Alterar retorna um código que indica o que aconteceu
            code = excluir(sessao_dict)

            # Traduz de forma mais clara ao usuário
            utils.turn_code_into_message(module, code)

        # Trata a escolha de sair e salvar as alterações no arquivo
        elif escolha == 6:
            dict_utils.save_dict_in_file(module, sessao_dict)