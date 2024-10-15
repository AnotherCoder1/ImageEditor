from image_editor import ImageEditing
from vec2d import Vector2, single_point_rotate_clockwise
from copy import deepcopy
from math import pi, sqrt,atan

class MoreShapes(ImageEditing):
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

    def draw_filled_circle(self, radius:float):
        self.pos=self.init_circle_32()
        for i in range(0, len(self.pos)+31):
            if i%2==1:
                self.pos.insert(i, Vector2(0.0, 0.0))
        
        self.scale_and_offset(Vector2(radius, radius),Vector2(radius,radius))
        self.draw_filled_closed_shape()

    def init_isoceles_triangle(self):
        pos=[
            Vector2(0.0, 10.0), Vector2(2.5,0.0), Vector2(5.0,10.0)
        ]
        for i in pos:
            i.x=i.x*10.0
            i.y=i.y*10.0

        return pos
    
    def init_equilateral_tri(self):
        pos=[
            Vector2(-1.0, 1.0), Vector2(0.0, -1.0), Vector2(1.0, 1.0)
        ]
        return pos
    
    def draw_filled_tri(self, size:Vector2):
        self.pos=self.init_equilateral_tri()
        self.rotate_clockwise(pi)
        self.scale_and_offset(size,size)
        self.conv_vec2d_to_tuple()
        self.pen.polygon(self.pos, self.color)
        self.image.save(self.file_name, 'PNG')

    def draw_isoceles_tri(self):
        self.pos=self.init_isoceles_triangle()
        self.draw_closed_shape()

    def init_rhombus(self):
        pos={
            Vector2(0.0, 50.0),Vector2(58.889, 16.0), Vector2(11.6, 50.0),
            Vector2(58.889, 16.0),Vector2(70.489, 16.0), Vector2(11.6, 50.0)
        }
        return pos
    
    def draw_rhombus(self):
        self.pos=self.init_rhombus()
        self.conv_vec2d_to_tuple()
        self.pen.polygon(self.pos, self.color)
        self.image.save(self.file_name, 'PNG')

    def init_square(self):
        pos=[
            Vector2(0.0, 0.0), Vector2(1.0, 0.0),
            Vector2(0.0, 1.0), Vector2(1.0, 1.0)
        ]
        return pos
    
    def draw_filled_rectangle(self):
        self.pos=self.init_square()
        self.scale(Vector2(1.0, 10.0))
        self.draw_filled_closed_shape()

    def init_hexagon(self):
        pos=[
            Vector2(0.0, -1.0), Vector2(0.866, -0.5),
            Vector2(0.866, 0.5), Vector2(0.0, 1.0),
            Vector2(-0.866, 0.5), Vector2(-0.866, -0.5)
        ]
        return pos
    
    def draw_hexagon(self):
        self.pos=self.init_hexagon()
        self.scale_and_offset(Vector2(4.543,4.543), Vector2(0.866*4.543, 4.543))
        for i in range(0, len(self.pos)):
            j=i+1
            self.pen.line([(self.pos[i].x, self.pos[i].y),(self.pos[j%6].x, self.pos[j%6].y)], self.color)
        self.image.save(self.file_name, 'PNG')

    def draw_football(self):
        self.pos=self.init_hexagon()
        second=self.init_hexagon()
        third=self.init_hexagon()
        fourth=self.init_hexagon()
        fifth=self.init_hexagon()
        sixth=self.init_hexagon()
        seventh=self.init_hexagon()
        eight=self.init_hexagon()
        ninth=self.init_hexagon()
        tenth=self.init_hexagon()
        self.pos+=(second+third+fourth+fifth+seventh+eight+ninth+sixth+tenth) 
        self.scale_and_offset(Vector2(4.543,4.543), Vector2(3.934, 4.543))
        self.translate_partly(6,12, Vector2(7.69,0.0))
        self.translate_partly(12,18, Vector2(15.38, 0.0))
        self.translate_partly(18,24, Vector2(-3.846, 6.8145))
        self.translate_partly(24,30, Vector2(3.84, 6.8145))
        self.translate_partly(30,36, Vector2(11.53, 6.8145))
        self.translate_partly(36,42, Vector2(19.22, 6.8145))
        self.translate_partly(42,48, Vector2(0.0, 13.628))
        self.translate_partly(48,54, Vector2(7.69, 13.628))
        self.translate_partly(54,60, Vector2(15.38, 13.628))

        for i in range(0, len(self.pos)):
            j=i+1
            if j%6==0:
                self.pen.line([(self.pos[i].x, self.pos[i].y),(self.pos[j-6].x, self.pos[j-6].y)], self.color)
            else:
                self.pen.line([(self.pos[i].x, self.pos[i].y),(self.pos[j].x, self.pos[j].y)], self.color)

        self.pos.clear()

        self.draw_circle(Vector2(10.819,10.819))

    def draw_three_triangle(self, size:Vector2):
        pos=[
            Vector2(1.0, 2.0)
        ]
        self.pos=self.init_square()
        self.pos+=pos
        self.scale(size)
        self.draw_filled_closed_shape()

    def test_rounded_rectangle(self, coords:tuple, radius:float):
        self.pen.rounded_rectangle((coords[0], coords[1], coords[2], coords[3]), radius=radius, outline=self.color)
        self.image.save(self.file_name, 'PNG')

    def init_diagonal_30_degree(self):
        pos=[
            Vector2(0, 1),
            Vector2(1, 0.577),
            Vector2(0, 0.577),
            Vector2(1, 0)
        ]
        return pos

    def draw_diagonal_30_degree(self, size:Vector2):
        self.pos=self.init_diagonal_30_degree()
        self.scale(size)
        self.conv_vec2d_to_tuple()
        self.pen.line([self.pos[0],self.pos[1]], self.color, 1)
        self.pen.line([self.pos[2],self.pos[3]], self.color, 1)
        self.image.save(self.file_name, 'PNG')



                     
                 
     
         
                     

                         
                 
                 
                 
         
                     
             

                 
                 
                 
                 
                             
                     
                 
