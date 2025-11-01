import utils
import dict_utils

def menu():
    # Força uma entrada válida para escolha
    escolha = 0
    while escolha > 4 or escolha < 1:
        # Exibe as opções para receber a escolha
        print("\nSubmenu de relatórios:")
        print("1- Filtrar salas por exibição e capacidade")
        print("2- Listar todos os filmes a partir de um ano")
        print("3- Exibir todas as informações das sessões de uma data determinada até outra")
        print("4- Sair")
        escolha = utils.valid_int(input_message="\nEscolha: ")

        # Trata a escolha do usuário
        if escolha > 4 or escolha < 1:
            print("Escolha inválida")
        else:
            return escolha

def gerar_relatorio_sala_por_exibicao_capacidade(sala_dict):
    # Coleta os filtros do usuário
    exibicao = (input("Exibição: ")).upper()
    capacidade = utils.valid_int(input_message="Capacidade: ")

    # Abre o arquivo em modo write para reescrever todo o conteúdo
    file = open("arquivos/relatorio_salas.txt", "w")

    # Adiciona o título explicando o relatório
    file.write(f"Salas {exibicao} com capacidade para pelo menos {capacidade} pessoas\n\n")

    # Percorre o dicionário e adiciona os itens encontrados ao arquivo
    vazio = True
    for key in sala_dict.keys():
        if int(sala_dict[key][1]) >= capacidade and str(sala_dict[key][2]).upper() == exibicao:
            
            # Formata linha
            linha = f"{sala_dict[key][0]}\n\t{sala_dict[key][2]} com capacidade para {sala_dict[key][1]}\n\tAcessibilidade: {sala_dict[key][3]}\n\n"

            # Adiciona a linha ao arquivo
            file.write(linha)
            vazio = False

    # Fecha o arquivo
    file.close()

    # Retorna status booleano conforme encontrou algo
    if not vazio:
        return True
    else:
        return False

def gerar_relatorio_filme_a_partir_ano(film_dict):
    # Coleta o ano mínimo informado pelo usuário
    year = utils.valid_int(input_message="Ano: ")

    # Abre ou cria o arquivo em modo write para reescrever todo o conteúdo
    file = open("arquivos/relatorio_filmes.txt", "w")

    # Adiciona o título explicando o relatório
    file.write(f"Filmes a partir de {year}\n\n")

    # Variável para verificar se o arquivo é vazio
    vazio = True

    # Percorre o dicionário e adiciona os filmes a partir do ano informado ao arquivo
    for key in film_dict.keys():
        if int(film_dict[key][1]) >= year:

            # Monta linhas
            elenco = ', '.join(film_dict[key][3])
            linha = f"{film_dict[key][0]} ({film_dict[key][1]})\n\tDiretor: {film_dict[key][2]} // Elenco: " + elenco
            linha += '\n\n'

            # Adiciona a linha ao arquivo
            file.write(linha)
            vazio = False

    # Fecha o arquivo
    file.close()

    # Retorna status booleano conforme encontrou algo
    if not vazio:
        return True
    else:
        return False

def gerar_relatorio_sessao_por_periodo(session_dict,film_dict,screen_dict):
    # Importa biblioteca para lidar com datas
    from datetime import date

    # Coleta e formata as datas iniciais
    fromDate = utils.valid_date(input_message="Data início (DD-MM-AAAA)").split("-")
    fromDate = date(int(fromDate[2]), int(fromDate[1]), int(fromDate[0]))

    # Coleta e formata as datas finais
    toDate = utils.valid_date(input_message="Data final (DD-MM-AAAA)").split("-")
    toDate = date(int(toDate[2]), int(toDate[1]), int(toDate[0]))

    # Abre o arquivo em modo write para reescrever todo o conteúdo
    file = open("arquivos/relatorio_sessoes.txt", "w")

    # Adiciona o título explicando o relatório
    file.write(f"Sessoes entre {fromDate.strftime('%d/%m/%Y')} e {toDate.strftime('%d/%m/%Y')}\n\n")

    # Variável para verificar se o arquivo é vazio
    vazio = True

    # Percorre as sessões e adiciona as que estão no intervalo ao arquivo
    for key in session_dict:
        # Coleta e formata a data da sessao
        sessionDate = key[1].split("-")
        sessionDate = date(int(sessionDate[2]), int(sessionDate[1]), int(sessionDate[0]))

        # Adiciona as sessões que satisfazem os filtros ao arquivo
        if sessionDate >= fromDate and sessionDate <= toDate:
            # Formata os dados do filme
            film_ID = session_dict[key][0]
            actors = ', '.join(film_dict[film_ID][3])
            film = f"\n\tFilme: ({film_ID}) - {film_dict[film_ID][0]}\n\t\tElenco: {actors}"

            # Formata os dados da sessão e sala
            screen_ID = key[0]
            session = f"Sessao das {key[2]} do dia {key[1]} da sala {screen_dict[screen_ID][0]} ({screen_ID}):"

            # Formata a linha
            line = session + film + '\n\n'

            # Adiciona a linha ao arquivo
            file.write(line)
            vazio = False

    # Fecha o arquivo
    file.close()

    # Retorna status booleano conforme encontrou algo
    if not vazio:
        return True
    else:
        return False

def main():
    # Declara e monta o dicionário da sala, filme e sessao
    screen_dict = dict_utils.build_dict_from_file("sala")
    film_dict = dict_utils.build_dict_from_file("filme")
    session_dict = dict_utils.build_dict_from_file("sessao")

    # Continua oferecendo opções até o usuário decidir sair (4)
    escolha = 0
    while escolha != 4:
        # Coleta a escolha do usuário a partir do menu
        escolha = menu()

        # Trata cada uma das escolhas
        if escolha == 1:
            if gerar_relatorio_sala_por_exibicao_capacidade(screen_dict):
               print("Relatório gerado com sucesso")
            else:
                print("Nenhuma sala encontrada com os critérios especificados")
            
        # Trata a escolha de listar filmes a partir de um ano
        elif escolha == 2:
            if gerar_relatorio_filme_a_partir_ano(film_dict):
                print("Relatório gerado com sucesso")
            else:
                print("Nenhum filme encontrado a partir do ano especificado")

        # Trata a escolha de listar sessões dentro de um período
        elif escolha == 3:
            if gerar_relatorio_sessao_por_periodo(session_dict, film_dict, screen_dict):
                print("Relatório gerado com sucesso")
            else:
                print("Nenhuma sessão encontrada no período especificado")