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

def salvar_arquivo(filme_dict, nome_arquivo): # Sobreescreve o arquivo com o dicionário / chamada apenas no encerramento
    arquivo = open(nome_arquivo,'w')
    contador = 0
    for key in filme_dict.keys():
        if contador == len(filme_dict)-1:
            arquivo.write(key+'/'+filme_dict[key][0]+'/'+filme_dict[key][1]+'/'+filme_dict[key][2]+'/'+filme_dict[key][3])
        else:
            arquivo.write(key+'/'+filme_dict[key][0]+'/'+filme_dict[key][1]+'/'+filme_dict[key][2]+'/'+filme_dict[key][3]+'\n')
        contador+=1
    arquivo.close

def listar_dict(filme_dict): # Lista os filmes, ordenados por inclusão no sistema
    for key in filme_dict.keys():
        print(f"Código: {key}\n\tTítulo: {filme_dict[key][0]} // Ano de Lançamento: {filme_dict[key][1]}\n\tDiretor: {filme_dict[key][2]} // Elenco principal: {filme_dict[key][3]}\n")
    
def build_dict(filme_dict, nome_arquivo): # Abre o arquivo, salva seu conteúdo dividido por linhas diretamente no dicionário
    if utils.file_exists(nome_arquivo):
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
    print("\nMenu de alteração de filmes:\n\t1 - Título\n\t2 - Ano de lançamento\n\t3 - Diretor\n\t4 - Elenco")
    # Força uma entrada válida
    opc = int(input("Escolha um para alterar: "))
    while opc < 1 and opc > 4:
        opc = int(input("Opção inválida, escolha de 1 à 4! Escolha um para alterar: "))
    novo_valor = input("Informe o novo valor: ")
    confirma = input(f"Confirmação de alteração:\n\tSerá alterado: {filme_dict[key][opc-1]} \n\tpor: {novo_valor}\nConfirma a alteração? (Entre com sim ou nao): ")
    while confirma.lower() != 'sim' and confirma.lower() != 'nao':
        confirma = input("Erro! Digite apenas sim ou nao.\nConfirma alteração? ")
    if confirma.lower() == 'sim':
        filme_dict[key][opc-1] = novo_valor
        return True
    else:
        return False

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

        elif escolha == 2: # Listar um filme específico
            key = input("Informe o código do filme: ")
            while key not in filme_dict.keys():
                key = input("Código inexistente! Informe o código do filme que deseja detalhar: ")
            detalhar_filme(filme_dict, key)

        elif escolha == 3: # Incluir novo filme no catálogo
            incluir_filme(filme_dict)

        elif escolha == 4: # Alterar dados de um filme do catálogo (não é possível alterar Chave/Key/Código)
            continua = 'sim'
            while continua.lower() == 'sim':
                # Força entrada de dados válida para Código do filme
                key = input("Informe o código do filme que deseja alterar: ")
                while key not in filme_dict.keys():
                    key = input("Código inexistente! Informe o código do filme que deseja alterar: ")
                
                if alterar_filme(filme_dict,key,nome_arquivo):
                    print("Alterado com sucesso!!")
                    continua = input("Deseja realizar outra alteração? (Entre apenas com sim ou nao): ")
                    while continua.lower() != 'sim' and continua.lower() != 'nao':
                        continua = input("Erro! Digite apenas sim ou nao, deseja efetuar outra alteração? ")
                else:
                    print("Alteração cancelada! Redirecionando ao menu principal!")

        elif escolha == 5: # Excluir um filme do catálogo
            #excluir_filme(filme_dict, key)
            print("Função em produção")
        elif escolha == 6:
            salvar_arquivo(filme_dict,nome_arquivo)
            return

main()