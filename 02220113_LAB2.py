class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
        self.size = 0
        print("Created new LinkedList")
        print(f"Current size: {self.size}")
        print(f"Head: {self.head}")

ll = LinkedList()
