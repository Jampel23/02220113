class ArrayQueue:
    def __init__(self, capacity=10):
        # Initialize the queue with a default capacity (or given capacity)
        self.capacity = capacity
        self.queue = [None] * capacity  # Array to store the queue elements
        self.front = 0  # Points to the front element in the queue
        self.rear = 0  # Points to the next available position to insert an element
        self.size = 0  # Tracks the number of elements in the queue
        print(f"Created new Queue with capacity: {self.capacity}")

    def enqueue(self, element):
        # Add an element to the rear of the queue
        if self.size == self.capacity:
            print("Queue is full! Cannot enqueue.")
        else:
            self.queue[self.rear] = element
            self.rear = (self.rear + 1) % self.capacity  # Circular increment
            self.size += 1
            print(f"Enqueued {element} to the queue")
            self.display()

    def dequeue(self):
        # Remove and return the element at the front
        if self.size == 0:
            print("Queue is empty! Cannot dequeue.")
            return None
        else:
            element = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity  # Circular increment
            self.size -= 1
            print(f"Dequeued element: {element}")
            self.display()
            return element

    def peek(self):
        # Return the element at the front without removing it
        if self.size == 0:
            print("Queue is empty! Cannot peek.")
            return None
        else:
            return self.queue[self.front]

    def size(self):
        # Return the current number of elements
        return self.size

    def display(self):
        # Show all elements in the queue
        if self.size == 0:
            print("Queue is empty.")
        else:
            elements = []
            index = self.front
            for _ in range(self.size):
                elements.append(self.queue[index])
                index = (index + 1) % self.capacity  # Circular increment
            print(f"Current queue: {elements}")
    
    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0

    def is_full(self):
        # Check if the queue is full
        return self.size == self.capacity


# Example usage of the ArrayQueue class
queue = ArrayQueue(10)

print(f"Queue is empty: {queue.is_empty()}")

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"Front element: {queue.peek()}")

queue.dequeue()

print(f"Queue size: {queue.size}")
