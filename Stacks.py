'''
The Stack ADT
push- add a new item to the stack.
pop- remove and return the next item in Last In First Out (LIFO)
ordering.
peek- return the next item in LIFO ordering.
method)
size- returns the number of items in the stack (well use the pythonic
len
isempty- return True if the stack has no items and return False
otherwise.
'''

# class ListStack:
#     def __init__(self):
#         self._L = []
#     def push(self, item):
#         self._L.append(item)
#     def pop(self):
#         return self._L.pop()
#     def peek(self):
#         return self._L[-1]
#     def __len__(self):
#         return len(self._L)
#     def isempty(self):
#         return len(self) == 0
    
'''
The Stack class above illustrates the object-oriented strategy of com
position (the Stack has a list). It is also an example of the Wrapper
 Pattern
'''

# from ds2.stack import ListStack
# class BadStack(ListStack):
#     def push(self, item):
#         self._L.insert(0, item)
#     def pop(self):
#         return self._L.pop(0)
#     def peek(self):
#         return self._L[0]

class stk1:
    def __init__(self):
        self.stk = []

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stk.pop()
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
s.push(5)
s.push(10)
print(s.peek())  # Should print 10
print(s.size())  # Should print 2
print(s.pop())   # Should print 10
print(s.size())  # Should print 1
