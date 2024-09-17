# 10:45
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class Linked_List:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_node(self):
        item = self.head.data
        self.head = self.head.next
        return item
    
LL = Linked_List()
LL.add_node(5)
LL.add_node(6)
LL.add_node(7)
LL.add_node(8)
LL.add_node(9)
LL.add_node(10)
LL.display()

