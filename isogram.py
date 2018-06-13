#https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not/0
def test(expected,result):
    print(expected==result)

def test_isogram():
    test1 = "france"
    test(isogram(test1),1)
    test2 = "india"
    test(isogram(test2),0)

def isogram(strs):
    strs1 = set(strs)
    if(len(strs)==len(strs1)):
        return 1
    else:
        return 0

test_isogram()