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
        print(f"Código da Sessão: {key} // Código do Filme: {sessao_dict[key][0]} // Código da Sala: {sessao_dict[key][1]} // Data: {sessao_dict[key][2]} // Horário: {sessao_dict[key][3]} // Preço do Ingresso: {sessao_dict[key][4]}")

def listar_especifico(sessao_dict, codigo=None):
    # Coleta o código que o usuário deseja exibir caso já não tenha sido passado por parâmetro (função alterar)
    if codigo == None:
        codigo = input("Código da Sessão: ")

    # Exibe caso o codigo exista no dicionário
    if codigo in sessao_dict:
        print(f"Código do Filme: {sessao_dict[codigo][0]} // Código da Sala: {sessao_dict[codigo][1]} // Data: {sessao_dict[codigo][2]} // Horário: {sessao_dict[codigo][3]} // Preço do Ingresso: {sessao_dict[codigo][4]}")
        return 
    else:
        print("Chave não encontrada.")

def incluir(sessao_dict):
    # Garante a entrada de um código único
    codigo = input("Código da Sessão: ")
    while codigo in sessao_dict.keys():
        codigo = input("Código já em uso, insira outro: ")
    
    # Obtém todos os outros atributos
    cod_filme = input("Código do Filme: ")
    cod_sala = input("Código da Sala: ")
    data = input("Data (DD/MM/AAAA): ")
    horario = input("Horário (HH:MM): ")
    preco = input("Preço do Ingresso: ")

    # Formata o conteúdo na estrutura do arquivo
    conteudo = "\n" + codigo + "/" + cod_filme + "/" + cod_sala + "/" + data + "/" + horario + "/" + preco

    # Escreve no arquivo
    arquivo = open("arquivos/sessao.txt", "a")
    arquivo.write(conteudo)
    arquivo.close()

    # Adiciona ao dicionário a nova chave e seus elementos
    sessao_dict[codigo] = [cod_filme, cod_sala, data, horario, preco]

def alterar(sessao_dict):
    # Força uma entrada válida de código para continuar com a operação
    codigo = input("Código da Sessão: ")
    if codigo in sessao_dict:
        listar_especifico(sessao_dict, codigo)
    else:
        print("Código não encontrado")
        return

    # Declara dicionário referenciando a ordem dos dados (posição) e o que eles se referem no sessao_dict
    posicoes_dict = {
        1: "Código do Filme",
        2: "Código da Sala",
        3: "Data",
        4: "Horário",
        5: "Preço do Ingresso"
    }

    # Força uma entrada válida de qual dado o usuário quer alterar (posição)
    posicao = 0
    while posicao not in posicoes_dict.keys():
        posicao = int(input(f"\nQual dado deseja mudar? \n1- {posicoes_dict[1]}\n2- {posicoes_dict[2]}\n3- {posicoes_dict[3]}\n4- {posicoes_dict[4]}\n5- {posicoes_dict[5]}\nEscolha: "))
        
        if posicao not in posicoes_dict.keys():
            print("Posição inválida!")

    # Coleta o valor que vai substituir o anterior
    novo_valor = input("Digite o novo valor: ")
    
    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"{sessao_dict[codigo][posicao-1]} -> {novo_valor} \nConfirma essa troca? (entre apenas 'sim' ou 'nao'): ")
    
    # Outputs de acordo com a resposta
    if confirmacao.lower() == "sim":
        sessao_dict[codigo][posicao - 1] = novo_valor
        print(f"Valor atualizado com sucesso!")
    else:
        print("Operação cancelada!")

def excluir(sessao_dict):
    # Força uma entrada válida de código para continuar com a operação
    codigo = input("Código da Sessão: ")
    if codigo not in sessao_dict.keys():
        print("Código não encontrado")
        return

    # Verifica se o usuário realmente deseja confirmar a operação
    confirmacao = ""
    while confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
        confirmacao = input(f"Confirma a exclusão da sessão de código {codigo}? (entre apenas 'sim' ou 'nao'): ")
        
        if confirmacao.lower() != "sim" and confirmacao.lower() != "nao":
            print("Resposta inválida")

    # Encerra a operação caso a resposta seja negativa
    if confirmacao.lower() == "nao":
        print("Operação cancelada!")
        return

    # Cria cópia do conteúdo escrito no arquivo
    file = open("arquivos/sessao.txt", "+r")
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
    file = open("arquivos/sessao.txt", "w")
    file.writelines(content)
    file.close()

    # Atualiza sessao_dict
    del sessao_dict[codigo]
    
def build_dict(sessao_dict):
    # Salva o conteúdo dividido por linhas
    arquivo = open("arquivos/sessao.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por '/'
    for linha in conteudo:
        elementos = linha.split("/")
        sessao_dict[elementos[0]] = [
            elementos[1],
            elementos[2],
            elementos[3],
            elementos[4],
            elementos[5].replace("\n", "")
        ]

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
            return
