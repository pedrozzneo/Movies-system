def main():
    # Abre o arquivo, salva seu conteúdo divido por linhas em uma variável local e depois fecha arquivo
    arquivo = open("users.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por /
    user_dict = {}
    for linha in conteudo:
        elementos = linha.split("/")
        user_dict[elementos[0]] = [elementos[1], elementos[2]]

    print(user_dict)
main()