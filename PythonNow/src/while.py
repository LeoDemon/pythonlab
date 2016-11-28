#filename: while.py

import sys

number = 18
running = True

while running:
    try:
        guess = int(input('Enter an integer: '))
        if guess == number:
            print ('Congratulations, you guessed it.')
            running = False
        elif guess < number:
            print ('No, it is a little higher than that')
        else:
            print ('NO, it is a little lower than that')
    except ValueError as ve:
        print("input error, please check and try again...error is:[%s]" % ve.args)
    except Exception:
        print("Exception...and exit now")
        sys.exit()
else:
    print ('The while loop is over.')

print ('Done.')

