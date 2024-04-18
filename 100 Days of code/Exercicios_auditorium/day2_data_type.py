'''Instructions Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8'''

two_digit_number = input('Digite um numero com 2 digitos: ')


first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

sum_digit = first_digit + second_digit
first_digit_str = str(first_digit)
second_digit_str = str(second_digit)
sum_digit_str = str(sum_digit)

print('A soma de ' + first_digit_str + ' + ' + second_digit_str + ' = ' + sum_digit_str)