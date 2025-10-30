import utils

def menu():
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 4 or escolha < 1:
        # Exibe as opções para receber a escolha
        print("\nSubmenu de salas:")
        print("1- Filtrar salas por exibição e capacidade")
        print("2- Listar todos os filmes a partir de um ano")
        print("3- Exibir todas as informações das sessões de uma data determinada até outra")
        print("4- Sair")
        escolha = int(input("\nEscolha: "))

        # Trata a escolha do usuário
        if escolha > 4 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha

def listarSalaPorExibicaoCapacidade(sala_dict):
    # Coleta os filtros do usuário
    exibicao = (input("Exibição: ")).upper()
    capacidade = int(input("Capacidade: "))

    # Percorre o dicionário e exibe os itens encontrados
    found = False
    for item in sala_dict.items():
        if int(item[1][1]) >= capacidade and item[1][2] == exibicao:
            print(f"Código: {item[0]}// Nome: {item[1][0]}// Capacidade: {item[1][1]}// Exibição {item[1][2]}// Acessível: {item[1][3]}")
            found = True

    # Retorna status booleano conforme encontrou algo
    if found:
        return True
    else:
        return False

def listarFilmeAPartirAno(filme_dict):
    # Coleta o ano mínimo informado pelo usuário
    ano = int(input("Ano: "))

    # Percorre o dicionário e exibe os filmes a partir do ano informado
    found = False
    for item in filme_dict.items():
        if int(item[1][1]) >= ano:
            print(f"Código: {item[0]}// Nome: {item[1][0]}// Ano de lançamento: {item[1][1]}// Diretor {item[1][2]}// Atores: {item[1][3]}")
            found = True

    # Retorna status booleano conforme encontrou algo
    if found:
        return True
    else:
        return False

def listSessionFromDateToDate(session_dict):
    # Importa biblioteca para lidar com datas
    from datetime import date

    # Coleta e formata as datas iniciais
    fromDate = input("Data início (DD-MM-AAAA): ").split("-")
    fromDate = date(int(fromDate[2]), int(fromDate[1]), int(fromDate[0]))

    # Coleta e formata as datas finais
    toDate = input("Data final: ").split("-")
    toDate = date(int(toDate[2]), int(toDate[1]), int(toDate[0]))

    # Percorre as sessões e exibe as que estão no intervalo
    found = False
    for item in session_dict.items():
        # Coleta e formata a data da sessao
        sessionDate = item[1][1].split("-")
        sessionDate = date(int(sessionDate[2]), int(sessionDate[1]), int(sessionDate[0]))

        # Exibe as sessões que satisfazem os filtros e guarda a informação que pelo menos 1 foi encontado
        if sessionDate >= fromDate and sessionDate <= toDate:
            print(f"Código do Filme: {item[0]} // Código da Sala: {item[1][0]} // Data: {item[1][1]} // Horário: {item[1][2]} // Preço do Ingresso: {item[1][3]}")
            found = True

    # Retorna status booleano conforme encontrou algo
    if found:
        return True
    else:
        return False

def main():
    # Declara e monta o dicionário da sala, filme e sessao
    sala_dict = utils.build_dict_through_file("sala")
    filme_dict = utils.build_dict_through_file("filme")
    session_dict = utils.build_dict_through_file("sessao")

    # Continua oferecendo opções até o usuário decidir sair (4)
    escolha = 0
    while escolha != 4:
        # Coleta a escolha do usuário a partir do menu
        escolha = menu()

        # Trata cada uma das escolhas
        if escolha == 1:
           status = listarSalaPorExibicaoCapacidade(sala_dict)
           if not status:
               print("Nenhuma sala encontrada com os critérios especificados")

        # Trata a escolha de listar filmes a partir de um ano
        elif escolha == 2:
            status = listarFilmeAPartirAno(filme_dict)
            if not status:
                print("Nenhum filme encontrado a partir do ano especificado")

        # Trata a escolha de listar sessões dentro de um período
        elif escolha == 3:
            status = listSessionFromDateToDate(session_dict)
            if not status:
                print("Nenhuma sessão encontrada no período especificado")
        
        # Trata a escolha de sair
        elif escolha == 4:
            return "EXIT"
