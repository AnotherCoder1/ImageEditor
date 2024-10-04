from math import sqrt, cos,sin,pi
from copy import deepcopy

class Vector2:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, another):
        any=Vector2(0,0)
        any.x=self.x+another.x
        any.y=self.y+another.y
        return any
    def __sub__(self, another):
        any=Vector2(0,0)
        any.x=self.x-another.x
        any.y=self.y-another.y
        return any
    def __imul__(self, another):
        self.x*=another.x
        self.y*=another.y

    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def __str__(self) -> str:
        return f'( x: {self.x}, y: {self.y} )'
    
def toKm(distance):
    return 111*distance

def rotate_clockwise(angle:float, poss:list[Vector2]):
    rotated_poss=[]
    for i in range(len(poss)):
        rotated=Vector2(0.0,0.0)
        rotated.x=poss[i].x*cos(angle)-poss[i].y*sin(angle)
        rotated.y=poss[i].x*sin(angle)+poss[i].y*cos(angle)
        rotated_poss.append(rotated)
    
    return rotated_poss

def rotate_anticlockwise(angle:float, poss:list[Vector2]):
    rotated_poss=[]
    for i in range(len(poss)):
        rotated=Vector2(0.0,0.0)
        rotated.x=poss[i].x*cos(angle)+poss[i].y*sin(angle)
        rotated.y=poss[i].x*-sin(angle)+poss[i].y*cos(angle)
        rotated_poss.append(rotated)
    
    return rotated_poss

def single_point_rotate_clockwise(angle:float, pos:Vector2):
    temp=deepcopy(pos)
    pos.x=temp.x*cos(angle)-temp.y*sin(angle)
    pos.y=temp.x*sin(angle)+temp.y*cos(angle)
    return pos

def single_point_rotate_anticlockwise(angle:float, pos:Vector2):
    temp=deepcopy(pos)
    pos.x=temp.x*cos(angle)+temp.y*sin(angle)
    pos.y=temp.x*-sin(angle)+temp.y*cos(angle)
    return pos
          
