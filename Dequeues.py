'''
These are stacks and queues combined together
'''
class stk1:
    def __init__(self):
        self.stk = []

    def addlast(self, item):
        self.stk.append(item)

    def addfirst(self, item):
        self.stk.insert(0,item)

    def removelast(self):
        if not self.is_empty():
            return self.stk.pop()
        else:
            print("Stack is empty!")
            return None
        
    def removefirst(self):
        if not self.is_empty():
            return self.stk.pop(0)
        else:
            print("Stack is empty!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stk[-1]
        else:
            print("Stack is empty!")
            return None

    def size(self):
        return len(self.stk)

    def is_empty(self):
        return len(self.stk) == 0

# Example usage
s = stk1()
s.addfirst(1)
s.addlast(5)
s.addfirst(4)
s.addlast(7)
s.addfirst(3)
s.addlast(9)
print(s.removefirst())
print(s.removefirst())
print(s.removelast())
print(s.peek())
print(s.size())
print(s.is_empty())
