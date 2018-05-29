import math
def test(expected,answer):
    print(expected==answer)

def test_multiply_left_right_array():
    test1 = [1,2,3,4]
    test(multiply_left_right_array(test1),21)
    test2 = [4,5,6]
    test(multiply_left_right_array(test2), 44)
    test3 = []
    test(multiply_left_right_array(test3),0)
    test4 = [10,9,8,7,6,5,4,3,2,1]
    test(multiply_left_right_array(test4),600)

def multiply_left_right_array(arrs):
    size = len(arrs)
    n = math.floor(size/2)
    arr1 = arrs[0:n]
    arr2 = arrs[n:size]
    pro1 = pro2 = 0
    for i in range (0,len(arr1)):
        pro1 = pro1 + arr1[i]
    for i in range(0, len(arr2)):
        pro2 = pro2 + arr2[i]
    return(pro1*pro2)

test_multiply_left_right_array()