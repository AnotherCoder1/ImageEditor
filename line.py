from vec2d import Vector2

class Line:
    def __init__(self, p0:Vector2, p1:Vector2) -> None:
        self.points=[p0,p1]

    def __str__(self) -> str:
        return f'({self.points[0]}, {self.points[1]})'