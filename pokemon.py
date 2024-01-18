import requests
import mysql.connector

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
pokemon_list = response.json()['results']

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pokemon_list"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE pokemon (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), weight INT, height INT)")

for pokemon in pokemon_list:
    response = requests.get(pokemon['url'])
    pokemon_data = response.json()
    name = pokemon_data['name']
    weight = pokemon_data['weight']
    height = pokemon_data['height']
    sql = "INSERT INTO pokemon (name, weight, height) VALUES (%s, %s, %s)"
    val = (name, weight, height)
    mycursor.execute(sql, val)

mydb.commit()

mydb.close()
