# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, row, column):
        self.width = row
        self.height = column

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
