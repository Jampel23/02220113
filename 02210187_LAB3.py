#implemented by Sujeet Rai
class Node:
    def __init__(self, data=None):
        self.data = data  # Holds the data of the node
        self.next = None  # Points to the next node in the stack


class LinkedStack:
    def __init__(self):
        self.top = None  # Points to the top node of the stack
        self.size = 0  # Keeps track of the number of elements in the stack
        print("Created new LinkedStack")

    def push(self, element):
        # Create a new node and add it to the top of the stack
        new_node = Node(element)
        new_node.next = self.top  # Point the new node to the current top node
        self.top = new_node  # Make the new node the top node
        self.size += 1  # Increment the size counter
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        # If the stack is not empty, pop the top element
        if not self.is_empty():
            popped_element = self.top.data  # Get the data of the top node
            self.top = self.top.next  # Move the top to the next node
            self.size -= 1  # Decrement the size counter
            print(f"Popped element: {popped_element}")
            self.display()
            return popped_element
        else:
            print("Stack is empty, cannot pop.")
            return None

    def peek(self):
        # Return the top element without removing it
        if not self.is_empty():
            print(f"Top element: {self.top.data}")
            return self.top.data
        else:
            print("Stack is empty, no top element.")
            return None

    def is_empty(self):
        # Check if the stack is empty
        return self.size == 0

    def size(self):
        # Return the current size of the stack
        return self.size

    def display(self):
        # Display all elements in the stack from top to bottom
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Display stack: [" + " -> ".join(elements) + "]")

# Example Usage:

# Create a new LinkedStack
stack = LinkedStack()

# Test the operations
stack.push(10)  # Pushed 10 to the stack
stack.push(20)  # Pushed 20 to the stack
stack.push(30)  # Pushed 30 to the stack

stack.peek()  # Top element: 30

stack.pop()   # Popped element: 30
stack.display()  # Current stack: 20 -> 10 -> null




print("Stack size:", stack.size)  # Stack size: 2
