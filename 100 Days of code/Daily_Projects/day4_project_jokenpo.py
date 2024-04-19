import random
'''
papel > pedra > tesoura > papel

'''

rodadas = 0
vitoria_jogador = 0
vitoria_computador = 0
jogadas = ['Pedra', 'Papel', 'Tesoura']

#Variaveis para desenhar as escolhas
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

print('Vamos jogar Jo-ken-po! Quem vencer três primeiro ganha!\n')


# enquanto não tiver 3 rodadas continua
while vitoria_jogador < 3 and vitoria_computador < 3: #trocar por while rodadas < 3: caso queira por rodadas
  
  computador = random.choice(jogadas).title()
  jogador = input('Sua jogada:\n').title()

  #Empate
  if jogador == 'Tesoura' and computador == 'Tesoura':
    print(tesoura)
    print(f'Computador jogou {computador}')
    print(tesoura)
    print('empate')
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
  
  elif jogador == 'Papel' and computador == 'Papel':
    print(papel)
    print(f'Computador jogou {computador}')
    print(papel)  
    print('empate')
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
  
  elif jogador == 'Pedra' and computador == 'Pedra':
    print(pedra)
    print(f'Computador jogou {computador}')
    print(pedra)
    print('Empate!')
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
  
  #Vitoria Jogador
  elif jogador == 'Pedra' and computador == 'Tesoura':
    print(pedra)
    print(f'Computador jogou {computador}')
    print(tesoura)
    print('Você ganhou')
    vitoria_jogador += 1
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
    
  elif jogador == 'Papel' and computador == 'Pedra':
    print(papel)
    print(f'Computador jogou {computador}')
    print(pedra)
    print('Você ganhou')
    vitoria_jogador += 1
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1

  elif jogador == 'Tesoura' and computador == 'Papel':
    print(tesoura)
    print(f'Computador jogou {computador}')
    print(papel)
    print('Você ganhou')
    vitoria_jogador += 1
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
  
  #Vitoria computador
  elif computador == 'Pedra' and jogador == 'Tesoura':
    print(tesoura)
    print(f'Computador jogou {computador}')
    print(pedra)
    print('Você perdeu')
    vitoria_computador += 1
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1

  elif computador == 'Papel' and jogador == 'Pedra':
    print(pedra)
    print(f'Computador jogou {computador}')
    print(papel)
    print('Você perdeu')
    vitoria_computador += 1
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
  
  elif computador == 'Tesoura' and jogador == 'Papel':
    print(papel)
    print(f'Computador jogou {computador}')
    print(tesoura)
    print('Você perdeu')
    vitoria_computador += 1
    print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
    rodadas +=1
  else:
    print('Jogada inválida')

if vitoria_jogador == 3:
  print(f'O resultado final foi {vitoria_jogador} X {vitoria_computador}. Você venceu!!')
else:
  print(f'O resultado final foi {vitoria_jogador} X {vitoria_computador}. Você perdeu!!')