class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_area(length, width):
        return length * width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

    def get_area(self):
        return self.calculate_area(self.length, self.width)

    def get_perimeter(self):
        return self.calculate_perimeter(self.length, self.width)

if __name__ == "__main__":
    length = float(input("请输入矩形的长度："))
    width = float(input("请输入矩形的宽度："))

    rectangle = Rectangle(length, width)

    area = rectangle.get_area()
    perimeter = rectangle.get_perimeter()

    print(f"矩形的面积为：{area}")
    print(f"矩形的周长为：{perimeter}")
