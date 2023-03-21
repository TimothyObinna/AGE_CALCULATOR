Current_year = 2023 #Global variable
Average_age = 18 #Global varable

def age_cal():
    Name = str(input('enter your name: '))
    age_calculation = int(input('enter year of birth: '))
    final_age = Current_year - age_calculation
    if age_calculation < 2006:
        print('Hello', Name, 'you are', final_age, 'years old')
    else:
        print('Sorry', Name,'you are', final_age, 'years old, expected age is 18 years and above.')

age_cal()