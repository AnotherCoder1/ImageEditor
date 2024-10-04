from vec2d import Vector2,rotate_clockwise
from copy import deepcopy
from math import pi

class BezierCurve:
    def __init__(self,positions: list[Vector2]=[Vector2(0,0), Vector2(1,1),Vector2(2,1),Vector2(3,0)]) -> None:
        self.pos=positions
        self.drawing_points=[positions[0]]

    def __str__(self) -> str:
        return f'Bezier Curve->[0]: {self.pos[0]}, [1]: {self.pos[1]}, [2]:{self.pos[2]}, [3]: {self.pos[3]}\n'
    
    def find_point(self, t:float):
        tt=t*t
        ttt=t*t*t
        return Vector2((1-t)**3*self.pos[0].x+ 3*(1-t)**2*t*self.pos[1].x+3*(1-t)*tt*self.pos[2].x+ttt*self.pos[3].x, 
                       (1-t)**3*self.pos[0].y+ 3*(1-t)**2*t*self.pos[1].y+3*(1-t)*tt*self.pos[2].y+ttt*self.pos[3].y) 




        