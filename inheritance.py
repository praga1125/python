class Area:
    def __init__(self, x):
        self.x = x


class Circle(Area):
    def area(self):
        result = 3.14 * self.x * self.x
        return result


class Square(Area):
    def area(self):
        result = self.x * self.x
        print(f'The area of square is : {result}')


obj = Circle(5)
area = obj.area()
print(f'The radius of circle : {obj.x} and it\'s area of circle : {area} ')
obj1 = Square(3)
obj1.area()
