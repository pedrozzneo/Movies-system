def main():
    # Abre o arquivo, salva seu conteúdo dividido por linhas em uma variável local e depois fecha o arquivo
    arquivo = open("arquivos/filme.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    filme_dict = {}
    for linha in conteudo:
        elementos = linha.split("/")
        # Código, Nome, Ano, Diretor, Atores
        filme_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].strip()]
    
    print(filme_dict)
