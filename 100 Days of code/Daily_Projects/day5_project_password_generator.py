#Gerador de senha
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Gerador de senha!")
nr_letters= int(input("Quantas letras deseja que sua senha tenha?\n")) 
nr_symbols = int(input(f"Quantas símbolos deseja que sua senha tenha??\n"))
nr_numbers = int(input(f"Quantas números deseja que sua senha tenha??\n"))

password = ""

for letter in range(1, nr_letters + 1):
  password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
#Adicionando valores a lista
for letter in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list) #randomizando a lista
print(password_list)

#nova variavel que vai receber a senha
new_password = "" 

#extraindo os valores para dentro da nova variavel
for value in password_list:
  new_password += value

print(f"Sua senha é: {new_password}")