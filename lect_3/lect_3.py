class FILO:
    def __init__(self):
        self.l = []

    def pull(self, i):
        self.l.append(i)
        return self.l

    def push(self):
        self.l.remove(self.l[-1])
        if len(self.l) == 0:
            raise StopIteration

    def __str__(self):
        return str(self.l[::-1])

class FIFO:
    def __init__(self):
        self.l = []

    def pull(self, i):
        self.l.append(i)
        return self.l

    def push(self):
        self.l.remove(self.l[0])
        if len(self.l) == 0:
            raise StopIteration

    def __str__(self):
        return str(self.l)

y = FILO()
y.pull(5)
y.pull(7)
y.pull(6)
y.push()
print(y)