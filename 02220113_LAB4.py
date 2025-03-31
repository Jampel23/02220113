class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is not None:  
            self.rear.next = new_node 
        self.rear = new_node          
        if self.front is None:        
            self.front = new_node      
        self.size += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        removed_data = self.front.data  
        self.front = self.front.next      
        if self.front is None:           
            self.rear = None              
        self.size -= 1
        print(f"Dequeued element: {removed_data}")
        return removed_data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        print(f"Front element: {self.front.data}")
        return self.front.data

    def size(self):
        return self.size

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display queue: [{', '.join(map(str, elements))}]")


if __name__ == "__main__":
    queue = LinkedQueue()
    print(f"Created new LinkedQueue")
    print(f"Queue is empty: {queue.is_empty()}")

    queue.enqueue(10)
    queue.display()
    
    queue.enqueue(20)
    queue.display()
    
    queue.enqueue(30)
    queue.display()
    
    queue.peek()
    queue.dequeue()
    queue.display()
    
    print(f"Queue size: {queue.size}")