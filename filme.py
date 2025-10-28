import utils

def menu():
    #Força uma entrada válida
    escolha = 0
    while escolha > 6 or escolha < 1:
        print("\nMenu de filmes:")
        print("1- Listar todos os filmes")
        print("2- Exibir detalhes de um filme")
        print("3- Incluir filme ao catálogo")
        print("4- Alterar um filme do catálogo")
        print("5- Excluir filme do catálogo")
        print("6- Sair")

        escolha = int(input("\nEscolha: "))
        if escolha > 6 or escolha < 1:
                input("Opção inexistente (escolha de 1 a 6)! Pressione enter para ser redirecionado ao menu novamente.")
        else:
            return escolha

def listar_dict(filme_dict):
    # Lista os filmes, ordenados por inclusão no sistema
    for key in filme_dict.keys():
        print(f"Código: {key}\n\tTítulo: {filme_dict[key][0]} // Ano de Lançamento: {filme_dict[key][1]}\n\tDiretor: {filme_dict[key][2]} // Elenco principal: {filme_dict[key][3]}\n")
    
def build_dict(filme_dict, nome_arquivo): # Abre o arquivo, salva seu conteúdo dividido por linhas diretamente no dicionário
    if utils.existe_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        # Extrai a chave e seus atributos organizados a cada linha separados por '/'
        for linha in arquivo:
            elementos = linha.split("/")
            # Código, Nome, Ano, Diretor, Atores
            filme_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].replace("\n","").strip()]
        arquivo.close()
    else:
        print("Não foi encontrado arquivo de dados.\nVocê será redirecionado para inclusão de dados em novo arquivo.\n")
        arquivo = open(nome_arquivo, 'w')
        arquivo.close()
        incluir_filme(filme_dict,nome_arquivo)

def incluir_filme(filme_dict,nome_arquivo): # Inclui um novo filme no dicionário e registra em arquivo
    # Garante a entrada de um código único
    codigo = input("Código: ")
    while codigo in filme_dict.keys():
        codigo = input("Código já em uso, insira outro: ")
    
    # Obtém os atributos do filme
    titulo = input("Informe o título do filme: ")
    lancamento = input("Informe o ano de lançamento do filme: ")
    diretor = input("Informe o nome do diretor: ")

    # Obtém os nomes dos atores/atrizes e armazena em uma única string
    elenco = ""
    tamanhoElenco = int(input("Informe quantos atores/atrizes quer incluir no elenco: "))
    i=0
    while i < tamanhoElenco:
        i+=1
        nome = input(f"Informe o nome do {i}º Ator/Atriz: ")
        elenco = elenco + nome
        if i < tamanhoElenco:
            elenco = elenco + " "

    # Formata o conteúdo na estrutura do arquivo
    conteudo = "\n" + codigo + "/" + titulo + "/" + lancamento + "/" + diretor + "/" + elenco

    # Escreve no arquivo
    arquivo = open(nome_arquivo, "a")
    arquivo.write(conteudo)
    arquivo.close()

    # Adiciona ao dicionário a nova chave e seus elementos
    filme_dict[codigo] = [titulo, lancamento, diretor, elenco]

def detalhar_filme(filme_dict, key): # Exibe as informações de um filme
    if key in filme_dict:
        print(f"Título: {filme_dict[key][0]} // Ano de Lançamento: {filme_dict[key][1]}\n\tDiretor: {filme_dict[key][2]} // Elenco principal: {filme_dict[key][3]}\n")
    else:
        print("Código não encontrado!")
        input("Pressione Enter para retornar ao menu inicial.")
        print()

def alterar_filme(filme_dict, key, nome_arquivo): # Altera uma das informações de um filme
    detalhar_filme(filme_dict,key)
    continua = 'sim'
    while continua.lower() == 'sim':
        print("\nMenu de alteração de filmes:\n\t1 - Título\n\t2 - Ano de lançamento\n\t3 - Diretor\n\t4 - Elenco")
        opc = int(input("Escolha um para alterar: "))
        while opc < 1 and opc > 4:
            opc = int(input("Opção inválida, escolha de 1 à 4! Escolha um para alterar: "))
        novo_valor = input("Digite o novo valor: ")
        filme_dict[key][opc-1] = novo_valor
        continua = input("Alteração efetuada com sucesso, deseja efetuar outra alteração? (Entre com sim ou nao)\n")
        while continua.lower() != 'sim' and continua.lower() != 'nao':
            continua = input("ERRO: Digite apenas sim ou nao, deseja efetuar outra alteração? ")
        arquivo = open(nome_arquivo,'w')
        for key in filme_dict.keys():
            arquivo.write(filme_dict)
        arquivo.close
        
def main():
    # Declara e monta o dicionário do filme
    filme_dict = {}
    nome_arquivo = "./arquivos/filme.txt"
    build_dict(filme_dict,nome_arquivo)

    # Oferece opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()
        if escolha == 1: # Listar todos os filmes no catálogo
            listar_dict(filme_dict)
            input("Pressione Enter para retornar ao menu principal...")

        elif escolha == 2: # Listar um filme específico
            key = input("Informe o código do filme: ")
            while key not in filme_dict.keys():
                key = input("Código inexistente! Informe o código do filme que deseja detalhar: ")
            detalhar_filme(filme_dict, key)

        elif escolha == 3: # Incluir novo filme no catálogo
            incluir_filme(filme_dict)

        elif escolha == 4: # Alterar dados de um filme do catálogo (não é possível alterar Chave/Key/Código)
            key = input("Informe o código do filme que deseja alterar: ")
            while key not in filme_dict.keys():
                key = input("Código inexistente! Informe o código do filme que deseja alterar: ")
            alterar_filme(filme_dict,key,nome_arquivo)

        elif escolha == 5: # Excluir um filme do catálogo
            #excluir_filme(filme_dict, key)
            print("Função em produção")
        elif escolha == 6:
            return

main()