#100 days of coding - Day 1 (String, variables, concatenation, input, print))

#executa primeiro o input e depois o print
print('Bem vindo ' + input('Qual seu nome? ') + ' ao gerador de nome de pet')

#solicita o input de um nome
nome1 = input('Nome do seu personagem favorito: ')

#solicita o input de um outro nome
nome2 = input('Nome de um elemento químico: ')

#Print nome1 e nome2 em linhas diferentes em uma mesma função print()
print(f'{nome1}\n{nome2}')

#Print nome1 e nome2 usando f'' string
print(f'O nome do seu pet pode ser {nome1} {nome2}')