import re
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_database = os.getenv('DB_DATABASE')
mydb = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_pass,
  database=db_database
)

names=list()
a='A2 | AlbertLin - Albert'
b='A1 | Uyud - Yudha'

a_new = tuple(re.split('\| |-',a))
b_new = tuple(re.split('\| |-',b))
print(a_new)
print(b_new)

names.append(a_new)
names.append(b_new)

print(names)