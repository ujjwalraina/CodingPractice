def test(expected,result):
    print(expected==result)

def test_jumpy_ball():
        test1 = 10
        test(jumpy_ball(test1),36)
        test2 = 20
        test(jumpy_ball(test2),76)
        test3 = 30
        test(jumpy_ball(test3),112)
        test4 = 0
        test(jumpy_ball(test4), 0)
        test3 = 1
        test(jumpy_ball(test3), 2)

def jumpy_ball(h):
    d = 0
    while h != 0:
        d = d + (2*h)
        h = int(h/2)
    return d

test_jumpy_ball()