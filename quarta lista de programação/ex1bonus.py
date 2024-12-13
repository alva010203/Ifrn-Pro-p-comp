import requests, json, pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

ano_atual = datetime.now().year

# pede o ano
def solicitar_ano():
    while True:
        try:
            ano = int(input(f"Informe o ano desejado (até {ano_atual}): "))
            if ano > ano_atual:
                print(f"O ano informado não pode ser superior a {ano_atual}.")
            else:
                return ano
        except ValueError:
            print("Por favor, insira um número válido para o ano.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


def solicitar_moeda(dictMoedas):
    try:
        moedas_disponiveis = []
        for moeda in dictMoedas['value']:
            moedas_disponiveis.append(moeda['simbolo'])  # armazena as moedas 

        while True:
            moeda = input("Informe a moeda desejada (símbolo): ").upper()
            if moeda in moedas_disponiveis:
                return moeda
            else:
                print("Moeda inválida. As moedas disponíveis são:")
                print(", ".join(moedas_disponiveis))
    except KeyError as e:
        print(f"Erro ao acessar os dados das moedas: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Função para organizar as cotações por mês e calcular as médias
def calcular_medias_mensais(dictCotacoes):
    try:
        meses = {
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
            '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
            '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
        }

        cotacoes_mensais = {}

        for cotacao in dictCotacoes['value']:
            try:
                data = cotacao['dataHoraCotacao'][:10]  
                mes = data[5:7]  
                compra = cotacao['cotacaoCompra']  
                venda = cotacao['cotacaoVenda']  

                # Inicializa o mês se ainda não estiver no dicionário
                if meses[mes] not in cotacoes_mensais:
                    cotacoes_mensais[meses[mes]] = {'total_compra': 0, 'total_venda': 0, 'quantidade': 0}

                # pega o mês puxando o número no dicionário de meses e cria uma chave para cada 
                cotacoes_mensais[meses[mes]]['total_compra'] += compra
                cotacoes_mensais[meses[mes]]['total_venda'] += venda
                cotacoes_mensais[meses[mes]]['quantidade'] += 1
            except (KeyError, TypeError) as e:
                print(f'Erro ao adquirir as cotações: {e}')


        medias_mensais = {}
        for mes, dados in cotacoes_mensais.items():
            try:
                media_compra = round(dados['total_compra'] / dados['quantidade'], 5)  # round usando para arredondar 
                media_venda = round(dados['total_venda'] / dados['quantidade'], 5)
                medias_mensais[mes] = {'media_compra': media_compra, 'media_venda': media_venda}
            except ZeroDivisionError:
                print(f'Erro ao calcular a média, divisão por zero')
    except Exception as e:
        print(f"Ocorreu um erro inesperado no cálculo das médias mensais: {e}")

    return medias_mensais


def salvar_em_json(medias_mensais, moeda, ano):
    try:
        nome_arquivo = f"medias_cotacoes_{moeda}_{ano}.json"
        with open(nome_arquivo, 'w') as arquivo_dados_json:
            json.dump(medias_mensais, arquivo_dados_json, indent=4)
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso.")
    except (IOError, OSError) as e:
        print(f'Erro ao salvar arquivo json: {e}')
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao salvar o arquivo JSON: {e}")


def salvar_em_csv(medias_mensais, moeda, ano):
    try:
        nome_arquivo_csv = f"medias_cotacoes_{moeda}_{ano}.csv"
        with open(nome_arquivo_csv, 'w', encoding='utf-8') as arquivo_dados_csv:
            # Escreve o cabeçalho
            arquivo_dados_csv.write('moeda;mes;media_compra;media_venda\n')

            # Escreve os dados de cada mês
            for mes, medias in medias_mensais.items():
                arquivo_dados_csv.write(f"{moeda};{mes};{medias['media_compra']:.5f};{medias['media_venda']:.5f}\n")

        print(f"Arquivo CSV '{nome_arquivo_csv}' gerado com sucesso.")
    except (IOError, OSError) as e:
        print(f'Erro ao salvar arquivo CSV: {e}')
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao salvar o arquivo JSON: {e}")


def exibir_grafico():
    try:
        nome_arquivo_csv = f"medias_cotacoes_{moeda_desejada}_{ano_desejado}.csv"
        df = pd.read_csv(nome_arquivo_csv, delimiter=';')
        titulo = f"Média Cotações :{moeda_desejada} - Ano: {ano_desejado}"

        plt.figure(figsize=(10, 4))
        plt.suptitle('Cotações')
        plt.plot(df['mes'], df['media_compra'], marker='o', linestyle='-', color='g', label='Média Compra')
        plt.plot(df['mes'], df['media_venda'], marker='o', linestyle=':', color='y', label='Média Venda')
        plt.title(titulo)
        plt.xlabel('Mês')
        plt.ylabel('Valor')
        plt.legend()
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print(f'O arquivo CSV não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao exibir o gráfico: {e}")


strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
try:
    dictMoedas = requests.get(strURL).json()
except requests.RequestException as e:
    print(f"Erro ao fazer a requisição das moedas: {e}")

try:
    ano_desejado = solicitar_ano()
    moeda_desejada = solicitar_moeda(dictMoedas)

    strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
    strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURL += f'@moeda=%27{moeda_desejada}%27&@dataInicial=%2701-01-{ano_desejado}%27&'
    strURL += f'@dataFinalCotacao=%2712-31-{ano_desejado}%27&$format=json'

    # junta todo o link e armazena os dados das cotações
    dictCotacoes = requests.get(strURL).json()

    # Verificar se houve cotações
    if len(dictCotacoes['value']) > 0:
        print(f"Cotações de {moeda_desejada} para o ano de {ano_desejado}:")

        # faz as médias mensais
        medias_mensais = calcular_medias_mensais(dictCotacoes)


        salvar_em_json(medias_mensais, moeda_desejada, ano_desejado)
        salvar_em_csv(medias_mensais, moeda_desejada, ano_desejado)
        exibir_grafico()
    else:
        print(f"Não foram encontradas cotações para {moeda_desejada} no ano de {ano_desejado}.")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
except requests.RequestException as e:
    print(f"Erro ao fazer a requisição das cotações: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
