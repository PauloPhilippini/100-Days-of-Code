import math

def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width) / cover)
  print(f'Você vai precisar de {number_of_cans} latas de tinta.')

test_h = int(input('Altura da parede em metros: ')) 
test_w = int(input('Largura da parede em metros: ')) 
coverage = int(input('Quantos m2 uma lata de tinta pinta: ')) 
paint_calc(height=test_h, width=test_w, cover=coverage)
