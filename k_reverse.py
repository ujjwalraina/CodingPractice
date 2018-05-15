def test(expected,answer):
    return (expected==answer)

def test_case_1():
    arr = [1,2,3,4,5,6,7,8,9]
    k = 4
    arr_out = [4,3,2,1,8,7,6,5,9]
    print(test(k_reverse(arr,k), arr_out))

def test_case_2():
    arr = [1,2,3,4]
    k = 2
    arr_out = [2,1,4,3]
    print(test(k_reverse(arr,k),arr_out))

def test_case_3():
    arr = [1,2,3,4]
    k = 5
    arr_out = [1,2,3,4]
    print(test(k_reverse(arr,k),arr_out))

def test_case_4():
    arr = [1,2,3,4]
    k = 4
    arr_out = [4,3,2,1]
    print(test(k_reverse(arr,k),arr_out))

def test_case_5():
    arr = [1,2,3,4]
    k = 0
    arr_out = [1,2,3,4]
    print(test(k_reverse(arr,k),arr_out))

def test_case_6():
    arr = [1,2,3,4]
    k = 1
    arr_out = [1,2,3,4]
    print(test(k_reverse(arr,k),arr_out))

def k_reverse(arr,k):
    add = k
    j = 0
    new_arr = []

    if k > len(arr) or k == 0 or k == 1:
        return arr

    while j < len(arr) :
        for i in range((k-1),j-1,-1):
            new_arr.append(arr[i])
        j = j + k
        k = k + add

    if len(arr) % add != 0:
        j = j - add
        for i in range(j,len(arr)):
            new_arr.append(arr[i])
    return new_arr

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()