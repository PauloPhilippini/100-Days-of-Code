typed_number = int(input('Digite um numero: '))

def check_prime_number(number):
    is_prime = True
    if number <= 1:
        print('Número não é primo')
        return
    for i in range (2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print('Numéro primo')
    else:
        print('Não é primo')

check_prime_number(number = typed_number)



    