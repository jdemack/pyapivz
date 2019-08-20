#!/usr/bin/python3

def main():

    while True:
        try:
            name = input('Enter a file name: ')
            with open(name, 'w') as myfile:
                myfile.write("This worked")
        except:
            print('Error with that file name! Try again...')
        else:
            break

    print('Thanks for making that simple file')


if __name__ == '__main__':
    main()

