import sqlite3
from main import BD_FILE, TABLE_NAME


connection = sqlite3.connect(BD_FILE)
cursor = connection.cursor() #O cursor que vai selecionar os dados dentro da base de dados, podendo manipular eles (criar, modificar ou deletar)

cursor.execute(f'SELECT * FROM {TABLE_NAME}') #Fazendo uma consulta nos dados do banco de dados

for row in cursor.fetchall(): #featchall -> obtém todos os dados que estão inseridos na tabela
    _id, name, weight = row
    print(f'ID: {_id}, Name: {name}, Weight: {weight}')

print()
cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "3"')
row = cursor.fetchone()
_id, name, weight = row
print(f'ID: {_id}, Name: {name}, Weight: {weight}')


cursor.close() #Fechando o cursor
connection.close() #Fechando a conexão