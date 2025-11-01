import utils
import dict_utils

def existing_element_in_DB(DB, input_message):
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

def valid_index(begin, end):
    # Loop que garante a entrada de um index válido
    index = begin - 1
    while index < begin or index > end:
        index = int(input("\nEscolha: ")) - 1
        if index < begin or index > end:
            print("Posição inválida!")
    return index

def get_new_valid_value_for_edit(dict, key, index):
    # Inicializa o novo valor com o valor anterior para entrar no loop
    novo_valor = dict[key][index]

    # Loop que garante o novo valor ser diferente do anterior
    while novo_valor == dict[key][index]:
        # Trata a escolha de mudar o filme
        if index == 0:
            # Garante a entrada de um filme que exista no 'banco de dados' de filmes
            novo_valor = existing_element_in_DB(DB="filme", input_message="Código do filme: ")

        # Trata a escolha de mudar o preço
        elif index == 1:
            # Garante a entrada de um preço válido
            novo_valor = utils.valid_float(input_message="Preço do Ingresso: ")

        # Se o novo valor for igual ao anterior, avisa e continua o loop
        if novo_valor == dict[key][index]:
            print("O novo valor deve ser diferente!")

    # Retorna o novo valor
    return novo_valor

def list_dict(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False
    
    # Exibe todas as sessões sem distinção 
    for key in sessao_dict:
        print(f"Código da Sala: {key[0]} // Data: {key[1]} // Horário: {key[2]} // Código do Filme: {sessao_dict[key][0]} // Preço do Ingresso: {utils.format_cash(sessao_dict[key][1])}")
    return True

def list_element(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False

    # Garante uma key existente neste módulo
    key = dict_utils.existing_key_in_dict(sessao_dict)

    # Exibe as informações da sessão e retorna True
    print(f"Código do Filme: {sessao_dict[key][0]} // Preço do Ingresso: {utils.format_cash(sessao_dict[key][1])}")
    return True

def include(sessao_dict):
    # Confere se filme e/ou sala estão vazios
    if dict_utils.length_of_dict(file_name="filme") == 0 or dict_utils.length_of_dict(file_name="sala") == 0:
        return False

    # Garante a entrada de uma nova key 
    key = dict_utils.new_key_in_dict(sessao_dict)

    # Garante a entrada de um filme que exista no 'banco de dados' de filmes
    filme = existing_element_in_DB(DB="filme", input_message="Código do filme: ")
    
    # Obtém o preço associado a essa key
    preco = utils.valid_float(input_message="Preço do Ingresso: ")

    # Adiciona a nova key e seus elementos ao dicionário
    sessao_dict[key] = [filme, preco]
    return True

def edit(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False

    # Garante uma key composta existente neste módulo
    key = dict_utils.existing_key_in_dict(sessao_dict)
    
    # Exibe os valores que podem ser trocados pelo index
    print(f"\nQual dado deseja mudar?\n1- Código do Filme: {sessao_dict[key][0]} // 2- Preço do Ingresso: {utils.format_cash(sessao_dict[key][1])}")

    # Garante a entrada de um index válido
    index = valid_index(0, 1)

    # Garante um novo valor válido para aquele index e dicionário
    novo_valor = get_new_valid_value_for_edit(dict=sessao_dict, key=key, index=index)

    # Atualiza o dicionário com as alterações
    return dict_utils.change_dict(dict=sessao_dict, key=key, index=index, new_value=novo_valor)

def delete(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False

    # Garante uma key composta existente neste módulo
    key = dict_utils.existing_key_in_dict(sessao_dict)

    # Deleta o item com aquela key do dicionário a partir dos dados coletados
    return dict_utils.delete_element_in_dict(sessao_dict, key)

def main():
    # Declara o módulo que as operações se referem neste arquivo python
    module = "sessao"
    
    # Declara e monta o dicionário de sessões 
    sessao_dict = dict_utils.build_dict_from_file(module)

    # Continua oferecendo opções até o usuário decidir sair (6)
    option = 0
    while option != 6:
        # Coleta a escolha do usuário a partir do menu
        option = utils.menu(module)

        # Trata a escolha de listar todos
        if option == 1:
            if not list_dict(sessao_dict):
                print("Lista vazia!")

        # Trata a escolha de listar um elemento específico
        elif option == 2:
            if not list_element(sessao_dict):
                print("Lista vazia!")

        # Trata a escolha de incluir um novo elemento
        elif option == 3:
            if not include(sessao_dict):
                print("Chave já em uso ou não há filme e/ou sala!")

        # Trata a escolha de alterar um elemento existente com status pois há mais possibilidades
        elif option == 4:
            if not edit(sessao_dict):
                print("Operação cancelada ou lista vazia!")
            else:
                print("Operação bem sucedida!")
    
        # Trata a escolha de excluir um elemento existente com status pois há mais possibilidades
        elif option == 5:
            if not delete(sessao_dict):
                print("Operação cancelada ou lista vazia!")
            else:
                print("Operação bem sucedida!")

        # Trata a escolha de sair e salvar as alterações no arquivo
        elif option == 6:
            dict_utils.save_dict_in_file(module, sessao_dict)