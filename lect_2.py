l = [1, 2, [3, 4, [5, 6, [8, 9]]]]

class One:
    def met(self, l: list):
        for i in l:
            if isinstance(i, list):
                l += i
                l.remove(i)
        return l


class Two:
    def __init__(self):
        self.nl = []
    def met(self, l: list):
        for i in l:
            if isinstance(i, int):
                self.nl.append(i)
            else:
                self.met(i)
        return self.nl


t = One()
d = Two()

print(t.met(l))
