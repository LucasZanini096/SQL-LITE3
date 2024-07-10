import os
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
BD_NAME = 'db.sqlite3'
BD_FILE = ROOT_DIR / BD_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(BD_FILE)
cursor = connection.cursor() #O cursor que vai selecionar os dados dentro da base de dados, podendo manipular eles (criar, modificar ou deletar)

# CROUD -> Create  Read    Update   Delete
# SQL ->   INSERT  SELECT  UPDATE   DELETE

#CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
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

if __name__ == '__main__':
    print(sql)

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = "3"') #Deletando uma linha
    connection.commit()
    cursor.execute(f'UPDATE {TABLE_NAME} SET name="QUALQUER", weight=87.9 WHERE id = "1"')  #Fazendo a atualiação dos dados de uma linha da tabela
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()