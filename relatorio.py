from datetime import date

def menu():
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 4 or escolha < 1:
        print("\nSubmenu de salas:")
        print("1- Filtrar salas por exibição e capacidade")
        print("2- Listar todos os filmes a partir de um ano")
        print("3- Exibir todas as informações das sessões de uma data determinada até outra")
        print("4- Sair")
        escolha = int(input("\nEscolha: "))

        if escolha > 4 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha
    
def build_dict_through_file(sala_dict, file):
    # Salva O conteúdo dividido por linhas
    arquivo = open(f"arquivos/{file}.txt")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Extrai a chave e seus atributos organizados a cada linha separados por '/'
    for linha in conteudo:
        elementos = linha.split("/")
        sala_dict[elementos[0]] = [elementos[1], elementos[2], elementos[3], elementos[4].replace("\n", "")]

def listarSalaPorExibicaoCapacidade(sala_dict):
    exibicao = (input("Exibição: ")).upper()
    capacidade = int(input("Capacidade: "))

    for item in sala_dict.items():
        if int(item[1][1]) >= capacidade and item[1][2] == exibicao:
            print(f"Código: {item[0]}// Nome: {item[1][0]}// Capacidade: {item[1][1]}// Exibição {item[1][2]}// Acessível: {item[1][3]}")

def listarFilmeAPartirAno(filme_dict):
    ano = int(input("Ano: "))
    for item in filme_dict.items():
        if int(item[1][1]) >= ano:
            print(f"Código: {item[0]}// Nome: {item[1][0]}// Ano de lançamento: {item[1][1]}// Diretor {item[1][2]}// Atores: {item[1][3]}")

def listSessionFromDateToDate(session_dict):
    # Collect and format fromDate
    fromDate = input("Data início (DD-MM-AAAA): ").split("-")
    fromDate = date(int(fromDate[2]), int(fromDate[1]), int(fromDate[0]))
    print(fromDate)

    # Collect and format toDate 
    toDate = input("Data final: ").split("-")
    toDate = date(int(toDate[2]), int(toDate[1]), int(toDate[0]))
    print(toDate)

    # Something
    for item in session_dict.items():
        # Collect and format sessionDate
        sessionDate = item[1][1].split("-")
        sessionDate = date(int(sessionDate[2]), int(sessionDate[1]), int(sessionDate[0]))
        print(sessionDate)

        if sessionDate >= fromDate and sessionDate <= toDate:
            print(f"Código do Filme: {item[0]} // Código da Sala: {item[1][0]} // Data: {item[1][1]} // Horário: {item[1][2]} // Preço do Ingresso: {item[1][3]}")

def main():
    # Declara e monta o dicionário da sala, filme e sessao
    sala_dict = {}
    filme_dict = {}
    session_dict = {}
    build_dict_through_file(sala_dict, "sala")
    build_dict_through_file(filme_dict, "filme")
    build_dict_through_file(session_dict, "sessao")

    # Continua oferecendo opções até o usuário decidir sair (6)
    escolha = 0
    while escolha != 6:
        escolha = menu()

        # Trata cada uma das escolhas
        if escolha == 1:
           listarSalaPorExibicaoCapacidade(sala_dict)
        elif escolha == 2:
            listarFilmeAPartirAno(filme_dict)
        elif escolha == 3:
            listSessionFromDateToDate(session_dict)
        elif escolha == 4:
            return
            
