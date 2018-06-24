# https://practice.geeksforgeeks.org/problems/balanced-array/0

def test(expected,result):
    print(expected==result)

def test_balanced_array():
    test1 = "1 2 1 2 1 3"
    test(balanced_array(test1),2)
    test2 = "10 20"
    test(balanced_array(test2),10)

def balanced_array(arrs):
    arrs = arrs.split(" ")
    arrs=list(map(int,arrs))
    sum1,sum2 = 0,0
    if len(arrs)%2 == 0 :
        n = int(len(arrs)/2)
        sum1,sum2 = 0,0
        for i in range(0,n):
            sum1= sum1 + arrs[i]
        for i in range(n,len(arrs)):
            sum2= sum2 + arrs[i]
    return(sum2-sum1)

test_balanced_array()