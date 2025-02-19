import pandas as pd

import os

# Carregar o CSV original
def corrigir_referencias(input_file, output_file):
    # Verificar se o arquivo de entrada existe
    if not os.path.isfile(input_file):
        print(f"Erro: O arquivo {input_file} não foi encontrado.")
        return

    try:
        # Carregar o CSV para um DataFrame
        df = pd.read_csv(input_file, sep=';')
        
        # Remover o sufixo ".03" das referências
        df['Referencia'] = df['Referencia'].apply(lambda x: str(x).rstrip('.03') if str(x).endswith('.03') else x)
        
        # Salvar o arquivo corrigido
        df.to_csv(output_file, index=False, sep=';')
        print(f'Arquivo corrigido gerado: {output_file}')
    
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Usar o caminho do arquivo de entrada e saída
input_file = r'sua_planilha.csv'  # Caminho do arquivo CSV de entrada
output_file = r'C:/Users/Marketing/Desktop/Arquivo CSV/saida_corrigida.csv'  # Caminho do arquivo CSV corrigido

# Executar a função para corrigir as referências
corrigir_referencias(input_file, output_file)
