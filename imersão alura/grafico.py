# --- Bibliotecas Essenciais ---
# pandas: Para manipulação e análise de dados (ex: DataFrames).
# numpy: Para operações numéricas, especialmente para dados ausentes (NaN).
# matplotlib.pyplot: Para criar e customizar gráficos (é a base para outros).
# seaborn: Para criar gráficos mais bonitos e complexos, de forma mais fácil.
# plotly.express: Para gráficos interativos (ex: mapas, gráficos de barras dinâmicos).
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# --- Carregamento e Preparação Inicial dos Dados ---

# Carregar os dados de um CSV diretamente de uma URL.
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Exibir as 5 primeiras linhas para entender a estrutura dos dados.
print(df.head())
print('\n\n')

# Dicionário para renomear colunas para o português, facilitando a leitura.
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'nivel_de_experiencia',
    'employment_type': 'tipo_de_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'usd', # Mudei para 'usd' para ser mais direto
    'employee_residence': 'residencia_do_empregado',
    'remote_ratio': 'taxa_remoto',
    'company_location': 'localização_empresa',
    'company_size': 'tamanho_da_empresa'
}

# Aplicar o renomeio das colunas no DataFrame.
df = df.rename(columns=renomear_colunas)

# Remover linhas com valores nulos (dados ausentes) para garantir uma análise limpa.
df_limpo = df.dropna()

# Verificar se ainda existem valores nulos. O resultado deve ser zero para todas as colunas.
print(df_limpo.isnull().sum())
print('\n\n')
print(df_limpo.head())

# Converter o tipo da coluna 'ano' de float para int, pois anos são números inteiros.
# O método '.assign()' cria uma nova cópia do DataFrame com a alteração,
# o que é uma boa prática para evitar Side Effects.
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64')) 
print('\n\n')
# Verificar as informações do DataFrame para confirmar a mudança de tipo.
print(df_limpo.info())


# --- Gráficos Estáticos (Matplotlib & Seaborn) ---

# Primeiro Gráfico de Barras: Média Salarial por Nível de Experiência
# ----------------------------------------------------------------------

# Correção: O '.index' foi removido para que a variável 'ordem'
# contenha a Series completa, com os níveis e os valores da média.
ordem = df_limpo.groupby('nivel_de_experiencia')['usd'].mean().sort_values(ascending=False)

# Configurar o tamanho da figura (tela do gráfico).
plt.figure(figsize=(8,5))

# Usar sns.barplot para criar o gráfico.
# CORREÇÃO: Passamos diretamente o índice ('x') e os valores ('y') da nossa Series 'ordem'.
# Isso garante que o gráfico use os dados que já calculamos e ordenamos.
sns.barplot(x=ordem.index, y=ordem.values)

plt.title('Salário Médio por Senioridade')
plt.xlabel('Nível de Experiência')
plt.ylabel('Salário Médio Anual (USD)')
plt.show()

# Segundo Gráfico: Histograma de Salários
# ----------------------------------------------------------------------

plt.figure(figsize=(10, 5)) 
# sns.histplot: Cria um histograma para mostrar a distribuição dos dados.
# bins=50: Divide os salários em 50 "caixas" para contar a frequência em cada uma.
# kde=True: Adiciona uma linha de estimativa de densidade, que suaviza a distribuição.
sns.histplot(df_limpo['usd'], bins = 50, kde=True)
plt.title('Distribuição dos Salários Anuais')
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.show()

# Terceiro Gráfico: Boxplot de Salários
# ----------------------------------------------------------------------

plt.figure(figsize=(8,5))
# sns.boxplot: Ideal para visualizar a distribuição, mediana e outliers dos dados.
sns.boxplot(x=df_limpo['usd'])
plt.title('Boxplot do Salário em USD')
plt.xlabel('Salário em USD')
plt.show()

# Quarto Gráfico: Boxplot da Distribuição por Senioridade
# ----------------------------------------------------------------------

# CORREÇÃO: A sua lista 'ordem_senioridade' usava nomes que não existiam no DataFrame.
# Usei os nomes corretos do DataFrame para garantir que a ordem seja aplicada.
ordem_senioridade = ['EN', 'MI', 'SE', 'Ex']

plt.figure(figsize=(8,5))
# O boxplot por senioridade é ótimo para comparar a distribuição de salários entre os grupos.
# CORREÇÃO: 'x' deve ser 'nivel_de_experiencia', pois é o nome da coluna no DataFrame.
# 'order' garante que a ordem no gráfico seja a que definimos na lista.
sns.boxplot(x='nivel_de_experiencia', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2')
plt.title("Boxplot da distribuição por senioridade")
plt.xlabel("Nível de Experiência")
plt.ylabel("Salário em USD")
plt.show()


# --- Gráficos Interativos (Plotly) ---

# Quinto Gráfico: Média Salarial por Senioridade (Barras interativas)
# ----------------------------------------------------------------------

# CORREÇÃO: Usar 'nivel_de_experiencia', pois é o nome da coluna no DataFrame.
senioridade_media_salario = df_limpo.groupby('nivel_de_experiencia')['usd'].mean().sort_values(ascending=False).reset_index()

# px.bar: Cria um gráfico de barras interativo.
fig = px.bar(senioridade_media_salario,
             x='nivel_de_experiencia', # CORREÇÃO: 'x' deve ser 'nivel_de_experiencia'.
             y='usd',
             title='Média Salarial por Senioridade',
             labels={'nivel_de_experiencia': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
fig.show()

# Sexto Gráfico: Mapa Salarial Interativo
# ----------------------------------------------------------------------

import pycountry

# Função para converter códigos de país ISO-2 para ISO-3, necessários para o Plotly.
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

# Criar nova coluna com o código ISO-3 para o mapa.
# CORREÇÃO: A coluna se chama 'residencia_do_empregado', e não 'residencia'.
df_limpo['residencia_iso3'] = df_limpo['residencia_do_empregado'].apply(iso2_to_iso3)

# Calcular a média salarial apenas para 'Data Scientist' agrupado por país.
df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Criar o mapa interativo (choropleth).
fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='usd',
                    color_continuous_scale='rdylgn',
                    title='Salário médio de Cientista de Dados por país',
                    labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
fig.show()

# Imprimir as primeiras 5 linhas para verificar a nova coluna adicionada.
print(df_limpo.head())


# --- Sétimo Gráfico: Média Salarial de Cientistas de Dados por País (Barras Interativas) ---
# ----------------------------------------------------------------------

# O DataFrame 'media_ds_pais' já tem a média salarial calculada para
# Cientistas de Dados agrupados por país.

# px.bar: Cria um gráfico de barras interativo.
fig_bar_pais = px.bar(data_frame=media_ds_pais,
                      x='residencia_iso3',
                      y='usd',
                      title='Média Salarial de Cientistas de Dados por País',
                      labels={'residencia_iso3': 'País (código ISO-3)', 'usd': 'Média Salarial (USD)'})

# Exibir o gráfico.
fig_bar_pais.show()