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

def listar_especifico(sessao_dict, key=None):
    # Constrói a chave que o usuário deseja exibir caso já não tenha sido passado por parâmetro (função alterar)
    if key == None:
        filme = input("Código do filme: ").upper()
        sala = input("Código do sala: ").upper()
        print("Data (DD-MM-AAAA)", end="")
        data = utils.valid_date()
        horario = input("Horario: ")
        key = (filme, sala, data, horario)

    # Exibe caso o codigo exista no dicionário
    if key in sessao_dict:
        print(f"Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")
        return True
    else:
        return False

def incluir(sessao_dict):
    # Constrói a key
    filme = input("Código do filme: ").upper()
    if not utils.element_exists(filme,"filme"):
        return "NO_FILM"
    sala = input("Código do sala: ").upper()
    if not utils.element_exists(sala,"sala"):
        return "NO_ROOM"
    print("Data", end = "")
    data = utils.valid_date()
    horario = input("Horario: ")
    key = [(filme,) (sala, data, horario)]

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
    # Constrói a key
    filme = input("Código do filme: ").upper()
    sala = input("Código do sala: ").upper()
    print("Data (DD-MM-AAAA)", end="")
    data = utils.valid_date()
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Retorna caso essa key não exista no dicionário
    if key not in sessao_dict.keys():
        return "NO_DATA"
    
    # Exibe o preco atual associado a essa key
    print(f"Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")

    # Coleta o valor que vai substituir o anterior
    novo_preco = input("Digite o novo valor: ")

    # Confirma e aplica via utilitário compartilhado (posicao 0 para lista de 1 elemento)
    return dict_utils.change_dict(sessao_dict, key, 0, novo_preco)

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
        return "NO_DATA"

    # Delegar confirmação e exclusão para função compartilhada
    return dict_utils.delete_element_in_dict(sessao_dict, key)

def main():
    # Declara e monta o dicionário de sessões 
    module = "sessao"
    sessao_dict = dict_utils.build_dict_from_file(module)

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        # Coleta a escolha do usuário a partir do menu
        escolha = utils.menu(module)

        # Trata a escolha de listar todos
        if escolha == 1:
            result = listar_todos(sessao_dict)
            if not result:
                print("Lista de sessões está vazia")

        # Trata a escolha de listar um elemento específico
        if escolha == 2:
            result = listar_especifico(sessao_dict)
            if not result:
                print("Sessão não encontrada!")

        # Trata a escolha de incluir um novo elemento
        if escolha == 3:
            utils.turn_code_into_message(module,incluir(sessao_dict))

        # Trata a escolha de alterar um elemento existente
        if escolha == 4:
            utils.turn_code_into_message(module,alterar(sessao_dict))

        # Trata a escolha de excluir um elemento existente
        if escolha == 5:
            utils.turn_code_into_message(module,excluir(sessao_dict))

        # Trata a escolha de sair
        if escolha == 6:
            # Salva todas as alterações no arquivo antes de sair
            dict_utils.save_dict_in_file(module, sessao_dict)
            return "EXIT"