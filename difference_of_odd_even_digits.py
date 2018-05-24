def test(expected,answer):
    print(expected==answer)

def test_difference():
    test1 = "1212112"
    test(difference_of_odd_even_digits(test1),"Yes")
    test2 = "123"
    test(difference_of_odd_even_digits(test2), "No")
    test3 = ""
    test(difference_of_odd_even_digits(test3), "Yes")
    test4 = "13598761"
    test(difference_of_odd_even_digits(test4), "Yes")

def difference_of_odd_even_digits(strs):
    sum1 = 0
    sum2 = 0
    strs = list(strs)
    for i in range(0, len(strs)):
        strs[i] = int(strs[i])
    for i in range(0,len(strs)):
        if i % 2 == 0 :
            sum1 = sum1 + strs[i]
        else :
            sum2 = sum2 + strs[i]
    if sum1 == sum2 :
        return ("Yes")
    else:
        return("No")

test_difference()