from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def _right_triangle(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True

        return False

    def _is_triangle_can_exist(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def area(self) -> float:
        if self._is_triangle_can_exist():
            p = (self.a + self.b + self.c) / 2
            if self._right_triangle():
                print(f'Triangle is right')

            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

        raise ValueError('Triangle does not exist')

class Circle(Figure):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return 3.14 * self.r ** 2

if __name__ == '__main__':
    params = input('Enter radius/sides of the circle/triangle separated by space: ').split()
    if len(params) == 3:
        triangle = Triangle(int(params[0]), int(params[1]), int(params[2]))
        print(f'Triangle area: {triangle.area()}')
    elif len(params) == 1:
        circle = Circle(int(params[0]))
        print(f'Circle area: {circle.area()}')
    else:
        raise ValueError