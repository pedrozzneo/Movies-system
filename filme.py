# encoding: utf-8
def menu():
    escolha = 0
    while escolha == 0:
        print("\nMenu de filmes:")
        print("1- Listar todos os filmes")
        print("2- Exibir detalhes de um filme")
        print("3- Incluir filme ao catálogo")
        print("4- Alterar um filme do catálogo")
        print("5- Excluir filme do catálogo")
        print("6- Sair")

        # Garante uma entrada válida, evita erro de conversão para inteiro.
        try:
            escolha = int(input("\nEscolha: "))
            print()
            if escolha > 6 or escolha < 1:
                    escolha = 0
                    input("Opção inexistente! Pressione enter para ser redirecionado ao menu novamente.")
            else:
                return escolha
        except:
            escolha = 0
            input("Dados inválidos! Pressione enter para ser redirecionado ao menu novamente.")


def listar_dict(filme_dict):
    # Exibe todas as salas sem distinção 
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

def main():
    # Declara e monta o dicionário do filme
    filme_dict = {}
    build_dict(filme_dict)


    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()

        if escolha == 1:
            listar_dict(filme_dict)
        elif escolha == 2:
            #listar_especifico(filme_dict)
            print("Função em produção")
        elif escolha == 3:
            #incluir(filme_dict)
            print("Função em produção")
        elif escolha == 4:
            #alterar(filme_dict)
            print("Função em produção")
        elif escolha == 5:
            #excluir(filme_dict)
            print("Função em produção")
        elif escolha == 6:
            return

main()