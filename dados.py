import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Defina o caminho do arquivo CSV
csv_file = '/content/datalogger.csv'  # Substitua pelo caminho do seu arquivo

# Função para carregar e processar o arquivo CSV
def process_and_plot(csv_file):
    # Carregar o arquivo CSV
    df = pd.read_csv(csv_file, header=None, names=['Valor'])
    
    # Separar os dados de temperatura e umidade
    df['Tipo'] = ['Temperatura' if i % 2 == 0 else 'Umidade' for i in range(len(df))]
    
    # Criar colunas separadas para Temperatura e Umidade
    df_temp = df[df['Tipo'] == 'Temperatura'].reset_index(drop=True)
    df_umid = df[df['Tipo'] == 'Umidade'].reset_index(drop=True)
    
    # Unir os dados em um único DataFrame
    data = pd.DataFrame({
        'Temperatura': df_temp['Valor'],
        'Umidade': df_umid['Valor']
    })
    data['Leitura'] = range(1, len(data) + 1)
    
    # Plotagem dos dados
    plt.figure(figsize=(14, 7))
    
    # Gráfico de linhas
    plt.subplot(1, 2, 1)
    sns.lineplot(data=data, x='Leitura', y='Temperatura', marker='o', label='Temperatura')
    sns.lineplot(data=data, x='Leitura', y='Umidade', marker='o', label='Umidade')
    plt.title('Gráfico de Temperatura e Umidade')
    plt.xlabel('Leitura')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    
    # Gráfico de dispersão com linha de tendência
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=data, x='Leitura', y='Temperatura', label='Temperatura', color='blue')
    sns.scatterplot(data=data, x='Leitura', y='Umidade', label='Umidade', color='orange')
    sns.regplot(data=data, x='Leitura', y='Temperatura', scatter=False, color='blue')
    sns.regplot(data=data, x='Leitura', y='Umidade', scatter=False, color='orange')
    plt.title('Dispersão de Temperatura e Umidade com Linha de Tendência')
    plt.xlabel('Leitura')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Chame a função com o caminho para o arquivo CSV
process_and_plot(csv_file)
