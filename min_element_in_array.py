def test_min_element(array,answer):
    expected = min_element(array)
    print (expected==answer)

def test():
    test1 = [2,3,4,5]
    test_min_element(test1,2)
    test2 = [5,4,-3,-1]
    test_min_element(test2,-3)
    test3 = [1.2,1.222,4.213]
    test_min_element(test3,1.2)

def min_element(arr):
    mini = arr[0]
    for i in arr:
        if i < mini:
            mini = i
    return mini

def main():
    arr = input()
    arr = arr.split(' ')
    arr = map(float,arr)
    arr = list(arr)
    mini = min_element(arr)
    print(mini)

test()