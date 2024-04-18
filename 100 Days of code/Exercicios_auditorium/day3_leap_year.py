# Input do ano
year = int(input('Digite um ano:\n'))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"O ano {year} é bissexto!")
    else:
      print(f"O ano {year} não é bissexto!")
  else:
    print(f"O ano {year} é bissexto!")
else:
  print(f"O ano {year} não é bissexto!")