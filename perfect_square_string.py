import math

def test(expected,answer):
    print(expected==answer)

def test_perfect_square_string():
    test1 = "1Qy";
    test(perfect_square_string(test1),0)
    test2 = "abcd"
    test(perfect_square_string(test2), 0)
    test3 = "efgh"
    test(perfect_square_string(test3), 0)
    test4 = "d"
    test(perfect_square_string(test4), 1)
    test5=" "
    test(perfect_square_string(test5), 0)

def perfect_square_string(strs):
    strs = list(strs)
    sum = 0
    for i in range(0,len(strs)):
        sum = sum + ord(strs[i])
    res = sum ** 0.5
    if math.ceil(res) == res:
        return 1
    else:
        return 0

test_perfect_square_string()