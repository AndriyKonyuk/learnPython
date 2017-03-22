class A(type):
    def treePrint(self):
        l = []
        for i in self.__bases__:
            if not i in l:
                l.append(i)
                i.treePrint()
        return l

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(D,B):
    pass

class F(C):
    pass

class G(C):
    pass

class H(F,E,G):
    pass

l = []
def treeprint(cls):
    for i in cls.__bases__:
        if i not in l:
            l.append(i)
            treeprint(i)
    return l

print(treeprint(H))