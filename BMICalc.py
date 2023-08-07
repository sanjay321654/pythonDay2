height = float(input("what your height? "))
weight = float(input("what is your weight?"))
#bmi formula is weight divided by height square
bmi = round(weight / height**2)
# line alignments are very importany in if else elif conditions.
if bmi <18.5:
  print(f"your bmi is {bmi}, you are underweight. ")
elif bmi<25:
  print(f"your bmi is {bmi}, you are normal weight.")
elif bmi<35:
  print(f"your bmi is {bmi}, your are obese. ")
else:
  print(f"your bmi is {bmi}, your clinically obese.")
