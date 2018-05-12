import math

def test_palindrome1(strings,answer):
    print (palindrome1(strings)==answer)

def test_palindrome2(strings,answer):
    print (palindrome2(strings)==answer)

def test_palindrome3(strings,answer):
    print (palindrome3(strings)==answer)

def test():
    test1 = "abba"
    test_palindrome3(test1,True)
    test2 = "Abbbba"
    test_palindrome3(test2,False)
    test3 = "gdfvtre"
    test_palindrome3(test3,False)
    test4 = "ab1221ba"
    test_palindrome3(test4,True)
    test5 = "abcba"
    test_palindrome3(test5,True)
    test6 = "abca"
    test_palindrome3(test6, False)

def palindrome1(a):
    if a == a[::-1]:
        return True
    else :
        return False

def palindrome2(a):
    b = list(a)
    c = []
    for i in range(len(a)-1,-1,-1):
        c.append(a[i])
    return (b==c)

def palindrome3(a):
    for i in range(0,math.ceil((len(a)/2))):
        if a[i] != a[(len(a)-1)-i]:
            return False
    return True

def main():
    a = input()
    b = palindrome3(a)

test()