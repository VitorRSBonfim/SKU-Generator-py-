import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="catalogoProdutos"
)

select_query = mydb.cursor()

select_query.execute("SELECT * FROM allProducts")

result = select_query.fetchall()




