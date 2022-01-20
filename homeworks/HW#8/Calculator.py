print('Zero as an operation sign '
      '\nwill terminate the program')
while True:
    s = input("Input '+','-','*','/': ")
    if s == '0':
        print('Exit the program')
        break
    if s in ('+', '-', '*', '/'):
        x = float(input('x= '))
        y = float(input('y= '))


        if s == '+':
            result = x + y
            print(f'result = {result}')
            with open('result.txt', 'a') as file:
                file.write(f'\nx = {x} \ny = {y} \nresult = {result} \n*************' )
        elif s == '-':
            result = x - y
            print(f'result = {result}')
            with open('result.txt', 'a') as file:
                file.write(f'\nx = {x} \ny = {y} \nresult = {result} \n*************')
        elif s == '*':
            result = x * y
            print(f'result = {result}')
            with open('result.txt', 'a') as file:
                file.write(f'\nx = {x} \ny = {y} \nresult = {result} \n*************')
        elif s == '/':
            if y != 0:
                result = x / y
                print(f'result = {result}')
                with open('result.txt', 'a') as file:
                    file.write(f'\nx = {x} \ny = {y} \nresult = {result} \n*************')
            else:

                print('result : Division by zero')
                with open('result.txt', 'a') as file:
                    file.write(f'\nx = {x} \ny = {y} \nresult : Division by zero \n*************')
    else:
        print('Invalid operation sign')









