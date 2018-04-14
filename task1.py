"""
===================   TASK 1   ====================
* Name: Rectangular To Polar
*
* Write a function `rect2polar` that will convert
* rectangular complex number notation to polar
* notation. 
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

import math

def rect_2_polar(a,b):

    z = math.sqrt(a**2 + b**2)

    if a > 0:
        angle = math.atan(b/a)

    elif a < 0:
        angle = 3.14 + math.atan(b/a)

    else:
        if b > 0:
            angle = 3.14/2

        else:
            angle = -(3.14/2)

    angle = angle * (180 / 3.14)

    return "("+ str(angle)+","+str(angle)+")"

def main():

     print(rect_2_polar(6,2))

main()