weight = int(input())
height = float(input())
bmi = weight / float(height * height)
if bmi < 18.5:
    print('Underweight')
if bmi >= 18.5 and bmi < 25:
    print('Normal')
if bmi >= 25 and bmi < 30:
    print('Overweight')
if bmi > 30:
    print('Obesity')
