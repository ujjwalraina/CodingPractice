def test(expected,result):
    print(expected==result)

def test_vowel_removal():
    test0 = "cheese"
    test(vowel_removal1(test0), "chs")
    test1 = "welcome to geeksforgeeks"
    test(vowel_removal1(test1),"wlcm t gksfrgks")
    test2 = "what is your name ?"
    test(vowel_removal1(test2), "wht s yr nm ?")

def vowel_removal(strs):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for i in strs:
        if i in vowels:
            strs = strs.replace(i,"")
    return strs

def vowel_removal1(strs):
    strs = list(strs)
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for i in range(0,len(strs)):
        if strs[i] in vowels:
            strs[i] = ""
    strs = "".join(strs)
    return strs

test_vowel_removal()