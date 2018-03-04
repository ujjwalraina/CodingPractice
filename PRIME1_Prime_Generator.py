testcase = int(input())
while testcase != 0 :
    a = [int(x) for x in input().split()]
    m = a[0]
    n = a[1]
    c = []
    b = []
    for i in range ((m+1),n):
        b.append(i)
        j = 2
        while j < i:
            if i % j == 0 and i != j:
                c.append(i)
                break
            j = j + 1
    d = list(set(b)-set(c))
    sort(d)
    for i in d:
        print(i)
    testcase = testcase - 1
    print("\n")
