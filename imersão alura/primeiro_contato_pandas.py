import pandas as pd 

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

# Ele descreve melhor os dados 
# Mostra o max, minimo mean == media.
print(df.describe())

# Para saber o tamanho do arquivo
df.shape
print('\n\n')

# Saber a quantidade de linhas e colunas 
linhas, colunas = df.shape[0], df.shape[1]
print('linhas:', linhas)
print('coluna:', colunas)


# Pra saber o nome das colunas 


# Pra renomear as colunas
df = df.rename(columns=renomear_colunas)

print(df.columns)

print('\n\n')
# Pra ver oq tem na coluna nivel_de_experiencia
print(df['nivel_de_experiencia'].value_counts())

print('\n\n')

print(df['localização_empresa'].value_counts())