Name = str(input('Enter Your Name: '))
Marks_List = list(map(int, input(
    'Enter your all 3 subjects Marks (Space-Seperated): ').strip().split()))
total = sum(Marks_List)
average = int(total / 3)

if average >= 75:
    print('\nYou Got A')
elif average <= 74 and average >= 60:
    print('\nYou Got B')
elif average <= 59 and average >= 50:
    print('\nYou Got C')
elif average <= 49 and average >= 40:
    print('\nYou Got S')
else:
    print('\nYou Got F')
