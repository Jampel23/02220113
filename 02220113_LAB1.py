class CustomList:
    def __init__(self, capacity=10):
      
        self._capacity = capacity  
        self._size = 0  
        self._array = [None] * self._capacity  

        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

    def __str__(self):
       
        return str([self._array[i] for i in range(self._size)])



if __name__ == "__main__":
    my_list = CustomList()  
    print(my_list)  
