import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

tabela = {
    'Data': [],
    'Hora': [],
    'Arquivo de áudio': [],
    'Tempo do Áudio': [],
    'CPF Operador': [],
    'Nome do Operador': [],
    'Tabulação': [],
    'Origem': [],
    'Tipo': [],
    'Telefone': [],
    'Contrato': [],
    'Assessoria': [],    
}


df = pd.DataFrame(tabela)


caminho_arquivo_excel = os.getenv("CAMINHO_EXCEL_CRIAR_DATAFRAME")

# Salvando o DataFrame em um arquivo Excel
try:
    df.to_excel(caminho_arquivo_excel, index=False, engine='openpyxl')
    print('Tabela criada e salva com sucesso em Excel!')
except Exception as e:
    print(f"Erro ao salvar o arquivo Excel: {e}")

print(df)