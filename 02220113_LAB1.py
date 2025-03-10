class CustomList:
    def __init__(self, capacity=10):
        """
        Constructor to initialize the CustomList.
        Default capacity is set to 10.
        """
        self._capacity = capacity  # Capacity of the list
        self._size = 0  # Current number of elements in the list
        self._array = [None] * self._capacity  # Underlying array for storage

        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

    def append(self, element):
        """
        Adds an element to the end of the list.
        """
        if self._size == self._capacity:
            print("List is full! Cannot append.")  # Simple check for full list
            return
        self._array[self._size] = element
        self._size += 1
        print(f"Appended {element}. Current size: {self._size}")

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        return str([self._array[i] for i in range(self._size)])


# Example usage
if __name__ == "__main__":
    my_list = CustomList()  # Create a CustomList with default capacity
    my_list.append(5)  # Append an element
    my_list.append(10)  # Append another element
    print(my_list)  # Print the list
