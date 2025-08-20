
# Criar um DataFrame com informações de estudantes contendo nome, idade e nota.
# Alguns valores de nota estarão ausentes (nulos).
# A proposta é aplicar técnicas de tratamento de dados para lidar com esses valores faltantes:
# 
# 1. Preencher os valores nulos da coluna "Nota" com a média das notas.
# 2. Criar uma nova coluna chamada "Nota_mediana" preenchendo os valores nulos com a mediana.
# Criando o DataFrame

import pandas as pd
import numpy as np
df_estudantes = pd.DataFrame({
    'Nome': ['Rafael', 'Briet', 'Ana', 'Luis', 'Rique'],
    'Idade': [14, 15, 14, 16, 15],
    'Nota': [10, np.nan , 6, 8 ,np.nan],
})
print('Data Frame Original:')
print(df_estudantes)
print('\n')

# Preencher a nova coluna com a mediana
mediana_notas = df_estudantes['Nota'].median().round(2) 
df_estudantes['Nota_mediana'] = df_estudantes['Nota'].fillna(mediana_notas)

# Preencher a coluna Nota com a média
media_notas = df_estudantes['Nota'].mean().round(2) 
df_estudantes['Nota'] = df_estudantes['Nota'].fillna(media_notas)
print("\nDataFrame após o tratamento:")


print(df_estudantes)