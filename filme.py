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

def build_dict(filme_dict):
    # Abre o arquivo, salva seu conteúdo dividido por linhas em uma variável local e depois fecha o arquivo
    arquivo = open("arquivos/filme.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    for linha in conteudo:
        elementos = linha.split("/")
        # Código, Nome, Ano, Diretor, Atores
        filme_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].replace("\n","").strip()]

def incluir_filme(filme_dict):
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
    arquivo = open("arquivos/filme.txt", "a")
    arquivo.write(conteudo)
    arquivo.close()

    # Adiciona ao dicionário a nova chave e seus elementos
    filme_dict[codigo] = [titulo, lancamento, diretor, elenco]

def detalhar_filme(filme_dict, key):
    if key in filme_dict:
        print(f"Título: {filme_dict[key][0]} // Ano de Lançamento: {filme_dict[key][1]}\n\tDiretor: {filme_dict[key][2]} // Elenco principal: {filme_dict[key][3]}\n")
    else:
        print("Código não encontrado!")
        input("Pressione Enter para retornar ao menu inicial.")
        print()

def main():
    # Declara e monta o dicionário do filme
    filme_dict = {}
    build_dict(filme_dict)

    # Oferece opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()
        if escolha == 1:
            listar_dict(filme_dict)
            input("Pressione Enter para retornar ao menu principal...")
        elif escolha == 2:
            key = input("Informe o código do filme: ")
            detalhar_filme(filme_dict, key)
        elif escolha == 3:
            incluir_filme(filme_dict)
        elif escolha == 4:
            #alterar_filme(filme_dict, key)
            print("Função em produção")
        elif escolha == 5:
            #excluir_filme(filme_dict, key)
            print("Função em produção")
        elif escolha == 6:
            return

main()