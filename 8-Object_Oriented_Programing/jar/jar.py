class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        string = f""
        for _ in range(self.size):
            string += "🍪"
        return string

    def deposit(self, n):
        if (self.capacity < self.size + n):
            raise ValueError("Capacity excided")
        self.size += n

    def withdraw(self, n):
        if (self.size - n < 0):
            raise ValueError("Can't withdraw that many")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if (capacity < 0):
            raise ValueError("Negative capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    j = Jar(12)
    print(j.capacity)
    print(j.size)
    j.deposit(2)
    print(j)
    j.withdraw(12)
    print(j)
    return (0)

if __name__ == "__main__":
    main()
