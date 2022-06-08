from math import fabs
from random import randint, seed
from sqroot import sqroot

def test_sqrt(tests, errortol):
    passed = 0
    n = len(tests)
    for i in range(n):
        x = tests[i]
        result = sqroot(x, errortol)
        if fabs(x - result*result) > errortol:
            print(f'test {i+1} failed')
        else:
            print(f'test {i+1:2d} successful!\t\tsqrt({x}) ~= {result:.2f}')
            passed += 1
    print(f'\nPassed {passed}/{n} tests')

# seed random number generator for tests to be equal across platforms
seed(1)

# actual test cases
n = 10
tests = [randint(10, 1000) for _ in range(n)]
errortol = 0.01
test_sqrt(tests, errortol)
