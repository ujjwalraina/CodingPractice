def test_vowel_reverse(expected,answer):
    print(expected==answer)

def test():
    test1 = "hello"
    test_vowel_reverse(vowel_reverse(test1),"holle")
    test2 = "twillio"
    test_vowel_reverse(vowel_reverse(test2),"twollii")
    test3 = "help"
    test_vowel_reverse(vowel_reverse(test3),"help")
    test4 = "run"
    test_vowel_reverse(vowel_reverse(test4),"run")
    test5 = "feel"
    test_vowel_reverse(vowel_reverse(test5),"feel")
    test6 = " "
    test_vowel_reverse(vowel_reverse(test6)," ")
    test7 = ""
    test_vowel_reverse(vowel_reverse(test7),"")


def vowel_reverse(strr):
    arr1 = []
    arr2 = []
    for i in strr:
        vowels = ['i','e','a','o','u','I','E','A','O','U']
        if i in vowels:
            arr1.append(i)
    for i in range(0,len(strr)):
        if strr[i] not in vowels:
            arr2.append(strr[i])
        else:
            arr2.append(arr1.pop())
    arr2 = "".join(arr2)
    return arr2

test()