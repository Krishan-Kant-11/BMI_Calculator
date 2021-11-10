a = input('- Weight(in Kilogram) : ')              # Inputs start here.
b = input('- Height(in Meters) : ')

bmi = float(a)/float(b)**2                         # BMI formula.


if bmi < 18.5:                                     # BMI conditions.
    print('- You are Underweight.')
elif 18.5 < bmi < 24.9:
    print('- You are Normal.')
elif 25 < bmi < 29.9:
    print('- You are Overweight.')
elif 30 < bmi:
    print('- You are obese.')

print('- Your BMI is ', bmi , ".")                  # End result.


