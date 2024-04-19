#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print("-=-"* 30)
print('Bem vindo a calculadora de gorjetas!')
print("-=-"* 30)
valor_conta = float(input("Qual o valor da conta?\n"))
nro_pessoas = int(input("Quantas pessoas vão dividir a conta?\n"))
porcentagem_gorjeta = int(input("Qual a porcentagem de gorjeta 10%, 12% ou 15%?\n"))
valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100) 
valor_gorjeta_individual = valor_gorjeta / nro_pessoas
valor_individual = (valor_conta + valor_gorjeta) / nro_pessoas

print(f'O valor da gorjeta para cada um é R${valor_gorjeta_individual:.2f}. Cada pessoa deve pagar R${valor_individual:.2f}')