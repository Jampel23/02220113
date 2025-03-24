#Implemented by Jampel Tenzin
class ArrayStack:
    def __init__(self, capacity=10):
        self._stack = [None] * capacity 
        self._top = -1 
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {self._capacity}")

    def push(self, element):
        if self._top >= self._capacity - 1:
            print("Stack Overflow: Cannot push element, stack is full.")
            return
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop from an empty stack.")
            return None
        element = self._stack[self._top]
        self._stack[self._top] = None
        self._top -= 1
        print(f"Popped element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty: No element to peek.")
            return None
        return self._stack[self._top]

    def is_empty(self):
        return self._top == -1

    def size(self):
        return self._top + 1

    def display(self):
        print("Display stack:", [self._stack[i] for i in range(self._top + 1)])


if __name__ == "__main__":
    stack = ArrayStack()  
    print("Stack is empty:", stack.is_empty())

    stack.push(10)
    stack.display()
    stack.push(20)
    stack.display()
    stack.push(30)
    stack.display()

    print("Top element:", stack.peek())
    stack.pop()
    print("Stack size:", stack.size())
    stack.display()
