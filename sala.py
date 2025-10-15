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
    
    print(sala_dict)