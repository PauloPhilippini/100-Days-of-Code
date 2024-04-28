logo = '''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1,numero2):
    return numero1 - numero2

def divide(numero1, numero2):
    return numero1 / numero2

def multiplicate(numero1,numero2):
    return numero1 * numero2

operators_symbol = {
"+": somar,
"-": subtrair,
"*": multiplicate,
"/": divide
}
def calculator():
    n1 = float(input('Digite o primeiro numero: '))
    for operators in operators_symbol:
        print(operators)
    should_continue = True
    while should_continue:
        selected_operation = input("Selecione uma operação: ")
        n2 = float(input('Digite o próximo numero: '))
        calculation_function = operators_symbol[selected_operation]
        answer = calculation_function(n1, n2)
        print(f'{n1} {selected_operation} {n2} = {answer}')

        if input(f'Digite S para continuar com {answer} ou N para iniciar um novo cálculo: ').lower() == 's':
            n1 = answer
        else:
            should_continue = False
            calculator()

     
calculator()