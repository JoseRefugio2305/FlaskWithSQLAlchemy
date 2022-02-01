from dotenv import load_dotenv
import os

load_dotenv()

user=os.environ['MYSQL_USER']
password=os.environ['MYSQL_PASS']
host=os.environ['MYSQL_HOST']
bdd=os.environ['MYSQL_BDD']

DATABASE_CONNECTION_URI=f'mysql://{user}:{password}@{host}/{bdd}'

print(DATABASE_CONNECTION_URI)