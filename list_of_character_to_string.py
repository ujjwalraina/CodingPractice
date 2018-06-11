def test(output,expected):
    print(output==expected)

def test_list_to_string():
    test1 = "g e e k s f o r g e e k s"
    test(list_to_string(test1),"geeksforgeeks")
    test2 = "p r o g r a m m i n g"
    test(list_to_string(test2),"programming")

def list_to_string(strs):
    strs = list(strs)
    for i in range(0,len(strs)):
        if strs[i] == " ":
            strs[i] = ''
    strs = "".join(strs)
    return strs

test_list_to_string()