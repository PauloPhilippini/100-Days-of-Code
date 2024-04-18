#100 days of coding - Day 2 (Data type)

#string 
print ('Hello'[0])
print ('Hello'[-1])
print("-=" * 30)

#integer
var1 = 10
var2 = 30
print (var1 + var2)
print (var1 * var2)
print (var1 / var2)
print (round(var1 / var2, 2))
print (var1 - var2)
print("-=" * 30)

#float
var1 = 8.33
var2 = 100.03
print (var1 + var2)
print (var1 * var2)
print (round(var1 * var2, 2))
print (var1 / var2)
print (round(var1 / var2, 3))
print (round(var1 // var2, 3))
print (var1 - var2)
print("-=" * 30)

#boolean
var1 = True
var2 = False
print(var1, var2)
print("-=" * 30)

#string conversion
num_char = len(input('What is your name:\n'))
new_num_char = str(num_char)
print('Your name has ' + new_num_char + ' characters')
print("-=" * 30)