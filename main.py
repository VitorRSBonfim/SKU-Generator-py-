
# Para realizar "operações" em um arquivo json é preciso utilizar 'import json'
import json
#Pegar json da solicitação do cliente
# Pegar Banco de dados separado de SKUs
# Criar SKU desejado pelo cliente, acima do id único +
# Verificar se o sku não existe no sistema
# Entregar SKU e adicionar SKU no sistema
print("Hello, Wolrd!!")

# Carregar json dos 10 últimos sku criados

# Teste arquivo JSON (Java Script Object Notation)

# Estrutura JSON SKU

# Criar SKC com base no id único SKC

# Estrutura SKC sc + 020525 + 0000000001 + 0000000001  
# Estrutura SKU 00000000014d42
# Adicionar 000 ao id, se o ID for 1 adicionar 9 zeros ao início do ID ID deverá ser adicionado na criação do SKC em uma linha separada de forma que seja possível comparar o ID recém criado com o id original (sem adição dos 0)
#                                                            baseado no id (comparação)
#                                                                  SKC inteiro para confirmação com os dados separados
                                                                                  #Deve ser único
                                                                                           #Irrelevante  
#Modelo DB ----> id | nome | dt de criação | token criador | sku | skc | skc_ini | id skc | id cor | id variação produtos |

# Etapas verificação / Criação.
# Verificiação disponibilidade 


# Conectando ao banco de dados MYSQL

import mysql.connector

# caminho db

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="catalogoProdutos"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM allProducts")

myresult = mycursor.fetchall()
a = 0
for a in myresult:
  print(a[5])

# Criando SKU

# Utilizando 

sku_JSON = '{"id" : id, id_comparador : id_comparador ,nome : "nome", dt_cr : dt_cr, token_cr : "token_cr", }'

x = '{"marca" : "nissan"}'

y = json.loads(x)

print("A marca é " + y["marca"])
