"""
===================   TASK 2   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
#Euklidov algoritam je nzd(a,b)

def nzd(a,b):

    if not isinstance(a,int) and not isinstance(b,int):
        return -1

    a_apsolutno= abs(a)
    b_apsolutno= abs(b)
    z = abs(a_apsolutno-b_apsolutno)

    if z == 0:
        return b_apsolutno
    else:
        return nzd(z,min(a_apsolutno,b_apsolutno))

def main():

    print(nzd(688, 24))

main()