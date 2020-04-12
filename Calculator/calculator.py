print('\nWelcome to Simple Calculator\n')

import time
time.sleep(1)
answer = ''
while True:

    try:
        s = input('You can do:\naddition \nsubtraction \nmultiplication \ndivision \ninteger division \nmodulus \nand exponent.\nType quit to end the program. \nType answer to use previous answer as one of the numbers\n')

        if s == 'addition':
            num1 = input('What is the the first number?\n')
            num2 = input('What is the second number?\n')
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) + float(num2)))
            print('The sum is ' + answer + '\n')
            time.sleep(2)

        elif s == 'subtraction':
            num1 = input('What is the the minuend?\n')
            num2 = input('What is the subtrahend?\n')
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) - float(num2)))
            print('The difference is ' + answer + '\n')
            time.sleep(2)

        elif s == 'multiplication':
            num1 = input('What is the the first number?\n')
            num2 = input('What is the second number?\n')
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) * float(num2)))
            print('The product is ' + answer + '\n')
            time.sleep(2)

        elif s == 'division':
            num1 = float(input('What is the the dividend?\n'))
            num2 = float(input('What is the divsor?\n'))
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) / float(num2)))
            print('The quotient is ' + answer + '\n')
            time.sleep(2)

        elif s == 'integer division':
            num1 = input('What is the the dividend?\n')
            num2 = input('What is the divsor?\n')
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) // float(num2)))
            print('The quotient is ' + answer + '\n')
            time.sleep(2)

        elif s == 'modulus':
            num1 = input('What is the the dividend?\n')
            num2 = input('What is the divsor?\n')
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) % float(num2)))
            print('The remainder is ' + answer + '\n')
            time.sleep(2)

        elif s == 'exponent':
            num1 = input('What is the the base?\n')
            num2 = input('What is the power?\n')
            if num1 == 'answer':
                num1 = float(answer)
            if num2 == 'answer':
                num2 = float(answer)
            answer = (str(float(num1) ** float(num2)))
            print('The answer is ' + answer + '\n')
            time.sleep(2)

        elif s == 'quit':
            print('\n\nSee you next time!')
            time.sleep(3)
            break

        else:
            print('\nERROR: Unkown operator')
            time.sleep(2)

    except ValueError:
            print('\nERROR: Numbers only\n')
            time.sleep(2)

    except ZeroDivisionError:
            print('\nERROR: No dividing by zero\n')
            time.sleep(2)
