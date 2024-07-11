# Instalar  Mysql y el installer 
# pip install mysql
# pip install mysql-connector 
        # Si no funciona 

# pip install mysql-connector-python


import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql@123'

)

#Preparar el cursor 

cursorObject = database.cursor()


#Crear la base de datos 
cursorObject.execute('CREATE DATABASE dbEla')

print('All done')

