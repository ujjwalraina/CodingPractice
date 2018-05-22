def test(expected,result):
    print(expected==result)

def test_max_sum():
    test1 = [1,2,3]
    test(max_sum(test1),4)
    test2 = [1,2,2,2,3,4]
    test(max_sum(test2),10)
    test3 = [9,7,5,3,2,0]
    test(max_sum(test3),24)

def max_sum(arrs):
    arrs.sort()
    arrs = arrs[::-1]
    sum = 0
    for i in arrs:
        sum = sum + i
        n = i - 1
        if n in arrs:
            arrs.remove(n)
    return sum

test_max_sum()