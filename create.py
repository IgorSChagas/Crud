# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Semke@140499",
    database="teste"
)

cursor = connection.cursor() ##

sql = "INSERT INTO users (name, email, created) VALUES(%s, %s, %s)" ## Query de INSERT
data = ( ## Dados que vou inserir
    'Segundo Usuário',
    'segundosuario@teste.com.br',
    datetime.datetime.today()
)

cursor.execute(sql, data) ## Executar a query 
connection.commit() ## Efetivar a query

userid = cursor.lastrowid ## Recupera o ID da última linha

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID: ", userid)