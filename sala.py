def menu():
    # Força uma entrada válida de "escolha"
    escolha = 0
    while escolha > 5 or escolha < 1:
        print("1- Listar todos")
        print("2- Listar um elemento específico")
        print("3- Incluir (sem repetição)")
        print("4- Alterar um elemento")
        print("5- Excluir (após confirmação dos dados)")
        escolha = int(input("Escolha: "))

        if escolha > 5 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha
        
def listar_todos(sala_dict):
    print(sala_dict)

def listar_especifico(sala_dict):
    print("listar_especifico")

def incluir(sala_dict):
    print("incluir")

def alterar(sala_dict):
    print("alterar")

def excluir(sala_dict):
    print("excluir")

def main():
    # Abre o arquivo, salva seu conteúdo divido por linhas em uma variável local e depois fecha arquivo
    arquivo = open("arquivos/sala.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    sala_dict = {}
    for linha in conteudo:
        elementos = linha.split("/")
        sala_dict[elementos[0]] = [elementos[1], elementos[2]]

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
