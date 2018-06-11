def test_max_element(array,answer):
    expected = max_element(array)
    print (answer==expected)

def max_element(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    return max

def test():
    test1 = [1,4,5,89]
    test_max_element(test1,89)
    test2 = [-1,-2,-3,-4]
    test_max_element(test2,-1)
    test3 = [5,4,3,2,1]
    test_max_element(test3,5)
    test4 = [5.2,6.7,4.6]
    test_max_element(test4,6.7)

def main():
    a = input()
    a = a.split(" ")
    print(a)
    a = map(float,a)
    print(a)
    a = list(a)
    max = max_element(a)
    print(max)

#test()
main()