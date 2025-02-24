import pandas as pd
import os

# Função para corrigir as referências
def corrigir_referencias(input_file, output_file):
    # Verificar se o arquivo de entrada existe
    if not os.path.isfile(input_file):
        print(f"Erro: O arquivo {input_file} não foi encontrado.")
        return

    try:
        # Carregar o CSV para um DataFrame SEM modificar os tipos
        df = pd.read_csv(input_file, sep=';', dtype=str)

        # Remover o sufixo ".03" da coluna "Referencia"
        df['Referencia'] = df['Referencia'].apply(lambda x: str(x).removesuffix('.03') if isinstance(x, str) else x)

        # Salvar o arquivo corrigido mantendo os dados intactos
        df.to_csv(output_file, index=False, sep=';')

        print(f'Arquivo corrigido gerado: {output_file}')
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Caminhos dos arquivos
input_file = os.path.join('data', 'sua_planilha.csv')  # Caminho do arquivo de entrada
output_file = os.path.join('data', 'saida_corrigida.csv')  # Caminho do arquivo de saída

# Executar a função
corrigir_referencias(input_file, output_file)
