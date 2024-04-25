programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}
# imprimindo um item do dicionário
#print(programming_dictionary["Bug"])

#adicionando um item ao dicionário
programming_dictionary["Gambiarra"] = 'Se funcionou é o que importa'
#print(programming_dictionary)

#dicionario vazio 
#empty_dic = {}

#apagando um dicionario
#programming_dictionary = {}
#print(programming_dictionary)

#loop dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

for key, value in programming_dictionary.items():
  print(key)
  print(value)
  print(key, value)

#nested dictionary
capitals = {
  'Brasil' : 'Brasilia',
  'France' : 'Paris'
}

travel_log = {
  {'Country': 'Brasil', 'cities_visited': ['Brasilia', 'Rio de Janeiro', 'Sao Paulo'], 'times_visited': 12},
  {'Country': 'France', 'cities_visited': ['Paris', 'Lille', 'Dijon'], 'times_visited': 5},  
}

#nesting a dictionary in a list
travel_log = [
  {
    'Country': 'Brasil', 
    'cities_visited': ['Brasilia', 'Rio de Janeiro', 'Sao Paulo'], 
    'times_visited': 12
  },
  {
    'Country': 'France', 
    'cities_visited': ['Paris', 'Lille', 'Dijon'], 
    'times_visited': 5
  },  
]