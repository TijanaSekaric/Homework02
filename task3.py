"""
===================   TASK 3   ====================
* Name:  Roulette
*
* Write a script that will simulate casino game -
* Roulette but only for red, black or green (zero)
* fields. On each run, the script should return
* 'red', 'black' or '0'.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
import random

number = random.randrange(0, 37)
print(number)

red = [1, 3, 5, 7, 9, 10, 13, 14, 18, 20, 21, 24, 25, 29, 30, 31, 33, 35]

if number == 0:

    print('0')

elif number in red:

    print('red')

else:

    print('black')