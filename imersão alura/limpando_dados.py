import pandas as pd 
import numpy as np

df = pd.read_csv(" https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv ")


print(df.head())
print('\n\n')

# Mostra a tabela 
df.info()
print('\n\n')
df.columns

renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'nivel_de_experiencia',
    'employment_type': 'tipo_de_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia_do_empregado',
    'remote_ratio': 'taxa_remoto',
    'company_location': 'localização_empresa',
    'company_size': 'tamanho_da_empresa'
}
# Renomeando
df = df.rename(columns=renomear_colunas)

print(df.head())
print('\n\n')


# Aqui soma tudo e mostra quais são os campos nulos (sem dado)
# No ex a baixo vemos que 10 campos na parte do work_year ta sem estar preenchido(nulo)
print(df.isnull().sum())



# Nos mostra valores unicos expecificos da coluna q vc pedir 
print('\n\n')
print(df['ano'].unique())
# Ela exibe isso:
# [2025.   nan 2024. 2022. 2023. 2020. 2021.]
# O nan aqui é o valor nulo que temos e ele siguinifica:
#  Not a Number == não tem numero 



print(df[df.isnull().any(axis=1)])


df_salarios = pd.DataFrame({
    'Nome': ['Rafael', 'Ana', 'João', 'Renan', 'Roger'],
    'Salario': [2000, np.nan, 8230, np.nan, 100000]
})



# df == base e
# Subistitui o nulo pela a media 
media_salarios = df_salarios['Salario'].mean().round(2)
df_salarios['salario_media'] = df_salarios['Salario'].fillna(media_salarios)

# A mediana é mais pra vc conseguir meio q saber a media real pois 
# Se vc olhar a media ela ta muito alta ja  ' na mediana da pra ter uma noção melhor 
# Substitue o nulo pela mediana 
media_salarios = df_salarios['Salario'].median().round(2)
df_salarios['salario_mediana'] = df_salarios['Salario'].fillna(media_salarios)
print(df_salarios)
print('\n\n')


# DataFrame == tabela
df_temperaturas = pd.DataFrame({
    'Dia': ['Segunda', 'Qerça', 'Quarta', 'Quinta','Sexta'],
    'Temperatura': [30, np.nan, np.nan, 28, 27]
})
# O .ffill ele pega o dado anterior e coloca no nulo 
df_temperaturas['preenchido_ffill'] = df_temperaturas['Temperatura'].ffill()

print(df_temperaturas)
print('\n\n')



df_temperaturas = pd.DataFrame({
    'Dia': ['Segunda', 'Qerça', 'Quarta', 'Quinta','Sexta'],
    'Temperatura': [30, np.nan, np.nan, 28, 27]
})
# O .ffill ele pega o dado posterior e coloca no nulo 
df_temperaturas['preenchido_bfill'] = df_temperaturas['Temperatura'].bfill()
print(df_temperaturas)



print('\n\n')
df_cidades = pd.DataFrame({
    'Nome': ['Rafael', 'Ana', 'João', 'Renan', 'Roger'],
    'Cidade': ['são paulo', np.nan, 'Rio de Janeiro', np.nan, np.nan]
})

# Aqui usamos o .fillna pra aducionar no lugar do nulo o 'Não Informado'
# No df_cidades['cidade_preenchida'] é o nome que eu dei pra coluna e ele pode ser qualquer um 
df_cidades['cidade_preenchida'] = df_cidades['Cidade'].fillna('Não Informado')

print(df_cidades)
print('\n\n')
# .dropna() Remove linhas ou colunas que contêm valores nulos
df_limpo = df.dropna()

# tira os nulos
print(df_limpo.isnull().sum())


print('\n\n')

print(df_limpo.head())

# Aqui mudamos o ano que estava em float pra int pois ano é numero inteiro 
# ussando o .assign e .astype
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64')) 
print('\n\n')
print(df_limpo.info)
'''palavra chave do curso: pandas, print, matplotlib, alura'''