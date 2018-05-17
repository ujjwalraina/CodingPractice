def test(arr):
    first_positive = len(arr)
    for i in range(0,len(arr)):
        if arr[i]>=0:
            first_positive = i
            break
    for i in range(first_positive,len(arr)):
        if arr[i]<0:
            print("False")
            return
    print("True")


def test_1():
    arr1 = [1,-2,3,-7,0]
    test(split(arr1))
    arr2 = [-1,2,-3]
    test(split(arr2))
    arr3 = [-1, -2, -3]
    test(split(arr3))
    arr4 = [1, 2, 3]
    test(split(arr4))
    arr5 = [1,2,3,-1,-2,-3,4]
    test(split(arr5))

def split_1(arr1):
    for i in range(0,len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i] > arr1[j] and arr1[j]<0:
                temp =arr1[i]
                arr1[i] = arr1[j]
                arr1[j] = temp
    return(arr1)

def split(arr1):
    mini = min(arr1)
    maxi = max(arr1)
    temp = 0
    if mini >= 0 or maxi < 0:
        return (arr1)
    j = len(arr1) - 1
    k = 0
    for i in range(1,(len(arr1)-1)):
        if arr1[i]<0:
            temp = arr1[i]
            arr1[i] = arr1[k]
            arr1[k] = temp
            k = k + 1
        else:
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp
            j = j - 1
    return arr1





test_1()