import random
import hangman_arts
from hangman_word_list import chosen_word

end_of_game = False

chosen_word = random.choice(chosen_word)
lives = 6
used_letters = []
word_lenght = len(chosen_word)

display = []
for letter in range(word_lenght):
  display += "_"

print(hangman_arts.logo)

while not end_of_game:
  
  guess = input("Adivinhe uma letra: ").lower()
  
  if guess not in used_letters:
    used_letters.append(guess)
    print (f'Você usou essas letras: {used_letters}')
  
    for position in range(word_lenght):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
        
    if guess not in chosen_word:
      lives -= 1
      print (f'A letra {guess} não está na palavra')
      if lives == 0:
         end_of_game = True
         print(f'Você perdeu, a palavra era {chosen_word}')
         print(f'Você usou essas letras: {used_letters}')
 
    print(hangman_arts.stages[lives])
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
      end_of_game = True
      print('Você ganhou!')
      print (f'Você usou essas letras: {used_letters}')
  
  else:
    print('Letra já usada')
    print (f'Você usou essas letras: {used_letters}')