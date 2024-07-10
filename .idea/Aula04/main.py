import os
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
BD_NAME = 'db.sqlite3'
BD_FILE = ROOT_DIR / BD_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(BD_FILE)
cursor = connection.cursor() #O cursor que vai selecionar os dados dentro da base de dados, podendo manipular eles (criar, modificar ou deletar)

#CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute( #Deleta a sequencia dos ID's na tabela
    f'DELETE FROM slqLite_sequence WHERE name="{TABLE_NAME}"'
)

connection.commit()

#Criando a tabela
cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,' #Atributo Id definido como a chave primária da tabela, sendo um tipo inteiro  
        'name TEXT,'
        'weight REAL'
        ')'
)
connection.commit()

#Registrar valores nas colunas da tabela
# CUIDADO: sql injection

sql = (
        f'Insert into {TABLE_NAME}' 
        '(name, weight) '
        'VALUES '
        '(:nome,  :peso)' # definido as chaves de um dicionário
)

cursor.execute(sql, {'nome': 'Lucas', 'peso': 68})
#Estou pegando um dicionário e os valores referente as chaves estão sendo inseridos na tabela
cursor.executemany(sql, (
    {'nome': 'Lucas', 'peso': 68},
    {'nome': 'Bruna', 'peso': 58},
    {'nome': 'Rogério', 'peso': 85},
    {'nome': 'Sophia', 'peso': 62},
))

connection.commit()


cursor.close() #Fechando o cursor
connection.close() #Fechando a conexão