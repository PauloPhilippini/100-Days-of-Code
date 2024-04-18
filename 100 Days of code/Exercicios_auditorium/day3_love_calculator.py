print("A calculadora vai checar sua compatibilidade...")
name1 = input('Digite o primeiro nome: ') 
name2 = input('Digite o segundo nome: ') 

combine_name = name1 + name2

lovers_name = combine_name.lower()

a = lovers_name.count('a')
m = lovers_name.count('m')
o = lovers_name.count('o')
r = lovers_name.count('r')
first_digit = a + m + o + r

v = lovers_name.count('v')
e = lovers_name.count('e')
r = lovers_name.count('r')
d = lovers_name.count('d')
a = lovers_name.count('a')
d2 = lovers_name.count('d')
e2 = lovers_name.count('e')
i = lovers_name.count('i')
r2 = lovers_name.count('r')
o = lovers_name.count('o')

second_digit = v + e + r + d + a + d2 + e2 + i + r2 + o

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score > 40 and love_score < 50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'Your score is {love_score}.')
