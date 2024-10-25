# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, row, column):
        self.width = row
        self.height = column
        self.area = self.width * self.height
        self.perimeter = (self.width + self.height) * 2

    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.area}')
        print(f'Perimeter: {self.perimeter}')


shape1 = Shape(5, 3)
shape1.print_info()
