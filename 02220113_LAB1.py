class CustomList:
    def __init__(self, capacity=10):
        self._max_capacity = capacity  
        self._size = 0  
        self._array = [None] * self._max_capacity  

        print(f"Created new CustomList with capacity: {self._max_capacity}")
        print(f"Current size: {self._size}")

    def append(self, element):
        if self._size == self._max_capacity:
            self._resize()
        self._array[self._size] = element
        self._size += 1
        print(f"Appended {element} to the list")

    def _resize(self):
        old_capacity = self._max_capacity
        self._max_capacity *= 2
        new_array = [None] * self._max_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        print(f"Resized array from capacity {old_capacity} to {self._max_capacity}")

    def get(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, element):
        if 0 <= index < self._size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of range")

    def size(self):
        return self._size

    def __str__(self):
        return str([self._array[i] for i in range(self._size)])



if __name__ == "__main__":
    my_list = CustomList() 
    my_list.append(5)  
    print(f"Element at index 0: {my_list.get(0)}")  
    my_list.set(0, 10)  
    print(f"Element at index 0: {my_list.get(0)}")  
    print(f"Current size: {my_list.size()}")
