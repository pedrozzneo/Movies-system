import utils
import dict_utils

def ensure_key_exists_in_sala_dict(screen_dict):
    # Loop que garante a entrada de uma key existente (sala)
    key = None
    while key not in screen_dict:
        key = input("Codigo: ").upper()
        if key not in screen_dict:
            print("Chave não encontrada!")
    return key

def ensure_key_dont_exists_in_sala_dict(screen_dict):
    # Loop que garante a entrada de uma key que não existe (sala)
    key = input("codigo: ").upper()
    while key in screen_dict:
        # Avisa que a key é repetida
        print("Chave já em uso!")

        # Coleta uma nova key
        key = input("codigo: ").upper()
    return key

def list_dict(screen_dict):
    # Confere se a lista está vazia
    if len(screen_dict) == 0:
        return False

    # Exibe todas as salas sem distinção 
    for key in screen_dict.keys():
        print(f"Código: {key} // Nome: {screen_dict[key][0]} // Capacidade: {screen_dict[key][1]} // Tipo de exibição: {screen_dict[key][2]} // Acessível: {screen_dict[key][3]}")
    return True

def list_element(screen_dict):
    # Confere se a lista está vazia
    if len(screen_dict) == 0:
        return False

    # Garante uma key existente neste módulo
    key = ensure_key_exists_in_sala_dict(screen_dict)

    # Exibe as informações da sala e retorna True
    print(f"Nome: {screen_dict[key][0]} // Capacidade: {screen_dict[key][1]} // Tipo de exibição: {screen_dict[key][2]} // Acessível: {screen_dict[key][3]}")
    return True

def include(screen_dict):
    # Garante uma key que não existe neste módulo
    key = ensure_key_dont_exists_in_sala_dict(screen_dict)
    
    # Obtém todos os valores
    name = input("Nome: ").upper()
    capacity = str(utils.valid_int(input_message="Capacidade: "))
    display_type = input("Tipo de exibição: ").upper()
    accessibility = input("Acessível: ").upper()

    # Adiciona a nova key e seus elementos ao dicionário
    screen_dict[key] = [name, capacity, display_type, accessibility]
    return True

def edit(screen_dict):
    # Garante uma key existente neste módulo
    key = ensure_key_exists_in_sala_dict(screen_dict)

    # Exibe as opções que podem ser trocadas da key escolhida pela posicao
    print(f"\nQual dado deseja mudar?\n1- Nome: {screen_dict[key][0]} // 2- Capacidade: {screen_dict[key][1]} // 3- Tipo de exibição: {screen_dict[key][2]} // 4- Acessível: {screen_dict[key][3]}")

    # Força uma posição válida para alterar
    index = -1
    while index < 0 or index > 3:
        # Coleta a posição computacional do dado que o usuário quer alterar
        index = int(input(f"\nEscolha: ")) - 1 

        # Verifica se a posição é inválida
        if index < 0 or index > 3:
            print("Posição inválida!")

    # Loop que garante um novo valor
    new_value = screen_dict[key][index]
    while new_value == screen_dict[key][index]:
        # Coleta o valor do usuário
        new_value = (input("Digite o novo valor: ")).upper()

        # Verifica se não é igual ao que já tinha
        if new_value == screen_dict[key][index]:
            print("O novo valor deve ser diferente!")

    # Aplica as alterações no dicionário a partir dos dados coletados
    return dict_utils.change_dict(screen_dict, key, index, new_value)
    
def delete(screen_dict):
    # Garante uma key existente neste módulo
    key = ensure_key_exists_in_sala_dict(screen_dict)

    # Deleta o item com aquela key do dicionário a partir dos dados coletados
    return dict_utils.delete_element_in_dict(screen_dict, key)

def main():
    # Declara o módulo que as operações se referem neste arquivo python
    module = "sala"

    # Declara e monta o dicionário da sala 
    screen_dict = dict_utils.build_dict_from_file(module)

    # Continua oferecendo opções até o usuário decidir sair (6)
    option = 0
    while option != 6:
        # Coleta a escolha do usuário a partir do menu
        option = utils.menu(module)

        # Trata a escolha de listar todos
        if option == 1:
            if not list_dict(screen_dict):
                print("Lista vazia!")

        # Trata a escolha de listar um elemento específico
        elif option == 2:
            if not list_element(screen_dict):
                print("Chave não encontrada!")

        # Trata a escolha de incluir um novo elemento
        elif option == 3:
            if not include(screen_dict):
                print("Código já em uso!")

        # Trata a escolha de alterar um elemento existente com status pois há mais possibilidades
        elif option == 4:
            if not edit(screen_dict):
                print("Operação cancelada!")
            else:
                print("Operação bem sucedida!")
    
        # Trata a escolha de excluir um elemento existente com status pois há mais possibilidades
        elif option == 5:
            if not delete(screen_dict):
                print("Operação cancelada!")
            else:
                print("Operação bem sucedida!")
            
        # Trata a escolha de sair e salvar as alterações no arquivo
        elif option == 6:
            dict_utils.save_dict_in_file(module, screen_dict)