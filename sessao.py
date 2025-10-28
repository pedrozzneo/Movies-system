def menu():
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 6 or escolha < 1:
        print("\nSubmenu de sessões:")
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        print("6- Sair")
        escolha = int(input("\nEscolha: "))

        if escolha > 6 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha
 
def listar_todos(sessao_dict):
    # Exibe todas as sessões sem distinção 
    for key in sessao_dict.keys():
        print(f"Código do Filme: {key[0]} // Código da Sala: {key[1]} // Data: {key[2]} // Horário: {key[3]} // Preço do Ingresso: {sessao_dict[key]}")

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
        print(f"Código do Filme: {key[0]} // Código da Sala: {key[1]} // Data: {key[2]} // Horário: {key[3]} // Preço do Ingresso: {sessao_dict[key]}")
        return 
    else:
        print("Chave não encontrada.")

def incluir(sessao_dict):
    # Constrói a chave
    filme = input("Código do filme: ")
    sala = input("Código do sala: ")
    data = input("Data: ")
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    # Retorna caso não seja inserida uma nova chave
    if key in sessao_dict.keys():
        print("Chave já em uso!")
        return
    
    # Obtém o valor da key
    preco = input("Preço do Ingresso: ")

    # Formata o conteúdo na estrutura do arquivo
    conteudo = "\n" + filme + "/" + sala + "/" + data + "/" + horario + "/" + preco

    # Escreve no arquivo
    arquivo = open("arquivos/sessao.txt", "a")
    arquivo.write(conteudo)
    arquivo.close()

    # Adiciona ao dicionário a nova chave e seus elementos
    sessao_dict[key] = preco

def alterar(sessao_dict):
    # Constrói a chave
    filme = input("Código do filme: ")
    sala = input("Código do sala: ")
    data = input("Data: ")
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    if key in sessao_dict.keys():
        listar_especifico(sessao_dict, key)
    else:
        print("Código não encontrado")
        return

    # Coleta o valor que vai substituir o anterior
    novo_preco = input("Digite o novo valor: ")
    
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"{sessao_dict[key]} -> {novo_preco} \nConfirma essa troca? (entre apenas 'sim' ou 'nao'): ")
    
    # Retorna se a respota for nao
    if confirmacao.lower() == "nao":
        print("Operação cancelada!")
        return
    
    # Cria cópia do conteúdo escrito no arquivo
    file = open("arquivos/sessao.txt", "+r")
    content = file.readlines()
    file.close()

    # Encontra a linha que deve ser feita a alteração do valor 
    i = 0
    while i < len(content):
        # Desestrutura os elementos separados por '/'
        elementos = content[i].split("/")
        key_atual = (elementos[0], elementos[1], elementos[2], elementos[3])
        
        # Atualiza a linha quando achar a chave correspondente
        if key_atual == key:
            content[i] = filme + "/" + sala + "/" + data + "/" + horario + "/" + novo_preco
            break
        i += 1

    # Sobrescreve o arquivo com a linha removida
    file = open("arquivos/sessao.txt", "w")
    file.writelines(content)
    file.close()

    # Atualiza o dicionário
    sessao_dict[key] = novo_preco
    print(f"Valor atualizado com sucesso!")

def excluir(sessao_dict):
    # Constrói a chave
    filme = input("Código do filme: ")
    sala = input("Código do sala: ")
    data = input("Data: ")
    horario = input("Horario: ")
    key = (filme, sala, data, horario)

    if key not in sessao_dict.keys():
        print("Chave não encontrada")
        return False

    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"Confirma a exclusao de todos os dados dessa chave? (entre apenas 'sim' ou 'nao'): ")
        
        # Output se fez entrada inválida
        if confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
            print("resposta inválida")

    # Encerra a operação caso a resposta seja negativa
    if confirmacao.lower() == "nao":
        print("Operação cancelada!")
        return

    # Atualiza sessao_dict
    del sessao_dict[key]

    # Escreve o novo conteúdo do arquivo removendo a key escolhida
    content = ""
    linha = 1
    for key in sessao_dict.keys():
        # Desestrutura a key e seu valor para escrever na linha separados por '/'
        content += key[0] + "/" + key[1] + "/" + key[2] + "/" + key[3] + "/" + sessao_dict[key]
        
        # Só quebra para a proxíma linha se houver conteúdo para colocar nela
        if linha + 1 <= len(sessao_dict):
            content += "\n"

        # Acompanha a linha que será escrita
        linha += 1

    # Sobrescreve o arquivo com a linha removida
    file = open("arquivos/sessao.txt", "w")
    file.writelines(content)
    file.close()
    
def build_dict(sessao_dict):
    # Salva o conteúdo dividido por linhas
    arquivo = open("arquivos/sessao.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Monta a chave e seu único atributo a partir da separação dos dados do arquivo pelas '/'
    for linha in conteudo:
        elementos = linha.split("/")
        key = (elementos[0], elementos[1], elementos[2], elementos[3])
        sessao_dict[key] = elementos[4].replace("\n", "")

def main():
    # Declara e monta o dicionário de sessões 
    sessao_dict = {}
    build_dict(sessao_dict)

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()

        if escolha == 1:
            listar_todos(sessao_dict)
        elif escolha == 2:
            listar_especifico(sessao_dict)
        elif escolha == 3:
            incluir(sessao_dict)
        elif escolha == 4:
            alterar(sessao_dict)
        elif escolha == 5:
            excluir(sessao_dict)
        elif escolha == 6:
<<<<<<< HEAD
            return
=======
            return
>>>>>>> 41f6d4487537221036e8daa55c60dfb99ac8a54b
