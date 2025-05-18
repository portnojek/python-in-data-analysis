# slownik pythona
df = pd.DataFrame(data)

#lista slownikow
data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
df = pd.DataFrame(data)

#csv
df = pd.read_csv('plik.csv')

#excel
df = pd.read_excel('plik.xlsx')

#json
df = pd.read_json('plik.json')
# lub
import json
data = json.loads(json_string)
df = pd.DataFrame(data)

#baza danych SQL
import sqlite3
conn = sqlite3.connect('baza.db')
df = pd.read_sql_query('SELECT * FROM tabela', conn)

#lista wartosci
df = pd.DataFrame([1, 2, 3], columns=['liczba'])

#dane z API
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
df = pd.DataFrame(data)