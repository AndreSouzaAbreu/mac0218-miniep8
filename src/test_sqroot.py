from math import fabs

def test_sqrt(tests, errortol):
    passed = 0
    n = len(tests)
    for i in range(n):
        x = tests[i]
        result = sqroot(x)
        if fabs(x - result*result) > errortol:
            print(f'test {i+1} failed')
        else:
            print(f'test {i+1} successful')
            passed += 1
    print(f'\nPassed {passed}/{n}')
