prev_r = int(input('What is your Previous Meter Reading? '))
pres_r = int(input('What is your PresentMeter Reading? '))
unit = pres_r - prev_r

if unit <= 30:
    print('Your Bill is 50 USD')
elif unit <= 90:
    print('Your Bill is 75 USD')
elif unit > 90:
    print('Your Bill is 100 USD')
else:
    print('Invalid Meter Reading')
