import pandas as pd
import json


data = './files/data.xlsx'

df = pd.read_excel(data, dtype=str, na_values='')
df = df.where(pd.notnull(df), '')
df['Nome'] = df['Nome'].str.upper()
df['CPF'] = df['CPF'].replace(r'[^0-9\s]', '', regex=True)
df['Período'] = df['Período'].replace(r'[^0-9\s]', '', regex=True)
df['Matrícula'] = df['Matrícula'].replace(r'[^0-9\s]', '', regex=True)
df['Título'] = df['Título'].replace(r'[^0-9\s]', '', regex=True)
df['Endereco_CEP'] = df['Endereco_CEP'].astype(str)

json_data = df.apply(
    lambda row: {
    'nome': row['Nome'],
    'cpf': row['CPF'],
    'endereco': {
        'logradouro': row['Endereco_logradouro'],
        'numero': row['Endereco_num'],
        'bairro': row['Endereco_bairro'],
        'complemento': row['Endereco_complemento'],
        'cidade': row['Endereco_cidade'],
        'uf': row['Endereco_UF'],
        'cep': row['Endereco_CEP']
    },
    'email': row['Email'],
    'celular': row['Celular'],
    'instituicao': row['Instituição de Ensino'],
    'periodo': row['Período'],
    'matricula': row['Matrícula'],
    'título': row['Título']
    },
    axis=1
).tolist()

with open('./files/data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)