import mysql.connector as Connection

connection = Connection.connect(host = "localhost",port= 3306,user = "root",password = "@#Aryan7645",database = "flipkart")
cursor = connection.cursor()



# cursor.close()
# connection.close()