def menu():
    # Retorna a escolha de qual ação o usuário deseja realizar baseado em opções numeradas
    escolha = 0
    while escolha > 5 or escolha < 1:
        print("\n1- Listar todos")
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
        print(f"Código: {key} // Nome: {sala_dict[key][0]} // Capacidade: {sala_dict[key][1]} // Tipo de exibição: {sala_dict[key][2]} // Acessível: {sala_dict[key][3]}", end = "")
    print()

def listar_especifico(sala_dict):
    # Coleta o código que o usuário deseja exibir as informações sobre
    codigo = input("Código: ")

    # Exibe caso o codigo realmente existe no dicionário
    if codigo in sala_dict:
        print(f"Nome: {sala_dict[codigo][0]} // Capacidade: {sala_dict[codigo][1]} // Tipo de exibição: {sala_dict[codigo][2]} // Acessível: {sala_dict[codigo][3]}", end = "")
        return codigo
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

    # Adiciona ao dicionário que está em memória
    sala_dict[codigo] = [nome, duracao, classificacao, disponivel]

def alterar(sala_dict):
    posicoes_dict = {1: "Nome", 2: "Capacidade", 3: "Tipo de exibição", 4: "Acessível"}
    codigo = listar_especifico(sala_dict)

    posicao = 0
    while posicao not in posicoes_dict.keys():
        posicao = int(input(f"\nQual dado deseja mudar? \n1- {posicoes_dict[1]}\n2- {posicoes_dict[2]}\n3- {posicoes_dict[3]}\n4- {posicoes_dict[4]}\nEscolha: "))
        
        if posicao not in posicoes_dict.keys():
            print("Posição inválida!")

    novo_valor = input("Digite o novo valor: ")
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao" and confirmacao.lower() != "nao":
        confirmacao = input(f"{sala_dict[codigo][posicao-1]} -> {novo_valor} \nConfirma essa troca? (entre apenas 'sim' ou 'nao'): ")
    sala_dict[codigo][posicao - 1] = novo_valor

    print(f"Valor atualizado com sucesso!")

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
    
def build_dict(sala_dict):
    # Abre o arquivo, salva seu conteúdo divido por linhas em uma variável local e depois fecha arquivo
    arquivo = open("arquivos/sala.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    for linha in conteudo:
        elementos = linha.split("/")
        sala_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4]]

def main():
    sala_dict = {}
    build_dict(sala_dict)

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
