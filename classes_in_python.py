class a:
    def __init__(self):
        self.a = 12
        self.b = 12
    def multiply(self):
        print(self.a * self.b)
A = a()
A.multiply()



class b:
    def modulus(self,a,b):
        print(a//b)
B = b()
B.modulus(8,4)



def global_increment(h):
    h = h + 1
    print(h)
    return h




class c(a):
    def minus(self,y):
        x = self.a - y
        print(x)
        
C = c()
C.minus(1)




