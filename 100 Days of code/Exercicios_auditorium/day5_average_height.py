'''
Instructions
You are going to write a program that calculates the average student height from a List of heights.
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

'''

# Lista da altura dos estudantes
student_heights = [156, 178, 165, 171, 187]

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

number_students_counter = 0
total_sum_height = 0

for student in student_heights:
  number_students_counter +=1

for height in student_heights:
  total_sum_height += height

average_height = round(total_sum_height / number_students_counter)

print(f'Altura total = {total_sum_height}')
print(f'Número de estudantes = {number_students_counter}')
print(f'Mediana da altura = {average_height}')