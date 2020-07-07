height = float(input("Please enter your height in meters:"))
weight = int(input("Please enter your weight in kg: "))

BMI = weight / (height **2)
print("Your BMI is: " , int(BMI))

if BMI > 40:
    print('Obese Class III (Very severely obese)')
elif BMI  >= 35:
    print('Obese Class II (Severely obese)')
elif BMI  >= 30:
    print('Obese Class I (Moderately obese)')
elif BMI  >= 25:
    print('Overweight')
elif BMI  >= 18.5:
    print('Normal (healthy weight)')
else:
    print('Underweight')

