class Student:
    def __init__(self, x, y, z):
        self.name = x
        self.degree = y
        self.native = z

    def intro(self):
        print(f'Hi , My name is {self.name} ')
        print(f'I am pursuing {self.degree} from SVCE ')
        print(f'I am belongs to {self.native}')


student = Student("pragadeesh", "B.E", "chennai")
student.intro()

