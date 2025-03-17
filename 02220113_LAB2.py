class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def append(self, element):
        new_node = Node(element)
        if not self.head: self.head = self.tail = new_node
        else: self.tail.next, self.tail = new_node, new_node
        self.size += 1
        print(f"Appended {element}")

    def get(self, index):
        if index < 0 or index >= self.size: raise IndexError("Index out of range")
        current = self.head
        for _ in range(index): current = current.next
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.size: raise IndexError("Index out of range")
        current = self.head
        for _ in range(index): current = current.next
        current.data = element
        print(f"Set index {index} to {element}")

    def prepend(self, element):
        new_node = Node(element)
        new_node.next, self.head = self.head, new_node
        if not self.tail: self.tail = new_node
        self.size += 1
        print(f"Prepended {element}")

    def __str__(self):
        elements, current = [], self.head
        while current: elements.append(str(current.data)); current = current.next
        return "Linked list: [" + " ".join(elements) + "]"

if __name__ == "__main__":
    ll = LinkedList()
    print(f"Created new LinkedList\nSize: {ll.size}\nHead: {ll.head}")
    ll.append(5)
    print(f"Element at index 0: {ll.get(0)}")
    ll.set(0, 10)
    print(f"Element at index 0: {ll.get(0)}")
    ll.prepend(10)
    ll.append(5)
    print(ll)