def test(expected,answer):
    print(expected==answer)

def test_countries_at_war():
    test1_A = [1,2,3,4,5,6]
    test1_B = [6,5,4,3,2,1]
    test(countries_at_war(test1_A,test1_B),"3 3 DRAW")
    test2_A = [9]
    test2_B = [8]
    test(countries_at_war(test2_A,test2_B),"1 0 A")
    test3_A = [2,2]
    test3_B = [5,5]
    test(countries_at_war(test3_A,test3_B),"0 2 B")
    test4_A = []
    test4_B = []
    test(countries_at_war(test4_A,test4_B),"0 0 DRAW")

def countries_at_war(arr1,arr2):
    count1 = 0
    count2 = 0
    str1 = ""
    if len(arr1) == len(arr2):
        for i in range(0,len(arr1)):
            if arr1[i]>arr2[i]:
                count1 = count1 + 1
            elif arr2[i]>arr1[i]:
                count2 = count2 + 1
        str1 = str(count1) + " " + str(count2)
        if count1 > count2:
            str1 = str1 + " A"
        elif count2 > count1:
            str1 = str1 + " B"
        else:
            str1 = str1 + " DRAW"
    return str1

test_countries_at_war()