import math

def test_is_prime(expected,answer):
    print(expected==answer)

def test():
    test1 = 2
    test_is_prime(is_prime(test1),True)
    test2 = 3
    test_is_prime(is_prime(test2), True)
    test3 = 169
    test_is_prime(is_prime(test3), False)
    test4 = 10211
    test_is_prime(is_prime(test4), True)

def is_prime(num):
    if num == 2 or num == 3 :
        return True
    for i in range(2,math.ceil(num**0.5)+1):
        if num % i == 0 :
            return False
    return True

test()
