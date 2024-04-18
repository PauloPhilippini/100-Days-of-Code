print("Bem vindo a montanha russa! Para andar nesse brinquedo você deve ter mais que 120cm de altura e menos de 180cm")
print('''
Tabela de preços:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Até 12 anos: R$5
Acima de 12 até 18 anos: R$7
Acima de 18 anos: R$12
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')
height = int(input("Qual sua altura em cm?\n"))
age = int(input('Qual sua idade?\n'))

if height >= 120 and height <= 180:
  print("Você pode andar na montanha russa!")
  if age >= 18:
    print("Você deve pagar R$12,00")
  elif age >= 12 and age <= 17:
    print("Você deve pagar R$7,00")
  else:
    print('Você deve pagar R$5,00')
elif height > 181:
  print("Você é muito alto para andar na montanha russa!")
else:
  print("Você não tem a altura necessária para andar na montanha russa.")
