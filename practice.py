# # LIFO
class stk:
    def __init__(self):
        self.stk = []
    def push(self,item):
        self.stk.append(item)
    def peek(self):
        return self.stk[-1]
    def pop(self):
        self.stk.pop(-1)
s = stk()
s.push(0)
s.push(1)
print(s.peek())
s.pop()
print(s.peek())

# # FIFO
class queues:
    def __init__(self):
        self.qu = []
    def push1(self,item):
        self.qu.append(item)
    def peek1(self):
        return self.qu[0]
    def pop1(self):
        self.qu.pop(0)
q = queues()
q.push1(0)
q.push1(1)
print(q.peek1())
q.pop1()
print(q.peek1())


# Dequeues
class dequeue:
    def __init__(self):
        self.dequeues = []
    def push_end(self,item):
        self.dequeues.append(item)
        print(f"New Queue = {self.dequeues}")
    def push_front(self,item):
        self.dequeues.insert(0,item)
        print(f"New Queue = {self.dequeues}")
    def peek_front(self):
        return self.dequeues[0]
    def peek_end(self):
        return self.dequeues[-1]
    def pop_front(self):
        return self.dequeues.pop(0)
        print(f"New Queue = {self.dequeues}")
    def pop_end(self):
        self.dequeues.pop(-1)
        print(f"New Queue = {self.dequeues}")
    def size(self):
        return len(self.dequeues)
dq = dequeue()
print(dq.size())
dq.push_end(2)
dq.push_front(1)
dq.push_end(4)
dq.push_front(5)
print(dq.size())
dq.pop_end()
dq.pop_end()
print(dq.size())
print(dq.peek_front())
print(dq.peek_end())