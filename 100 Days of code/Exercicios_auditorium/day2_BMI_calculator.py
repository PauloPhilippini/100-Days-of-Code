# 1st input: enter height in meters e.g: 1.65
height = 1.65
# 2nd input: enter weight in kilograms e.g: 72
weight = 72
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_int = int(weight)
height_float = float(height)

bmi = weight_int / height_float ** 2
bmi_int = int(bmi)

print(bmi_int)