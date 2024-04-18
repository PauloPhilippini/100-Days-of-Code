'''Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x'''


student_scores = [5,10,6,8,9,10,11,12,25,39,15,47,17,100,19]

for score in range(0, len(student_scores)):
  student_scores[score] = int(student_scores[score])

high_score = min_score = student_scores[0]

for score in student_scores:
    if score > high_score:
        high_score = score
    if score < min_score:
        min_score = score

print (f'The highest score in the class is: {high_score}')
print (f'The lowest score in the class is: {min_score}')
