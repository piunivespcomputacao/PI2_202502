import pandas as pd
import os
import django
import sys

# Adicione o caminho do projeto para o Python
# Isso permite que o script encontre as configurações do Django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configura as variáveis de ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Importa o modelo Compressor após o setup do Django

# ... código de setup do Django (os.environ.setdefault, django.setup()) ...

from qualidade.models import Compressor

csv_file_path = 'data/data.csv' 

# Nomes de colunas a serem usadas (devem coincidir com seu models.py)
COLUNAS_PARA_USAR = [
    'id', 'rpm', 'motor_power', 'outlet_pressure_bar', 'air_flow', 
    'noise_db', 'outlet_temp', 'gaccx', 'gaccy', 'gaccz', 
    'haccx', 'haccy', 'haccz', 'exvalve', 'acmotor'
]

# 1. Lê o arquivo CSV usando pandas
try:
    # Use o parâmetro 'usecols' para ler apenas as colunas que você quer
    # Por conta do erro 'ï»¿id', precisamos ler todas e renomear primeiro.
    df = pd.read_csv(csv_file_path, encoding='latin-1')
    print("Dataset lido com sucesso.")
    
    # CORREÇÃO CRÍTICA: Renomear a coluna 'id'
    df.rename(columns={'ï»¿id': 'id'}, inplace=True) 
    
    # Filtra o DataFrame para ter apenas as colunas que você quer
    df = df[COLUNAS_PARA_USAR]
    
except FileNotFoundError:
    print(f"Erro: O arquivo '{csv_file_path}' não foi encontrado.")
    exit()
except KeyError as e:
    print(f"Erro: Uma coluna essencial {e} não foi encontrada. Verifique se o nome está correto no CSV.")
    exit()


# 2. Popula o banco de dados
for index, row in df.iterrows():
    
    # TRADUÇÃO: Converte 'clean/dirty' para 1/0 e 'stable/unstable' para 1/0
    # Certifique-se que o texto no CSV (row['exvalve']) é minúsculo ou use .lower()
    
    exvalve_value = 1 if str(row['exvalve']).lower() == 'clean' else 0
    acmotor_value = 1 if str(row['acmotor']).lower() == 'stable' else 0
    
    try:
        # Cria um objeto Compressor para cada linha do Dataframe
        compressor = Compressor(
            id=row['id'],
            rpm=row['rpm'],
            motor_power=row['motor_power'],
            outlet_pressure_bar=row['outlet_pressure_bar'],
            air_flow=row['air_flow'],
            noise_db=row['noise_db'],
            outlet_temp=row['outlet_temp'],
            gaccx=row['gaccx'],
            gaccy=row['gaccy'],
            gaccz=row['gaccz'],
            haccx=row['haccx'],
            haccy=row['haccy'],
            haccz=row['haccz'],
            exvalve=exvalve_value, 
            acmotor=acmotor_value, 
            # status_qualidade e diagnostico usam o valor default do models.py
        )

        # 3. Salva o objeto no banco de dados
        compressor.save()
        print(f"Compressor ID {row['id']} salvo no banco de dados.")

    except Exception as e:
        print(f"Ocorreu um erro ao salvar o compressor {row['id']}: {e}")
        break

print("Importação de dados concluída!")