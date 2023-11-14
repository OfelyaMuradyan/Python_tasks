def calculator():
    operation = input('''
    Choose an operation you want to complete.
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return 'error'
    else:
        return "Invalid input"
 

print(calculator())

t = True
while t:
    choice = input('Do you want to continue?(yes/no):')
    if choice == 'yes':
        print(calculator())
    else:
        print('Bye')
        t = False