#Functions with outputs
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}" #output / function ends here
#replace where the function is called with the output
print(format_name('PAULO', 'RICARDO'))