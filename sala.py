def menu():
    # Retorna a escolha de qual ação o usuário deseja realizar baseado em opções numeradas
    escolha = 0
    while escolha > 5 or escolha < 1:
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        escolha = int(input("\nEscolha: "))

        if escolha > 5 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha
 
def listar_todos(sala_dict):
    # Exibe todas as salas sem distinção 
    for key in sala_dict.keys():
        print(f"Código: {key}: Nome: {sala_dict[key][0]} // Capacidade: {sala_dict[key][1]} // Tipo de exibição: {sala_dict[key][2]} // Acessível: {sala_dict[key][3]}", end = "")
    print(end = "\n\n")

def listar_especifico(sala_dict):
    # Coleta o código que o usuário deseja exibir as informações sobre
    codigo = input("Digite o codigo da sala que deseja buscar: ")

    # Exibe caso o codigo realmente existe no dicionário
    if codigo in sala_dict:
        print(sala_dict[codigo]) 
    else:
        print("Chave não encontrada.")
        return None

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

    # Adiciona ao dicionário que está em memória
    sala_dict[codigo] = [nome, duracao, classificacao, disponivel]

def alterar(sala_dict):
    codigo = input("Digite o código do elemento que deseja alterar: ")

    if codigo not in sala_dict:
        print("Código não encontrado.")
        return

    print(f"Dados atuais do '{codigo}': {listar_especifico(sala_dict)}")

    posicao = 0
    while posicao not in [1, 2, 3]:
        posicao = int(input("Qual elemento deseja mudar? (1, 2 ou 3): "))

    novo_valor = input("Digite o novo valor: ")
    sala_dict[codigo][posicao - 1] = novo_valor

    print(f"Valor atualizado com sucesso!\nNovo conteúdo de '{codigo}': {sala_dict[codigo]}")

def excluir(sala_dict):
    chave = input("Digite a chave do elemento que deseja alterar: ")
    while chave not in sala_dict.keys():
        chave = input("Chave não encontrada, tente novamente: ")

    file = open("arquivos/sala.txt", "+r")
    content = file.readlines()
    file.close()

    i = 0
    excluido = False
    while i < len(content) and not excluido:
        elementos = content[i].split("/")
        print(elementos[0])
        if elementos[0] == chave:
            del content[i]
            excluido = True
        i += 1
    
    # Atualiza o arquivo e depois o fecha
    file = open("arquivos/sala.txt", "w")
    file.writelines(content)
    file.close()
    
    
def main():
    # Abre o arquivo, salva seu conteúdo divido por linhas em uma variável local e depois fecha arquivo
    arquivo = open("arquivos/sala.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    sala_dict = {}
    for linha in conteudo:
        elementos = linha.split("/")
        sala_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4]]

    escolha = 0
    while escolha != 5:
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
