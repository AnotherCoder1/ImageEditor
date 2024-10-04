from image_editor import ImageEditing
from implemented_shape import MoreShapes
from vec2d import Vector2, single_point_rotate_clockwise
from copy import deepcopy
from math import sqrt, atan,pi, sin, cos

class BendedCorner(ImageEditing):
    def __init__(self, file_name: str, file_size: tuple, color: tuple, triangle:list[Vector2]) -> None:
        super().__init__(file_name, file_size, color)
        self.triangle:list[Vector2]=triangle              
        self.d0=self.diff_points(triangle[1], triangle[0])
        self.d1=self.diff_points(triangle[2], triangle[1])
        self.d2=self.diff_points(triangle[2], triangle[0])

    def init_circle_32(self):
        initial=Vector2(0.0, -1.0)
        all_pos=[]
        all_pos.append(deepcopy(initial))
        for i in range(0,32):
            next=single_point_rotate_clockwise(11.25/180*pi,initial)
            entah=deepcopy(next)
            all_pos.append(entah)
            initial=deepcopy(next)

        return all_pos

    def draw_circle(self, size:Vector2, offset:Vector2):
        self.pos=self.init_circle_32()
        self.scale_and_offset(size, offset)
        self.draw_closed_shape()

    def draw_circle_in_triangle(self,smaller_radius):                                      
        radius=self.max_radius_in_triangle() 
        diff_radius=radius-smaller_radius
        center=self.get_center_in_tri()
        angle=self.compute_angle_transformed()
        dy=diff_radius*sin(angle)
        dx=diff_radius*cos(angle)

        self.draw_circle(Vector2(smaller_radius, smaller_radius), Vector2(self.triangle[1].x+dx, self.triangle[1].y+dy) )                                 
        self.pen.line([(200,100),(300,50),(400,170)], self.color)                          
        self.image.save(self.file_name, 'PNG')                                                                                    

    def max_radius_in_triangle(self):                                       
        ab = sqrt((self.triangle[1].x - self.triangle[0].x)**2 + (self.triangle[1].y - self.triangle[0].y)**2)     
        bc = sqrt((self.triangle[2].x - self.triangle[1].x)**2 + (self.triangle[2].y - self.triangle[1].y)**2)     
        ac = sqrt((self.triangle[2].x - self.triangle[0].x)**2 + (self.triangle[2].y - self.triangle[0].y)**2)     
        s = (ab + bc + ac) / 2                                                                 
        area = sqrt(s * (s - ab) * (s - bc) * (s - ac))                                        
        radius = area / s                                                                      
        return radius                                                                                       

    def get_center_in_tri(self):                                            
        ab = sqrt((self.triangle[1].x - self.triangle[0].x)**2 + (self.triangle[1].y - self.triangle[0].y)**2)     
        bc = sqrt((self.triangle[2].x - self.triangle[1].x)**2 + (self.triangle[2].y - self.triangle[1].y)**2)     
        ac = sqrt((self.triangle[2].x - self.triangle[0].x)**2 + (self.triangle[2].y - self.triangle[0].y)**2)     
        ox = (self.triangle[0].x * bc + self.triangle[1].x * ac + self.triangle[2].x * ab) / (ab + bc + ac)   
        oy = (self.triangle[0].y * bc + self.triangle[1].y * ac + self.triangle[2].y * ab) / (ab + bc + ac)   
        return Vector2(ox, oy)             

    def compute_angle_transformed(self):
        if self.d0.x !=0 or self.d0.y !=0 or self.d1.x !=0 or self.d1.y !=0 or self.d2.x !=0 or self.d2.y !=0:
            angle=atan(self.d2.y/self.d2.x)
            real_angle=pi-angle
            return angle
        else:
            return 0

    def diff_points(self, start:Vector2, end: Vector2):
        return Vector2(end.x-start.x, end.y-end.x)                                              