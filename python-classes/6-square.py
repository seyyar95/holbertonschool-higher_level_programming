#!/usr/bin/python3
'''Represents a square shape'''


class Square:
    '''Documantation for square class'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not (isinstance(value, int) and len(value) == 2
                and all(isinstance(x, int) for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for u in range(self.__position[1]):
                print()
        index_0 = " " * self.__position[0]
        for i in range(self.__size):
            print(index_0, end="")
            print("#" * self.__size)
