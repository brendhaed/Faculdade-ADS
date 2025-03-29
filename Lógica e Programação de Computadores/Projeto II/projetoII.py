import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Lista dos meses:
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Carregar os dados do CSV
def carregar_dados():
    arquivo = "anexoprojeto.csv"  
    df = pd.read_csv(arquivo, parse_dates=["data"], dayfirst=True)
    return df

# Filtro dos dados de acordo com o período informado
def filtrar_periodo(df, periodo_inicial, periodo_final):
    inicio = datetime.strptime(periodo_inicial.strip(), "%m/%Y")
    inicio = datetime(inicio.year, inicio.month, 1)

    fim = datetime.strptime(periodo_final.strip(), "%m/%Y")
    if fim.month in [1, 3, 5, 7, 8, 10, 12]:  
        fim = datetime(fim.year, fim.month, 31)
    elif fim.month in [4, 6, 9, 11]:  
        fim = datetime(fim.year, fim.month, 30)
    else:  
        fim = datetime(fim.year, fim.month, 29 if fim.year % 4 == 0 else 28)

    return df[(df['data'] >= inicio) & (df['data'] <= fim)]

# Exibir os dados no formato solicitado
def exibir_dados(df, opcao):
    if opcao == 1:
        print(df.to_string(index=False))  
    elif opcao == 2:
        print(df[['data', 'precip']].to_string(index=False))
    elif opcao == 3:
        print(df[['data', 'maxima', 'minima']].to_string(index=False))
    elif opcao == 4:
        print(df[['data', 'um_relativa', 'vel_vento']].to_string(index=False))
    else:
        print("Opção inválida! Digite um número entre 1 e 4.")

# Mês mais chuvoso
def mes_mais_chuvoso(df):
    df['ano_mes'] = df['data'].dt.to_period('M')
    precip_total = df.groupby('ano_mes')['precip'].sum()
    mes_chuvoso = precip_total.idxmax()
    maior_precip = precip_total.max()

    ano, mes = str(mes_chuvoso).split('-')
    mes_nome = meses[int(mes) - 1]
    
    return {
        "mes_ano_mais_chuvoso": f"{mes_nome} de {ano}",
        "precipitacao_maxima": maior_precip
    }

# Média de temperatura mínima para um mês nos últimos 11 anos
def media_temperatura_minima(df, mes, ano_inicio=2006, ano_fim=2016):
    dicionario_media = {}
    for ano in range(ano_inicio, ano_fim + 1):
        data_filtro = df[(df['data'].dt.month == mes) & (df['data'].dt.year == ano)]
        media_temp = data_filtro['minima'].mean()
        chave = f"{meses[mes - 1]} {ano}"
        dicionario_media[chave] = media_temp
    return dicionario_media

# Gráfico com a média da temperatura mínima
def gerar_grafico_temperatura(dicionario_media, mes, ano_inicio=2006, ano_fim=2016):
    anos = list(dicionario_media.keys())
    medias = list(dicionario_media.values())
    mes_nome = meses[mes - 1]

    plt.figure(figsize=(5, 5))
    plt.bar(anos, medias, color='#4169E1')
    plt.xlabel('Ano')
    plt.ylabel('Média da Temperatura Mínima (°C)')
    plt.title(f'Média da Temperatura Mínima em {mes_nome} ({ano_inicio}-{ano_fim})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.show() 

# Média geral da temperatura mínima do mês
def media_geral_temperatura(dicionario_media):
    return sum(dicionario_media.values()) / len(dicionario_media)

# Menu principal
def menu_escolha():
    df = carregar_dados()  
    while True:
        print("\nMenu Inicial: Análise de Dados Climáticos de Porto Alegre entre 1961 e 2016 ")
        print("1. Visualizar intervalo de dados")
        print("2. Mês mais chuvoso")
        print("3. Média da temperatura mínima de um mês (2006-2016)")
        print("4. Gráfico de barras com a média da temperatura mínima de um mês")
        print("5. Média geral da temperatura mínima de um mês")
        print("0. Sair")

        escolhaUsuario = int(input("Escolha uma opção: "))

        if escolhaUsuario == 0:
            print("Saindo...")
            break  
        elif escolhaUsuario == 1:
            periodo_inicial = input("Digite a data inicial (MM/YYYY): ")
            periodo_final = input("Digite a data final (MM/YYYY): ")

            df_filtrado = filtrar_periodo(df, periodo_inicial, periodo_final)

            print("Escolha o tipo de dados a visualizar:")
            print("1. Todos os dados")
            print("2. Apenas Precipitação")
            print("3. Apenas Temperatura")
            print("4. Apenas Umidade e Vento")
            opcao = int(input("Escolha uma opção: "))

            exibir_dados(df_filtrado, opcao)

# Mês mais chuvoso
        elif escolhaUsuario == 2:
            resultado = mes_mais_chuvoso(df)
            mes_chuvoso = resultado["mes_ano_mais_chuvoso"]
            maior_precip = resultado["precipitacao_maxima"]
            print(f"--> O mês mais chuvoso foi {mes_chuvoso} com uma precipitação total de {maior_precip:.2f} mm.")

# Média da temperatura mínima de um mês (2006-2016)
        elif escolhaUsuario == 3:
            mes = int(input("Digite o mês (1-12): "))
            medias = media_temperatura_minima(df, mes)
            for chave, media in medias.items():
                print(f"{chave}: {media:.2f}°C")

# Gráfico de barras com a média da temperatura mínima de um mês
        elif escolhaUsuario == 4:
            mes = int(input("Digite o mês (1-12): "))
            medias = media_temperatura_minima(df, mes)
            gerar_grafico_temperatura(medias, mes)

            input("Pressione Enter para voltar ao menu...") 
            
# Média geral da temperatura mínima de um mês
        elif escolhaUsuario == 5:
            mes = int(input("Digite o mês (1-12): "))
            medias = media_temperatura_minima(df, mes)
            media_geral = media_geral_temperatura(medias)
            print(f"--> A média geral da temperatura mínima em {meses[mes - 1]} (2006-2016) é: {media_geral:.2f}°C")
        else:
            print("Opção inválida! Digite um número entre 0-5")

menu_escolha()