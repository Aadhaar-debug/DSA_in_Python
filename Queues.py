'''
IN Queues the FIFO first in first out method is used
At the time of popping the first element is removed everytime.
this is the only diff bw stacks and queues
'''

class Qu1:
    def __init__(self):
        self.Que = []

    def push(self, item):
        self.Que.append(item)

    def pop(self):
        if not self.is_empty():
            return self.Que.pop(0) # ONly differnece between Stacks and Queues
        else:
            print("Stack is empty!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.Que[-1]
        else:
            print("Stack is empty!")
            return None

    def size(self):
        return len(self.Que)

    def is_empty(self):
        return len(self.Que) == 0

# Example usage
s = Qu1()
s.push(5)
s.push(10)
print(s.peek())  # Should print 10
print(s.size())  # Should print 2
print(s.pop())   # Should print 10
print(s.size())  # Should print 1