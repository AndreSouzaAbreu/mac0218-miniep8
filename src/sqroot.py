from math import fabs
def sqroot(x, errortol):
    guess = 1
    while fabs(guess*guess - x) > errortol:
        guess = guess/2 + x/(2*guess)
    return guess
