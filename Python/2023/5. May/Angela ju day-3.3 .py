# ANGELA JU DAY-3 , VIDEO NUMBER 3.5 DATE-31-MAY-2023

weight = float (input('Enter your weight in kg: ')) 
height = float (input('Enter your height in metar: '))
bmi = round(weight / height **2 , 2 )
print (bmi)

# oppsens
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are Under weight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, have a Normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are Over weight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are Obese")
else:
    print(f"Your bmi is {bmi}, you are Clinically obese")
    
# ANGELA JU DAY-3 , VIDEO NUMBER 3.5 DATE-31-MAY-2023