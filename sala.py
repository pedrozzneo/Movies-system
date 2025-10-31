import utils
import dict_utils

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
    codigo = input("Código: ").upper()

    # Exibe caso o codigo exista no dicionário
    if codigo in sala_dict:
        print(f"Nome: {sala_dict[codigo][0]} // Capacidade: {sala_dict[codigo][1]} // Tipo de exibição: {sala_dict[codigo][2]} // Acessível: {sala_dict[codigo][3]}")
        return True
    else:
        return False

def incluir(dict):
    # Recebe a key código
    key = input("codigo: ").upper()
    
    # Retorna caso essa key já esteja em uso
    if key in dict.keys():
        return False
    
    # Obtém todos os valores
    nome = input("Nome: ").upper()
    print("Capacidade", end = "")
    capacidade = str(utils.valid_int())
    exibicao = input("Tipo de exibição: ").upper()
    acessivel = input("Acessível: ").upper()

    # Adiciona ao dicionário a nova chave e seus elementos
    dict[key] = [nome, capacidade, exibicao, acessivel]
    return True

def alterar(dict):
    # Recebe a key código
    key = input("codigo: ").upper()
    
    # Retorna caso essa key não exista no dicionário
    if key not in dict:
        return "NO_KEY"

    # Exibe as opções que podem ser trocadas da key escolhida pela posicao
    print(f"\nQual dado deseja mudar?\n1- Nome: {dict[key][0]} // 2- Capacidade: {dict[key][1]} // 3- Tipo de exibição: {dict[key][2]} // 4- Acessível: {dict[key][3]}")

    # Força uma posição válida para alterar
    index = -1
    while index < 0 or index > 3:
        # Coleta a posição computacional do dado que o usuário quer alterar
        index = int(input(f"\nEscolha: ")) - 1

        # Verifica se a posição é inválida
        if index < 0 or index > 3:
            print("Posição inválida!")

    # Loop que garante um novo valor
    novo_valor = dict[key][index]
    while novo_valor == dict[key][index]:
        # Coleta o valor do usuário
        novo_valor = (input("Digite o novo valor: ")).upper()

        # Verifica se não é igual ao que já tinha
        if novo_valor == dict[key][index]:
            print("O novo valor deve ser diferente!")

    return dict_utils.change_dict(dict, key, index, novo_valor)
    
def excluir(sala_dict):
    # Força uma entrada válida de código para continuar com a operação
    codigo = input("Código: ").upper()
    if codigo not in sala_dict.keys():
        return "NO_KEY"

    # Delegar confirmação e exclusão para função compartilhada
    return dict_utils.delete_element_in_dict(sala_dict, codigo)

def main():
    # Declara o módulo que as operações se referem neste arquivo python
    module = "sala"

    # Declara e monta o dicionário da sala 
    sala_dict = dict_utils.build_dict_from_file(module)

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        # Coleta a escolha do usuário a partir do menu
        escolha = utils.menu(module)

        # Trata a escolha de listar todos
        if escolha == 1:
            if not listar_todos(sala_dict):
                print("Lista de salas está vazia!")

        # Trata a escolha de listar um elemento específico
        elif escolha == 2:
            if not listar_especifico(sala_dict):
                print("Código não encontrado!")

        # Trata a escolha de incluir um novo elemento
        elif escolha == 3:
            if not incluir(sala_dict):
                print("Código já em uso!")

        # Trata a escolha de alterar um elemento existente com status pois há mais possibilidades
        elif escolha == 4:
            # Alterar retorna um código que indica o que aconteceu
            code = alterar(sala_dict)

            # Traduz de forma mais clara ao usuário
            utils.turn_code_into_message(module, code)

        # Trata a escolha de excluir um elemento existente com status pois há mais possibilidades
        elif escolha == 5:
            # Alterar retorna um código que indica o que aconteceu
            code = excluir(sala_dict)

            # Traduz de forma mais clara ao usuário
            utils.turn_code_into_message(module, code)
            
        # Trata a escolha de sair e salvar as alterações no arquivo
        elif escolha == 6:
            dict_utils.save_dict_in_file(module, sala_dict)