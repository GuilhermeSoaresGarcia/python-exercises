class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        self.values = []
    
    
    def __str__(self):
        return str(self.values)
       

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        self.values.append(value)

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        for number in self.values:
            if value == number:
                self.values.remove(value)
                return print(True)
        return print(False)

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        
        if len(self.values) == 0:
            raise RuntimeError("Lista vazia")
        if (len(self.values) % 2) == 0:
            left = self.values[:(len(self.values) // 2)]
            return left[-1]
        if (len(self.values) % 2) != 0:
            index = (len(self.values) // 2)
            return self.values[index]
            
        
bla = Container()

# bla.add(5)
# bla.add(3)
# bla.add(2)
# bla.add(1)
# bla.delete(4)
# bla.delete(1)
# print(bla)
# bla.add(1)
# bla.add(7)
# bla.add(8)
# bla.add(4)
# bla.add(9)
# bla.add(26)
# print(bla)
# print(bla.get_median())
# bla.add(10)
# bla.add(56)
# bla.add(13)
# print(bla)
print(bla.get_median())

