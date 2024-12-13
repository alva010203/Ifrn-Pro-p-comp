import requests,json,datetime,sys
from tabulate import tabulate

# ano fechado
data_atual = datetime.date.today().year

while True:
    try:
        ano = int(input('Digite um ano entre 2021 e 2024: '))
        if ano < 2021 or ano > 2024:
            print(' O ano deve estar entre 2021 e 2024.')
        else:
            break  
    except ValueError:
        print('insira um número inteiro.')
    except KeyboardInterrupt:
        sys.exit('O usuário finalizou a ação')

try:
    if ano == data_atual:
        strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
        dictCartola = requests.get(strURL).json()
    else:
        arquivo = f'cartola_fc_{ano}.json'
        with open(arquivo, 'r', encoding='utf-8') as file:
            dictCartola = json.load(file)
except requests.exceptions.RequestException as e:                                        
    sys.exit("Erro ao fazer a requisição:", e)
    
except FileNotFoundError:
    sys.exit(f"Erro: O arquivo {arquivo} não foi encontrado.")
    
except json.JSONDecodeError:
    sys.exit(f"Erro ao decodificar o arquivo {arquivo}.")
    
except UnicodeDecodeError:
    sys.exit(f"Erro ao decodificar o arquivo {arquivo}.")
    
try:
    def mostrar_menu():
        print("\nEscolha a escala de jogadores:")
        print("1. 3-4-3")
        print("2. 3-5-2")
        print("3. 4-3-3")
        print("4. 4-4-2")
        print("5. 4-5-1")
        print("6. 5-3-2")
        print("7. 5-4-1")
        print("0. Sair")
except KeyboardInterrupt:
    print('O usuário finalizou a ação')

def calcular_pontuacao(atleta):
    return atleta['pontuacao'] * atleta['partidas']

def ajustar_url_foto(url):
    """
    Ajusta a URL da foto do jogador substituindo '_FORMATO_' ou '_FORMATO' por '_220x220_' ou '_220x220'.
    """
    if url:
        url = url.replace('_FORMATO_', '_220x220_')
        url = url.replace('_FORMATO', '_220x220')
    return url

def selecionar_jogadores(dictCartola, escala):
    escalas = {
        '3-4-3': {'goleiro': 1, 'zagueiros': 3, 'laterais': 0, 'meias': 4, 'atacantes': 3, 'tecnico': 1},
        '3-5-2': {'goleiro': 1, 'zagueiros': 3, 'laterais': 0, 'meias': 5, 'atacantes': 2, 'tecnico': 1},
        '4-3-3': {'goleiro': 1, 'zagueiros': 2, 'laterais': 2, 'meias': 3, 'atacantes': 3, 'tecnico': 1},
        '4-4-2': {'goleiro': 1, 'zagueiros': 2, 'laterais': 2, 'meias': 4, 'atacantes': 2, 'tecnico': 1},
        '4-5-1': {'goleiro': 1, 'zagueiros': 2, 'laterais': 2, 'meias': 5, 'atacantes': 1, 'tecnico': 1},
        '5-3-2': {'goleiro': 1, 'zagueiros': 3, 'laterais': 2, 'meias': 3, 'atacantes': 2, 'tecnico': 1},
        '5-4-1': {'goleiro': 1, 'zagueiros': 3, 'laterais': 2, 'meias': 4, 'atacantes': 1, 'tecnico': 1}
    }

    posicao_ids = {
        'goleiro': 1,
        'zagueiros': 3,
        'laterais': 2,
        'meias': 4,
        'atacantes': 5,
        'tecnico': 6
    }

    quantidade_posicoes = escalas[escala]
    selecionados = {}

    for posicao, quantidade in quantidade_posicoes.items():
        posicao_id = posicao_ids.get(posicao, None)
        
        if posicao_id:
            jogadores = [atleta for atleta in dictCartola['atletas'] if atleta['posicao_id'] == posicao_id]
            
            for atleta in jogadores:
                atleta['pontuacao_total'] = round(atleta.get('media_num', 0) * atleta.get('jogos_num', 0), 2)
                # Ajuste a URL da foto do jogador
                atleta['url_foto'] = ajustar_url_foto(atleta.get('url_foto', ''))
            
            jogadores = sorted(jogadores, key=lambda x: x.get('pontuacao_total', 0), reverse=True)[:quantidade]
            
            selecionados[posicao] = jogadores

    return selecionados

def imprimir_selecao(selecionados):
    tabela_selecao = []
    for posicao, atletas in selecionados.items():
        for atleta in atletas:
            clube_id = str(atleta['clube_id'])
            clube_nome = dictCartola['clubes'].get(clube_id, {}).get('nome', 'Clube Desconhecido')
            tabela_selecao.append([
                atleta['nome'],
                atleta['apelido'],
                clube_nome,
                posicao.capitalize(),
                f"{atleta.get('pontuacao_total', 0):.2f}"
            ])
    
    print("\nSeleção do Cartola FC:")
    print(tabulate(tabela_selecao, headers=['Nome', 'Apelido', 'Clube', 'Posição', 'Pontuação'], tablefmt='fancy_grid'))


def salvar_escalao(selecionados, escala):
    arquivo_saida = f'escalao_{escala.replace("-", "_")}.json'
    dados_escalao = {}
    
    # Prepara os dados da escalação
    for posicao, atletas in selecionados.items():
        dados_escalao[posicao] = [{'nome': atleta['nome'], 
                                  'apelido': atleta['apelido'], 
                                  'clube': dictCartola['clubes'].get(str(atleta['clube_id']), {}).get('nome', 'Clube Desconhecido'), 
                                  'pontuacao_total': atleta.get('pontuacao_total', 0),
                                  'url_foto': atleta.get('url_foto', 'URL não disponível')} 
                                  for atleta in atletas]

    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as file:
            json.dump(dados_escalao, file, indent=4, ensure_ascii=False)
        print(f"Escalação salva em {arquivo_saida}")
        
    except IOError as e:
        print(f"Erro ao abrir ou escrever no arquivo {arquivo_saida}: {e}")
        
    except PermissionError:
        print(f"Erro: Sem permissão para escrever no arquivo {arquivo_saida}.")
        
    except Exception as e:
        print(f"Erro inesperado ao salvar a escalação: {e}")

try:
    mostrar_menu()
    escolha = input("Escolha a escalação: ")

    escala_map = {
        '1': '3-4-3',
        '2': '3-5-2',
        '3': '4-3-3',
        '4': '4-4-2',
        '5': '4-5-1',
        '6': '5-3-2',
        '7': '5-4-1'
    }

    if escolha == '0':
        print("Saindo...")
        sys.exit()

    escala = escala_map.get(escolha, None)

    if escala:
        selecionados = selecionar_jogadores(dictCartola, escala)
        imprimir_selecao(selecionados)
        salvar_escalao(selecionados, escala)
    else:
        print("Escolha inválida.")
except KeyboardInterrupt:
    print('O usuário finalizou a ação')