def delete_element_in_dict(dict, key):
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao != "SIM" and confirmacao != "NAO":
        confirmacao = input(f"Confirma a exclusao dos elementos de código {key}? (entre apenas 'SIM' ou 'NAO'): ").upper()

    # Encerra a operação caso a resposta seja negativa
    if confirmacao == "NAO":
        return "CANCELLED"

    # Atualiza o dicionário
    del dict[key]
    return "SUCCESS"

def change_dict(dict, key, posicao, novo_valor):
    # Determina o valor atual apresentado na confirmação
    if posicao is not None:
        valor_atual = dict[key][posicao]
    else:
        valor_atual = dict[key]

    # Confirmação (SIM/NAO) em maiúsculas
    confirmacao = ""
    while confirmacao != "SIM" and confirmacao != "NAO":
        confirmacao = input(f"{valor_atual} -> {novo_valor} \nConfirma essa troca? (entre apenas 'SIM' ou 'NAO'): ").upper()

    if confirmacao == "NAO":
        return "CANCELLED"

    # Aplica a alteração (posicao é índice 0-based quando fornecido)
    if posicao is not None:
        dict[key][posicao] = novo_valor
    else:
        dict[key] = novo_valor

    return "SUCCESS"

def change_dict(dict, key, posicao, novo_valor):
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao != "SIM" and confirmacao != "NAO":
        confirmacao = input(f"{dict[key][posicao-1]} -> {novo_valor} \nConfirma essa troca? (entre apenas 'SIM' ou 'NAO'): ").upper()
    
    # Retorna caso o usuário escolheu interromper a operação
    if confirmacao == "NAO":
        return "CANCELLED"
    
    # Atualiza o dicionário e retorna sucesso
    dict[key][posicao - 1] = novo_valor
    return "SUCCESS"
