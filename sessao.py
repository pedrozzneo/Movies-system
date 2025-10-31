import utils
import dict_utils

def ensure_key_exists_in_sessao_dict(sessao_dict):
    # Loop que garante a entrada de uma key composta existente (sessão)
    key = None
    while key not in sessao_dict:
        filme = input("Código do filme: ").upper()
        sala = input("Código do sala: ").upper()
        print("Data (DD-MM-AAAA)", end="")
        data = utils.valid_date()
        horario = input("Horario: ")
        key = (filme, sala, data, horario)
        if key not in sessao_dict:
            print("Chave não encontrada!")
    return key

def ensure_key_dont_exists_in_sessao_dict(sessao_dict):
    # Loop que garante a entrada de uma key composta que não existe (sessão)
    filme = input("Código do filme: ").upper()
    if not utils.element_exists(filme, "filme"):
        return None
    
    sala = input("Código do sala: ").upper()
    if not utils.element_exists(sala, "sala"):
        return None
    
    print("Data", end = "")
    data = utils.valid_date()
    horario = input("Horario: ")
    key = (filme, sala, data, horario)
    
    while key in sessao_dict:
        # Avisa que a key é repetida
        print("Chave já em uso!")
        
        # Coleta novamente os dados da key
        filme = input("Código do filme: ").upper()
        if not utils.element_exists(filme, "filme"):
            return None
        
        sala = input("Código do sala: ").upper()
        if not utils.element_exists(sala, "sala"):
            return None
        
        print("Data", end = "")
        data = utils.valid_date()
        horario = input("Horario: ")
        key = (filme, sala, data, horario)
    
    return key

def listar_todos(sessao_dict):
    # Confere se a lista está vazia
    if len(sessao_dict) == 0:
        return False
    
    # Exibe todas as sessões sem distinção 
    for key in sessao_dict.keys():
        print(f"Código do Filme: {key[0]} // Código da Sala: {key[1]} // Data: {key[2]} // Horário: {key[3]} // Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")
    return True

def listar_especifico(sessao_dict):
    # Garante uma key existente neste módulo
    key = ensure_key_exists_in_sessao_dict(sessao_dict)

    # Exibe as informações da sessão e retorna True
    print(f"Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")
    return True

def incluir(sessao_dict):
    # Garante uma key composta que não existe neste módulo
    key = ensure_key_dont_exists_in_sessao_dict(sessao_dict)
    
    # Retorna False se não foi possível garantir uma key válida
    if key is None:
        return False
    
    # Obtém o preço associado a essa key
    print("Preço do Ingresso", end="")
    preco = utils.valid_float()

    # Adiciona a nova key e seus elementos ao dicionário
    sessao_dict[key] = [preco]
    return True

def alterar(sessao_dict):
    # Garante uma key composta existente neste módulo
    key = ensure_key_exists_in_sessao_dict(sessao_dict)
    
    # Exibe o preço atual associado à key
    print(f"Preço do Ingresso: {utils.format_cash(sessao_dict[key][0])}")

    # Coleta o valor que vai substituir o anterior
    novo_preco = input("Digite o novo valor: ")

    # Aplica as alterações no dicionário a partir dos dados coletados
    return dict_utils.change_dict(sessao_dict, key, 0, novo_preco)

def excluir(sessao_dict):
    # Garante uma key composta existente neste módulo
    key = ensure_key_exists_in_sessao_dict(sessao_dict)

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
                print("Chave não encontrada!")

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