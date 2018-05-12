import math

def test_factorial(expected,result):
    print(expected==result)

def test():
    test1 = 3
    test_factorial(fact(test1),6)
    test2 = 1
    test_factorial(fact(test2),1)
    test3 = 567
    test_factorial(fact(test3),math.factorial(test3))

def fact(num):
    for i in range(1,num):
        num = num * i
    return num

def main():
    num = int(input())
    n = fact(num)
    print(n)

test()