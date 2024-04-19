import random
'''
papel > pedra > tesoura > papel

'''
rodadas = 0
vitoria_jogador = 0
vitoria_computador = 0

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
game_image = [pedra, papel, tesoura]
print('Vamos jogar Jo-ken-po! Quem vencer três primeiro ganha!\n')

# enquanto não tiver 3 rodadas continua
while vitoria_jogador < 3 and vitoria_computador < 3: #trocar por while rodadas < 3: caso queira por rodadas

  jogador = int(input("Qual sua escolha? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
  if jogador >= 3 or jogador < 0:
    print('Jogada Inválida')
  else:
    print(game_image[jogador])
  
    computador = random.randint(0, 2)
    print("O computador escolheu:")
    print(game_image[computador])
  
    if jogador == 0 and computador == 2:
      print("Você ganhou!")
      vitoria_jogador += 1
      print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
      rodadas +=1
    elif computador == 0 and jogador == 2:
      print("Você perdeu!")
      vitoria_computador += 1
      print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
      rodadas +=1
    elif computador > jogador:
      print("Você perdeu!")
      vitoria_computador += 1
      print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
      rodadas +=1
    elif jogador > computador:
      print("Você ganhou!")
      vitoria_jogador += 1
      print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
      rodadas +=1
    elif computador == jogador:
      print("Empate!")
      print(f'Placar: {vitoria_jogador} X {vitoria_computador}')
      rodadas +=1
      
if vitoria_jogador == 3:
  print(f'O resultado final foi {vitoria_jogador} X {vitoria_computador}. Você venceu!!')
else:
  print(f'O resultado final foi {vitoria_jogador} X {vitoria_computador}. Você perdeu!!')