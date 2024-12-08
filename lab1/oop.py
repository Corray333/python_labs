import math


class ShapeError(Exception):
    pass


class Shape:
    def __init__(self, id, x, y):
        self.id = id
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ShapeError("Координаты должны быть числами.")
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise ShapeError("Смещение должно быть числом.")
        self.x += dx
        self.y += dy

    def bounding_box(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе.")

    @staticmethod
    def is_intersect(s1, s2):
        try:
            x1_min, y1_min, x1_max, y1_max = s1.bounding_box()
            x2_min, y2_min, x2_max, y2_max = s2.bounding_box()
        except NotImplementedError as e:
            raise ShapeError(f"Ошибка вызова bounding_box: {e}")
        except AttributeError:
            raise ShapeError("Переданный объект не имеет метода bounding_box.")
        
        return not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)


class Quad(Shape):
    def __init__(self, id, x, y, side):
        super().__init__(id, x, y)
        if side <= 0:
            raise ShapeError("Сторона квадрата должна быть положительным числом.")
        self.side = side

    def bounding_box(self):
        return (self.x, self.y, self.x + self.side, self.y + self.side)


class Pentagon(Shape):
    def __init__(self, id, x, y, side):
        super().__init__(id, x, y)
        if side <= 0:
            raise ShapeError("Сторона пятиугольника должна быть положительным числом.")
        self.side = side

    def bounding_box(self):
        side_to_height = self.side * (1 + math.sqrt(5))
        return (self.x, self.y, self.x + self.side, self.y + side_to_height)


if __name__ == "__main__":
    try:
        quad = Quad("Quad1", 0, 0, side=10)
        pentagon = Pentagon("Pentagon1", 200, 100, side=4)

        if Shape.is_intersect(quad, pentagon):
            print(f"{quad.id} и {pentagon.id} пересекаются.")
        else:
            print(f"{quad.id} и {pentagon.id} не пересекаются.")

        print(f"Координаты пятиугольника до перемещения: ({pentagon.x}, {pentagon.y})")
        pentagon.move(10, 10)
        print(f"Координаты пятиугольника после перемещения: ({pentagon.x}, {pentagon.y})")

    except ShapeError as e:
        print(f"Ошибка: {e}")
