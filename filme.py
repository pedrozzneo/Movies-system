import utils

def listar_dict(filme_dict):
    # Confere se a lista está vazia
    if len(filme_dict) == 0:
        return False
    
    # Exibe todas as salas sem distinção 
    for key in filme_dict.keys():
        print(f"Código: {key}\n\tTítulo: {filme_dict[key][0]} // Ano de Lançamento: {filme_dict[key][1]}\n\tDiretor: {filme_dict[key][2]} // Elenco principal: {filme_dict[key][3]}\n")
    
    return True

def build_dict():
    import os
    
    file_path = "arquivos/filme.txt"
    
    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado. Criando arquivo vazio...")
        return {}
    
    # Abre o arquivo e lê o conteúdo
    arquivo = open(file_path, "r")
    conteudo = arquivo.read()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    filme_dict = {}
    for linha in conteudo.strip().split("\n"):
        if linha:  # Ignora linhas vazias
            elementos = linha.split("/")
            # Código, Nome, Ano, Diretor, Atores
            filme_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].strip()]
    
    return filme_dict

def detalhar_filme(filme_dict):
    # Funcionalidade ainda não implementada
    return "NOT_IMPLEMENTED"

def salvar_arquivo(filme_dict, file_path):
    return

def main():
    # Declara e monta o dicionário do filme
    filme_dict = build_dict()

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = utils.menu("salas")

        # Trata cada uma das escolhas
        if escolha == 1:
            result = listar_dict(filme_dict)
            if not result:
                print("Lista de filmes está vazia")
        elif escolha == 2:
            result = detalhar_filme(filme_dict)
            if result == "NOT_IMPLEMENTED":
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
            # Salva todas as alterações no arquivo antes de sair
            utils.save_dict_to_file("arquivos/filme.txt", filme_dict)
            return "EXIT"

        # Espera confirmação do usuário para continuar em qualquer fluxo
        input("\nPressione alguma tecla para continuar...")
