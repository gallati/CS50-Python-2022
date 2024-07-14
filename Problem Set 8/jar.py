class Jar:
    def __init__(self, capacity=12, size=0) -> None:
        self.capacity = capacity
        self.size = size


    def __str__(self):
        return "🍪"*self.size


    def deposit(self, n):
        self.size += n


    def withdraw(self, n):
        self.size -= n


    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int or capacity < 0:
            raise ValueError("Incorrect capacity")
        self._capacity = capacity


    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if type(size) != int or size > self.capacity or 0 > size:
            raise ValueError("Incorrect size")
        self._size = size


my_jar = Jar(capacity=10,size=3)
print(my_jar)
my_jar.deposit(3)
my_jar.withdraw(4)
print(my_jar)
