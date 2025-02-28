import pandas as pd
import os
from tkinter import filedialog, Tk, messagebox

# Função para corrigir as referências
def corrigir_referencias(input_file, output_file, file_type):
    # Verificar se o arquivo de entrada existe
    if not os.path.isfile(input_file):
        print(f"Erro: O arquivo {input_file} não foi encontrado.")
        return

    try:
        # Carregar o arquivo de entrada
        df = pd.read_csv(input_file, sep=';', dtype=str)

        # Remover o sufixo ".03" da coluna "Referencia"
        df['Referencia'] = df['Referencia'].apply(lambda x: str(x).removesuffix('.03') if isinstance(x, str) else x)

        # Salvar o arquivo corrigido de acordo com o tipo escolhido
        if file_type == 'csv':
            df.to_csv(output_file, index=False, sep=';', lineterminator='\n')
        elif file_type == 'txt':
            df.to_csv(output_file, index=False, sep=';', lineterminator='\n', header=False)

        print(f'Arquivo corrigido gerado: {output_file}')
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Caminhos dos arquivos
root = Tk()
root.withdraw()

input_file = filedialog.askopenfilename(title="Selecione o arquivo de entrada", filetypes=[("Arquivos CSV", "*.csv"), ("Arquivos TXT", "*.txt")])
output_file = filedialog.asksaveasfilename(title="Salvar arquivo corrigido como", defaultextension=".csv", filetypes=[("CSV", "*.csv"), ("TXT", "*.txt")])

file_type = 'csv' if output_file.endswith('.csv') else 'txt'

# Executar a função
corrigir_referencias(input_file, output_file, file_type)
