import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
pokedex.close()
moves = open("./moves.json")
datatwo = json.load(moves)
moves.close()

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# def names(pokemon_data):
#      for pokemon in pokemon_data:
#          print(pokemon["name"]["english"])
# names(data)
#Add a language choice feature and print the pokemons name based on the user input
language = input("Input a language (English, Chinese, Japanese or French): ")
for pokemon in data:
    print(pokemon["name"][language])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

def search_by_type(pokedata):
    search = input("Input a type: ").strip().capitalize()
    match = []
    for p in pokedata:
        if "type" in p:
            if search in p["type"]:
                match.append(p)
    if match:
        for pokemon in match:
            print(pokemon["name"][language])
    else:
        print("No pokemon were found")
    return match
    
search_by_type(data)
          
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.

def search_by_name(pokedata):
    search = input("Input the name of a pokemon: ").strip().capitalize()
    match = []
    for p in pokedata:
        name = p["name"][language].lower()
        if search in name:
            match.append(p)
    if match:
        for pokemon in match:
            print(pokemon["name"][language])
        else:
            print("No pokemon were found")
        return match
search_by_name(data)

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!xxxxxxx

def search_by_type(pokedata):
    search = input("Input a pokemon to find their type: ").strip().capitalize()
    match = []
    for p in pokedata:
        type = p["type"]
        if search in type:
            match.append(p)
    if match:
        for pokemon in match:
            print(pokemon["type"])
        else:
            print("No pokemon were found")
        return match

search_by_type(data)
