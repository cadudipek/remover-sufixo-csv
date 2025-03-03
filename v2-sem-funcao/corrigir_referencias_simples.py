import pandas as pd

df = pd.read_csv('sua_planilha.csv', sep=';')
df['Referencia'] = df['Referencia'].apply(lambda x: x[:-3] if str(x).endswith('.03') else x)
df.to_csv('planilha_atualizada.csv', sep=';', index=False)

print("Arquivo atualizado com sucesso!")

