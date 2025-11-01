import utils
import dict_utils

def menu():
    # Força uma entrada válida para escolha
    option = 0
    while option > 4 or option < 1:
        # Exibe as opções para receber a escolha
        print("\nSubmenu de relatórios:")
        print("1- Filtrar salas por exibição e capacidade")
        print("2- Listar todos os filmes a partir de um ano")
        print("3- Exibir todas as informações das sessões de uma data determinada até outra")
        print("4- Sair")
        option = utils.valid_int(input_message="\nEscolha: ")

        # Trata a escolha do usuário
        if option > 4 or option < 1:
            print("Escolha inválida")
        else:
            return option

def gerar_relatorio_sala_por_exibicao_capacidade(screen_dict):
    # Coleta os filtros do usuário
    display_type = (input("Exibição: ")).upper()
    capacity = utils.valid_int(input_message="Capacidade: ")

    # Abre o arquivo em modo write para reescrever todo o conteúdo
    file = open("arquivos/relatorio_salas.txt", "w", encoding="utf-8")

    # Adiciona o título explicando o relatório
    file.write(f"Salas {display_type} com capacidade para pelo menos {capacity} pessoas\n\n")

    # Percorre o dicionário e adiciona os itens encontrados ao arquivo
    is_void = True
    for key in screen_dict.keys():
        if int(screen_dict[key][1]) >= capacity and str(screen_dict[key][2]).upper() == display_type:
            
            # Formata linha
            linha = f"{screen_dict[key][0]}\n\t{screen_dict[key][2]} com capacidade para {screen_dict[key][1]}\n\tAcessibilidade: {screen_dict[key][3]}\n\n"

            # Adiciona a linha ao arquivo
            file.write(linha)
            is_void = False

    # Fecha o arquivo
    file.close()

    # Retorna status booleano conforme encontrou algo
    if not is_void:
        return True
    else:
        return False

def gerar_relatorio_filme_a_partir_ano(film_dict):
    # Coleta o ano mínimo informado pelo usuário
    year = utils.valid_int(input_message="Ano: ")

    # Abre ou cria o arquivo em modo write para reescrever todo o conteúdo
    file = open("arquivos/relatorio_filmes.txt", "w", encoding="utf-8")

    # Adiciona o título explicando o relatório
    file.write(f"Filmes a partir de {year}\n\n")

    # Variável para verificar se o arquivo é vazio
    is_void = True

    # Percorre o dicionário e adiciona os filmes a partir do ano informado ao arquivo
    for key in film_dict.keys():
        if int(film_dict[key][1]) >= year:

            # Monta linhas
            elenco = ', '.join(film_dict[key][3])
            linha = f"{film_dict[key][0]} ({film_dict[key][1]})\n\tDiretor: {film_dict[key][2]} // Elenco: " + elenco
            linha += '\n\n'

            # Adiciona a linha ao arquivo
            file.write(linha)
            is_void = False

    # Fecha o arquivo
    file.close()

    # Retorna status booleano conforme encontrou algo
    if not is_void:
        return True
    else:
        return False

def gerar_relatorio_sessao_por_periodo(session_dict, film_dict, screen_dict):
    # Importa biblioteca para lidar com datas
    from datetime import date

    # Coleta e formata as datas iniciais
    from_date = utils.valid_date(input_message="Data início (DD-MM-AAAA)").split("-")
    from_date = date(int(from_date[2]), int(from_date[1]), int(from_date[0]))

    # Coleta e formata as datas finais
    to_date = utils.valid_date(input_message="Data final (DD-MM-AAAA)").split("-")
    to_date = date(int(to_date[2]), int(to_date[1]), int(to_date[0]))

    # Abre o arquivo em modo write para reescrever todo o conteúdo
    file = open("arquivos/relatorio_sessoes.txt", "w", encoding="utf-8")

    # Adiciona o título explicando o relatório
    file.write(f"Sessoes entre {from_date.strftime('%d/%m/%Y')} e {to_date.strftime('%d/%m/%Y')}\n\n")

    # Variável para verificar se o arquivo é vazio
    is_void = True

    # Percorre as sessões e adiciona as que estão no intervalo ao arquivo
    for key in session_dict:
        # Coleta e formata a data da sessao
        sessionDate = key[1].split("-")
        sessionDate = date(int(sessionDate[2]), int(sessionDate[1]), int(sessionDate[0]))

        # Adiciona as sessões que satisfazem os filtros ao arquivo
        if sessionDate >= from_date and sessionDate <= to_date:
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
            is_void = False

    # Fecha o arquivo
    file.close()

    # Retorna status booleano conforme encontrou algo
    if not is_void:
        return True
    else:
        return False

def main():
    # Declara e monta o dicionário da sala, filme e sessao
    screen_dict = dict_utils.build_dict_from_file("sala")
    film_dict = dict_utils.build_dict_from_file("filme")
    session_dict = dict_utils.build_dict_from_file("sessao")

    # Continua oferecendo opções até o usuário decidir sair (4)
    option = 0
    while option != 4:
        # Coleta a escolha do usuário a partir do menu
        option = menu()

        # Trata cada uma das escolhas
        if option == 1:
            if gerar_relatorio_sala_por_exibicao_capacidade(screen_dict):
               print("Relatório gerado com sucesso")
            else:
                print("Nenhuma sala encontrada com os critérios especificados")
            
        # Trata a escolha de listar filmes a partir de um ano
        elif option == 2:
            if gerar_relatorio_filme_a_partir_ano(film_dict):
                print("Relatório gerado com sucesso")
            else:
                print("Nenhum filme encontrado a partir do ano especificado")

        # Trata a escolha de listar sessões dentro de um período
        elif option == 3:
            if gerar_relatorio_sessao_por_periodo(session_dict, film_dict, screen_dict):
                print("Relatório gerado com sucesso")
            else:
                print("Nenhuma sessão encontrada no período especificado")