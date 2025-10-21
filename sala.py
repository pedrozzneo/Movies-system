def menu():
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 6 or escolha < 1:
        print("\nSubmenu de salas:")
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
 
def listar_todos(sala_dict):
    # Exibe todas as salas sem distinção 
    for key in sala_dict.keys():
        print(f"Código: {key} // Nome: {sala_dict[key][0]} // Capacidade: {sala_dict[key][1]} // Tipo de exibição: {sala_dict[key][2]} // Acessível: {sala_dict[key][3]}")

def listar_especifico(sala_dict, codigo = None):
    # Coleta o código que o usuário deseja exibir caso já não tenho sido passado por parâmetro (funcão alterar)
    if codigo == None:
        codigo = input("Código: ")

    # Exibe caso o codigo realmente exista no dicionário
    if codigo in sala_dict:
        print(f"Nome: {sala_dict[codigo][0]} // Capacidade: {sala_dict[codigo][1]} // Tipo de exibição: {sala_dict[codigo][2]} // Acessível: {sala_dict[codigo][3]}")
        return 
    else:
        print("Chave não encontrada.")

def incluir(sala_dict):
    # Garante a entrada de um código único
    codigo = input("codigo: ")
    while codigo in sala_dict.keys():
        codigo = input("código já em uso, insira outro: ")
    
    # Obtém todos os outros atributos
    nome = input("Nome: ")
    duracao = input("Capacidade: ")
    classificacao = input("Tipo de exibição: ")
    disponivel = input("Acessível: ")

    # Formata o conteúdo na estrutura do arquivo
    conteudo = "\n" + codigo + "/" + nome + "/" + duracao + "/" + classificacao + "/" + disponivel

    # Escreve no arquivo
    arquivo = open("arquivos/sala.txt", "a")
    arquivo.write(conteudo)
    arquivo.close()

    # Adiciona ao dicionário a nova chave e seus elementos
    sala_dict[codigo] = [nome, duracao, classificacao, disponivel]

def alterar(sala_dict):
    # Força uma entrada válida de código para continuar com a operação
    codigo = input("Código: ")
    if codigo in sala_dict:
        listar_especifico(sala_dict, codigo)
    else:
        print("Código não encontrado")
        return

    # Declara dicionário referenciando a ordem dos dados (posicao) e o que eles se referem no sala_dict
    posicoes_dict = {1: "Nome", 2: "Capacidade", 3: "Tipo de exibição", 4: "Acessível"}

    # Força uma entrada válida de qual dado o usuário quer alterar (posicao)
    posicao = 0
    while posicao not in posicoes_dict.keys():
        posicao = int(input(f"\nQual dado deseja mudar? \n1- {posicoes_dict[1]}\n2- {posicoes_dict[2]}\n3- {posicoes_dict[3]}\n4- {posicoes_dict[4]}\nEscolha: "))
        
        if posicao not in posicoes_dict.keys():
            print("Posição inválida!")

    # Coleta o valor que vai ser substituir o anterior
    novo_valor = input("Digite o novo valor: ")
    
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"{sala_dict[codigo][posicao-1]} -> {novo_valor} \nConfirma essa troca? (entre apenas 'sim' ou 'nao'): ")
    sala_dict[codigo][posicao - 1] = novo_valor

    # Outputs de acordo com a resposta
    if confirmacao == "sim":
        print(f"Valor atualizado com sucesso!")
    else:
        print("operação cancelada!")

def excluir(sala_dict):
    # Força uma entrada válida de código para continuar com a operação
    codigo = input("Código: ")
    if codigo not in sala_dict.keys():
        print("Código não encontrado")
        return

    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"Confirma a exclusao dos elementos de código {codigo}? (entre apenas 'sim' ou 'nao'): ")
        
        if confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
            print("resposta inválida")

    # Encerra a operação caso a resposta seja negativa
    if confirmacao.lower() == "nao":
        print("Operação cancelada!")
        return

    # Cria cópia do conteúdo escrito no arquivo
    file = open("arquivos/sala.txt", "+r")
    content = file.readlines()
    file.close()

    # Encontra e apaga a linha referente ao código que se deseja apagar
    i = 0
    while i < len(content):
        elementos = content[i].split("/")
        if elementos[0] == codigo:
            del content[i]
            break
        i += 1

    # Sobrescreve o arquivo com a linha removida
    file = open("arquivos/sala.txt", "w")
    file.writelines(content)
    file.close()

    # Atualiza sala_dict
    del sala_dict[codigo]
    
def build_dict(sala_dict):
    # Salva O conteúdo dividido por linhas
    arquivo = open("arquivos/sala.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por '/'
    for linha in conteudo:
        elementos = linha.split("/")
        sala_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].replace("\n", "")]

def main():
    # Declara e monta o dicionário da sala 
    sala_dict = {}
    build_dict(sala_dict)

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()

        if escolha == 1:
            listar_todos(sala_dict)
        elif escolha == 2:
            listar_especifico(sala_dict)
        elif escolha == 3:
            incluir(sala_dict)
        elif escolha == 4:
            alterar(sala_dict)
        elif escolha == 5:
            excluir(sala_dict)
        elif escolha == 6:
            return