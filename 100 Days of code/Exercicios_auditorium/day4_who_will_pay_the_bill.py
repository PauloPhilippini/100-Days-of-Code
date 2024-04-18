import random

person_name = ['Paulo', 'Fabio', 'Rafael', 'Guilherme', 'Gilmarqueson', 'Gabriel', 'Manuel', 'Josuel', 'Emanuel']
#person1 = input("Enter the name of the first person: ")
#person2 = input("Enter the name of the second person: ")
#person3 = input("Enter the name of the third person: ")

#person_name.append(person1)
#person_name.append(person2)
#person_name.append(person3)

names = person_name

num_items = len(names)

random_choice = random.randint(0, num_items - 1) #ultima posição -1 já que a lista começa do 0 pega um numero
person_pay = names[random_choice] #joga o numero gerado como posição da lista ex: names[4]


print(f'{person_pay} vai pagar o rango hoje!')