# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Olá")
  print("Como está?")
  print('Escrevi e sai correndo...')

def greet_with_name(name):
  print(f"Olá {name}")
  print(f'Como está {name}?')
  print(f'Escrevi e sai correndo {name}...')

def multiple_parameter(name, location):
  print (f'Me chamo {name} e moro em {location}')
  
  
greet()
greet_with_name("Paulo")
multiple_parameter(name = 'Paulo', location = 'Recife')
