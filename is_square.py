import math

class point:
        def __init__(self,x,y):
            self.x =x
            self.y = y

def side(a,b):
    return (math.sqrt(((b.y-a.y)**2) + ((b.x-a.x)**2)))

def is_square(p,q,r,s):
    s1 = side(p,q)
    print(s1)
    s2 = side(q,r)
    print(s2)
    s3 = side(r,s)
    print(s3)
    s4 = side(s,p)
    print(s4)
    d1 = side(p,r)
    print(d1)
    d2 = side(q,s)
    print(d2)
    if s1==s2==s3==s4 and d1==d2:
        return True
    else:
        return False

def test_square(expected,result):
    print(expected==result)

def test():
    p = point(10,10)
    q = point(20,10)
    r = point(20,20)
    s = point(10,20)
    test_square(is_square(p,q,r,s), True)

test()