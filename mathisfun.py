from __future__ import annotations
import math

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point2d(self):
        print((self.x,self.y))


class Vector2D:
     def __init__(self, v_start: Point2D, v_end: Point2D):
         self.v_start = v_start
         self.v_end = v_end

     def print_Vector(self):
         print(str(self.v_start) + ' ' + str(self.v_end))

     def length(self):
         return math.sqrt((self.v_end.x - self.v_start.x)**2 - (self.v_end.y - self.v_start.y)**2)

     def add(self , another: Vector2D) -> Vector2D:
         return Vector2D(v_start=Point2D(x=self.v_start.x + another.v_start.x, y=self.v_start.y + another.v_start.y),
                         v_end=Point2D(x=self.v_end.x + another.v_end.x, y=self.v_end.y + another.v_end.y))

     def multiply_by_scalar(self, p_lambda) -> Vector2D:
         return Vector2D(v_start=Point2D(x=self.v_start.x * p_lambda, y=self.v_start.y * p_lambda),
                         v_end=Point2D(x=self.v_end.x * p_lambda, y=self.v_end.y * p_lambda))

     def __add__(self, another: Vector2D) -> Vector2D:
         return Vector2D(v_start=Point2D(x=self.v_start.x + another.v_start.x, y=self.v_start.y + another.v_start.y),
                         v_end=Point2D(x=self.v_end.x + another.v_end.x, y=self.v_end.y + another.v_end.y))

     def __mul__(self, p_lambda: int) -> Vector2D:
         return Vector2D(v_start=Point2D(x=self.v_start.x * p_lambda, y=self.v_start.y * p_lambda),
                         v_end=Point2D(x=self.v_end.x * p_lambda, y=self.v_end.y * p_lambda))

punkt1 = Point2D(0.9, 1.1)
punkt2 = Point2D(1.7, 3.5)

punkt3 = Point2D(1, 2)
punkt4 = Point2D(3, 6)

v1 = Vector2D(punkt1, punkt2)
v2 = Vector2D(punkt3, punkt4)
