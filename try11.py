#!/usr/bin/python3

while True:
    try:
        print('lets div x by y!')
        x = int(input('What is the value of x? '))
        y = int(input('What is the value of y? '))
        print('The value of x div by y is:', x/y)
    except ZeroDivisionError:
        print('Cannot divide by 0...restarting...')
    except ValueError:
        print('Non numerical value provided. Try again...')
    except Exception as err:
        print(err)

