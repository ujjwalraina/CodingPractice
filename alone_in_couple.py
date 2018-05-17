def test(e, a):
    print(e==a)

def test_case_1():
    arr1 = [1,2,3,4,5,6,1,2,3,4,5]
    test(alone(arr1), 6)
    arr2 = [3,1,1,4,2,3,5,6,4,2,5]
    test(alone(arr2), 6)
    arr3 = [6]
    test(alone(arr3),6)
    arr4 = [1,3,3,1]
    test(alone(arr4),0)

def alone_1(arr1):
    d = dict()
    for i in arr1:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for i in d:
        if d[i] == 1:
            return i

def alone(arr1):
    a = 0
    for i in range(0,len(arr1)):
        a = a ^ arr1[i]
    return(a)




test_case_1()