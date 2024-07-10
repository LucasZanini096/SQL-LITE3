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
        '(?,  ?)' # ? -> binding
)
cursor.execute(sql, ['Lucas', 4])
#Estou mandando um comando e os valores referente a esse comando, algo que evita o sql injection
#Não estou declarando valores no comando
connection.commit()
#cursor.executemany('')

cursor.close() #Fechando o cursor
connection.close() #Fechando a conexão

