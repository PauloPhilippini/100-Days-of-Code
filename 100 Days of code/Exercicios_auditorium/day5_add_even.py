'''You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.'''

target = int(input('Digite um número entre 0 e 1000:')) # Enter a number between 0 and 1000

even_total = 0
for number in range(0, target + 1, 2):
  even_total += number 
print(f'{even_total}')

even_total_alt = 0
for number in range(0, target + 1):
  if number % 2 == 0:
    even_total_alt += number
print(f'{even_total}')