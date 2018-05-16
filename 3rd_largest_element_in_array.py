import sys

def test_func(expected,answer):
    print(expected==answer)

def test():
    test1 = [1,2,3,4,5,6]
    test_func(third_largest_element_in_array(test1),4)
    test2 = [9,8,7,6,5]
    test_func(third_largest_element_in_array(test2),7)
    test3 = [1,1,1]
    test_func(third_largest_element_in_array(test3),1)
    test4 = [9,8,8,8,7,6]
    test_func(third_largest_element_in_array(test4),8)


def third_largest_element_in_array(arr):
    max1 = -1 * sys.maxsize
    max2 = -1 * sys.maxsize
    max3 = -1 * sys.maxsize
    for i in arr:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 =i
        elif i > max3:
            max3 = i
    return max3

test()