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
cursor.execute(''  # insere um valor na base de dados
               f'Insert into {TABLE_NAME}' 
               '(id, name, weight) '
               'VALUES '
               '(NULL, "Lucas Zanini", 19.8), (NULL, "Ivan Ferreira", 20.8)')
#cursor.executemany('')

cursor.close() #Fechando o cursor
connection.close() #Fechando a conexão

