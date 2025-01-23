number1 = int(input('enter your first number: '))
number2 = int(input('enter your second number(enter 0 if no second number): '))
chose_operations = int(input('''enter operation you want 
                            '1' for check even
                            '2' for addition
                            '3' for subtraction
                            '4' for multiplication
                            '5' for divistion
                             '''))
if chose_operations == 1 :
    if number1%2 == 0:
        print(f"number {number1} is even")
    else:
        print('the number',number1,'is not even')
elif chose_operations == 2 :
    sum1 = number1+number2
    print(sum1)
elif chose_operations == 3:
    subtraction1 = number1 - number2
    print(subtraction1) 
elif chose_operations == 4:
    multiplication1 = number1*number2
    print(multiplication1)
elif chose_operations == 5:
    division1 = number1/number2
    print(division1)