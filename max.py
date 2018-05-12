def test_max_frequency(strings,answer):
    print (max_frequency(strings)==answer)

def test():
    test1 = "aaaabbccddd"
    test_max_frequency(test1,'a')
    test2 = "AAAbbD"
    test_max_frequency(test2,'A')
    test3 = "ujjwal raina"
    test_max_frequency(test3,'a')
    test4 = "AabBcDCd"
    test_max_frequency(test4,'A')

def main():
    a  = input()
    max_freq = max_frequency(a)
    print(max_freq)

def max_frequency(a):
    str = a
    a = list(a)
    d = dict()
    maxi = ''
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    l = list(d.values())
    maxi = l[0]
    for i in range(0,len(l)):
        if l[i]> maxi :
            maxi = l[i]
    for i in range(0,len(str)):
        if d[str[i]] == maxi:
            return(str[i])

test()