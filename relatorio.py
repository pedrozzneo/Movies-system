def menu():
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 4 or escolha < 1:
        print("\nSubmenu de salas:")
        print("1- Filtrar salas por exibição e capacidade")
        print("2- Listar todos os filmes a partir de uma data")
        print("3- Exibir todas as informações das sessões de uma data determinada até outra")
        print("4- Sair")
        escolha = int(input("\nEscolha: "))

        if escolha > 4 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha
        
def build_dict_through_file(sala_dict, file):
    # Salva O conteúdo dividido por linhas
    arquivo = open(rf"arquivos/{file}.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por '/'
    for linha in conteudo:
        elementos = linha.split("/")
        sala_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].replace("\n", "")]

def main():
    # Declara e monta o dicionário da sala 
    sala_dict = {}
    build_dict_through_file(sala_dict, "sala")

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()

        # Trata cada uma das escolhas
        if escolha == 1:
           print("hi")
        #    listar_todos(sala_dict)
        # elif escolha == 2:
        #     listar_especifico(sala_dict)
        # elif escolha == 3:
        #     incluir(sala_dict)
        elif escolha == 4:
            return
            
