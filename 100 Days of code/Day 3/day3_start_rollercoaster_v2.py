print("Bem vindo a montanha russa! Para andar nesse brinquedo você deve ter mais que 120cm")
print('''
Tabela de preços:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Até 12 anos: R$5
Acima de 12 até 18 anos: R$7
Acima de 18 anos: R$12
Foto de recordação: R$3
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')
height = int(input("Qual sua altura em cm?\n"))
valor = 0

if height >= 120:
  print("Você pode andar na montanha russa!")
  age = int(input('Qual sua idade?\n'))
  if age < 12:
    valor = 5
    print("Ticket Criança R$5,00")
  elif age <= 18:
    valor = 7
    print("Ticket Adolescente R$7,00")
  elif age >= 45 and age <= 55:
    print("Você pode entrar grátis!")
  else:
    valor = 12
    print('Ticket Adulto R$5,00')
  
  recordacao = input('Você quer uma foto para recordação? S ou N\n')
  if recordacao in 'Ss':
    valor +=3
  else:
    valor +=0

  print(f'O valor total é de R${valor:.2F}')

else:
  print("Você não tem a altura necessária para andar na montanha russa.")
