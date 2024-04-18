# Enter your height in meters e.g., 1.55
height = float(input('Digite sua altura em metros: '))
# Enter your weight in kilograms e.g., 72
weight = int(input('Digite seu peso em Kg: '))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_int = int(weight)
height_float = float(height)

bmi = weight_int / height_float ** 2

if bmi < 18.5:
  print(f'Seu IMC é {bmi:.2f}, você está abaixo do peso.')
elif bmi < 25:
  print(f'Seu IMC é {bmi:.2f}, você está no peso ideal.')
elif bmi < 30:
  print(f'Seu IMC é {bmi:.2f}, você está um pouco acima do peso.')
elif bmi < 35:
  print(f'Seu IMC é {bmi:.2f}, você está obeso.')
else:
  print(f'Seu IMC é {bmi:.2f}, você está clinicamente obeso.')