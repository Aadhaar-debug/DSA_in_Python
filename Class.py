class a:
    def new(a , b):
        d = 3
        c = a+b
        print(c)
        print(d)
Object1 = a.new(1,3)


class b:
    def __init__(self):
        self.a = 23
        self.c = 25
    def add(self):
        print(self.a + self.c)
Object2 = b()
Object2.add()


class c(b):
    def __init__(self):
        super().__init__()
        self.x = 2
        self.y = 3
    def mult(self):
        m = self.x * self.y * self.a
        print(m)
Object3 = c()
Object3.mult()
