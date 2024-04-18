print("Bem vindo a Python Pizza Deliveries!")
print('''Menu
Pizza Pequena: R$ 15,00
Pizza Média: R$ 20,00
Pizza Grande: R$ 25,00
Peperoni extra(P): R$ 2,00
Peperoni extra(M,G): R$ 3,00
Queijo extra: R$ 1,00
''')
size = input('Qual o tamanho da Pizza: P, M ou G?\n') 
add_pepperoni = input('Você quer peperoni? S ou N?\n') 
extra_cheese = input('Você quer queijo extra? S ou N?\n') 
valor = 0

if size == 'P':
   valor += 15
elif size == 'M':
   valor += 20
else:
   valor += 25

if add_pepperoni == 'S':
  if size == 'P':
    valor += 2
  else:
    valor += 3

if extra_cheese == 'S':
  valor += 1

print(f'Sua pizza ficou: R${valor}.')