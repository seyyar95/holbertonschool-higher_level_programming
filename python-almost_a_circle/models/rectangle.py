#!/usr/bin/python3
"""Rectangle class module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError(f"width must be an integer")
        if width <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError(f"height must be an integer")
        if height <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError(f"x must be an integer")
        if x < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError(f"y must be an integer")
        if y < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = y

    def area(self):
        """public method that returns
        the area value of the"""
        return self.__width * self.__height

    def display(self):
        """public method that prints
        stdout the rectangle instance"""
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """__str__ method"""
        name = __class__.__name__
        x = self.__x
        y = self.__y
        return f"[{name}] ({self.id}) {x}/{y} - {self.__width}/{self.__height}"


   def update(self, *args):
        a = 0
        for arg in args:
            if a == 0:    
                self.id = arg
            elif a == 1: 
                self.width = arg
            elif a == 2:
                self.height = arg
            elif a == 3:
                self.x = arg
            elif a == 4:
                self.y = arg
            a += 1
