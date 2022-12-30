b_salary = int(input("Enter your basic salary: "))

if b_salary <= 1500:
    Net_Salary = (b_salary * 0.1) + b_salary
    print('Your Net Salary is USD ', Net_Salary)
elif b_salary > 1500 and b_salary <= 2500:
    Net_Salary = (b_salary * 0.15) + b_salary
    print('Your Net Salary is USD ', Net_Salary)
elif b_salary > 2500:
    Net_Salary = (b_salary * 0.2) + b_salary
    print('Your Net Salary is USD ', Net_Salary)
else:
    print("Please enter your accurate amount")
