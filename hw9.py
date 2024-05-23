class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__lt = (self.__x1, self.__y2)
        self.__rb = (self.__x2, self.__y2)
        

    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__lt}이고 우측 하단 꼭지점이 {self.__rb}인 사각형입니다.', end = ' ')

    def getWidth(self, x1 ,x2):
        Width = self.__x2 - self.__x1
        return Width

    def getHeight(self, y1, y2):
        Height = self.__y2 - self.__y1
        return Height
        
    def getArea(self):
        Area = (self.__x2 - self.__x1) * (self.__y2 - self.__y1)
        return Area

    def getPerimeter(self):
        perimeter = ((self.__x2 - self.__x1) * 2) + ((self.__y2 - self.__y1) * 2)
        return perimeter


r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
