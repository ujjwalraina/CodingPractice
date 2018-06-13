# https://practice.geeksforgeeks.org/problems/trimorphic-number/0

def test(answer,expected):
    print(answer==expected)

def test_trimorphic_number():
    test1 = 1
    test(trimorphic_number(test1),1)
    test2 = 0
    test(trimorphic_number(test2),1)
    test3 = 24
    test(trimorphic_number(test3),1)
    test4 = 4
    test(trimorphic_number(test4), 1)
    test5 = 9
    test(trimorphic_number(test5), 1)
    test6 = 25
    test(trimorphic_number(test6), 1)
    test7 = 8
    test(trimorphic_number(test7), 0)

def trimorphic_number(N):
    cube = N**3
    if cube == N:
        return 1
    cube_str = str(cube)
    leng = int(len(str(N)))
    temp = int(cube_str[-leng:])
    if temp == N :
        return 1
    else :
        return 0

test_trimorphic_number()