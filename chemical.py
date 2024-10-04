from image_editor import ImageEditing
from vec2d import Vector2, rotate_clockwise, single_point_rotate_anticlockwise, rotate_anticlockwise
from math import pi
from copy import deepcopy
from drawing_parser import Parser

ANGLE=21/180*pi

class Chemical(ImageEditing):
    def init_benzene(self):
        pos=[
            Vector2(0.0, -1.0),     Vector2(0.866, -0.5),
            Vector2(0.866, 0.0),    Vector2(0.866, 0.5), 
            Vector2(0.0, 1.0),      Vector2(-0.866, 0.5),
            Vector2(-0.866, 0.0),   Vector2(-0.866, -0.5),
            Vector2(0.766, -0.45),  Vector2(0.766, 0.45),
            Vector2(0.0, 0.88),     Vector2(-0.766, 0.45),
            Vector2(-0.766, -0.45), Vector2(0.0, -0.88)
            ]

        for i in range(0,14):
            pos[i].x=pos[i].x*100.0+86.6
            pos[i].y=pos[i].y*100.0+100.0
        
        return pos

    def draw_benzene(self):                            
        self.pos=self.init_benzene()
        for i in range(0, 14):
            j = i + 1
            if i < 7:
                self.pen.line([(self.pos[i % 7].x, self.pos[i % 7].y), (self.pos[j].x,  self.pos[j].y)], fill=self.color,width=1)
            if i == 7:
                self.pen.line([(self.pos[7].x, self.pos[7].y), (self.pos[0].x, self.pos[0].y)], fill=self.color, width=1)
            if i >= 8:
                self.pen.line([(self.pos[8].x,  self.pos[8].y),  (self.pos[9].x,  self.pos[9].y)], fill=self.color, width=1)
                self.pen.line([(self.pos[10].x, self.pos[10].y), (self.pos[11].x, self.pos[11].y)], fill=self.color, width=1)
                self.pen.line([(self.pos[12].x, self.pos[12].y), (self.pos[13].x, self.pos[13].y)], fill=self.color, width=1)

        self.image.save(self.file_name, 'PNG')

    def init_N(self):
        pos=[
            Vector2(-1.0, 1.0), Vector2(-1.0, -1.0),
            Vector2(1.0, 1.0),  Vector2(1.0, -1.0)
        ]

        for i in range(0, 4):
            pos[i].x=pos[i].x*10.0+10.0
            pos[i].y=pos[i].y*10.0+10.0

        return pos

    def draw_N(self):
        self.pos=self.init_N()
        self.draw_non_closed_shape()

    def init_azole(self):
        pos=[
            Vector2(0.10, -0.515), Vector2(0.809, 0.0),
            Vector2(0.6, 0.736),   Vector2(0.4, 0.809),
            Vector2(-0.5, 0.809),  Vector2(-0.809, 0.0),
            Vector2(-0.1, -0.515)
        ]

        for i in range(0,7):
            pos[i].x=pos[i].x*100.0+80.9
            pos[i].y=pos[i].y*100.0+51.5
        return pos

    def draw_azole(self):
        self.pos=self.init_azole()
        for i in range(0, 6):
            j = i + 1
            if i == 2:
                continue
            self.pen.line(
                [      (self.pos[i % 7].x, self.pos[i % 7].y), ( self.pos[j % 7].x,  self.pos[j % 7].y)], fill=self.color, width=1)

        self.pen.line([(self.pos[1].x-10.0, self.pos[1].y+5.04),(self.pos[2].x-8.0,  self.pos[2].y-5.04)], fill=self.color, width=1)
        self.pen.line([(self.pos[4].x+8.0, self.pos[4].y-5.04),( self.pos[5].x+10.0, self.pos[5].y+5.04)], fill=self.color, width=1)
        self.image.save(self.file_name, 'PNG')

    def draw_benzimidazole(self): 
        pos_imid=self.init_azole()
        rotated_imid=rotate_clockwise(ANGLE, pos_imid)
        self.translate(Vector2(193.0, 11.0))
        pos_benz=self.init_benzene()
        for i in range(0, 14):
            j = i + 1
            if i < 7:
                self.pen.line([(pos_benz[i % 7].x, pos_benz[i % 7].y), (pos_benz[j].x,  pos_benz[j].y)], fill=self.color,width=1)
            if i == 7:
                self.pen.line([(pos_benz[7].x, pos_benz[7].y), (pos_benz[0].x, pos_benz[0].y)], fill=self.color, width=1)
            if i >= 8:
                self.pen.line([(pos_benz[8].x, pos_benz[8].y),  (pos_benz[9].x,   pos_benz[9].y)],  fill=self.color, width=1)
                self.pen.line([(pos_benz[10].x, pos_benz[10].y), (pos_benz[11].x, pos_benz[11].y)], fill=self.color, width=1)
                self.pen.line([(pos_benz[12].x, pos_benz[12].y), (pos_benz[13].x, pos_benz[13].y)], fill=self.color, width=1)

        for i in range(0, 6):
            j = i + 1
            if i == 2:
                continue
            self.pen.line(
                [(rotated_imid[i % 7].x, rotated_imid[i % 7].y), (rotated_imid[j % 7].x, rotated_imid[j % 7].y)], fill=self.color, width=1)

        self.pen.line([(rotated_imid[1].x-10.0, rotated_imid[1].y+2.0),(rotated_imid[2].x-4.0,  rotated_imid[2].y-8.0)], fill=self.color, width=1)
        self.image.save(self.file_name, 'PNG')

    def init_propyl(self):
        pos=[
            Vector2(-1.0, 0.7067), Vector2(0.0,0.0),
            Vector2(1.0, 0.7067)
        ]
        for i in range(0, 3):
            pos[i].x=pos[i].x*100.0+100.0
            pos[i].y=pos[i].y*100.0
        return pos

    def draw_propyl(self):
        self.pos=self.init_propyl()
        self.draw_non_closed_shape()

    def init_butyl(self):
        pos=[
            Vector2(-1.0, 0.7067), Vector2(0.0,0.0),
            Vector2(1.0, 0.7067), Vector2(2.0,0.0)
        ]
        for i in range(0, 4):
            pos[i].x=pos[i].x*100.0+100.0
            pos[i].y=pos[i].y*100.0
        return pos

    def draw_butyl(self):
        self.pos=self.init_butyl()
        self.draw_non_closed_shape()

    def init_pyridine(self):
        pos=[
            Vector2(0.0, -1.0),   Vector2(0.6928, -0.6),
            Vector2(0.866, -0.5), Vector2(0.866, 0.5),
            Vector2(0.0, 1.0),    Vector2(-0.866, 0.5),
            Vector2(-0.866, -0.5), 

            Vector2(0.786, -0.44), Vector2(0.786, 0.44),
            Vector2(-0.08, 0.878), Vector2(-0.676, 0.519),
            Vector2(-0.698, -0.5), Vector2(-0.08, -0.85)
            ]

        for i in range(0,len(self.pos)):
            pos[i].x=pos[i].x*100.0+86.6
            pos[i].y=pos[i].y*100.0+100.0

        return pos

    def draw_pyridine(self):                            
        self.pos=self.init_pyridine()
        for i in range(0, 7):
            j = i + 1
            if i==1:
                continue
            else:
                self.pen.line([(self.pos[i].x,  self.pos[i].y), (self.pos[j%7].x, self.pos[j%7].y)], self.color, 1)
        self.pen.line([(self.pos[7].x,  self.pos[7].y), (self.pos[8].x,   self.pos[8].y)], self.color, 1)
        self.pen.line([(self.pos[9].x,  self.pos[9].y), (self.pos[10].x,  self.pos[10].y)], self.color, 1)
        self.pen.line([(self.pos[11].x, self.pos[11].y),(self.pos[12].x,  self.pos[12].y)], self.color, 1)

        self.image.save(self.file_name, 'PNG')

    def init_c(self):
        initial=Vector2(0.0, -1.0)

        all_pos=[]
        all_pos.append(deepcopy(initial))

        for i in range(0,16):
            next=single_point_rotate_anticlockwise(11.25/180*pi,initial)
            entah=deepcopy(next)
            all_pos.append(entah)
            initial=deepcopy(next)

        for i in all_pos:
            i.x=i.x*20.0+20.0 
            i.y=i.y*10.0+10.0

        return all_pos

    def draw_c(self):
        self.pos=self.init_c()
        self.draw_non_closed_shape()

    def init_a(self, coordParser:Parser):
        coords=coordParser.tuple_to_vector()
        min,max=coordParser.finding_min_max_from_vector()
        print(f'min: {min}, max: {max}')
        for i in coords:
            i.x=i.x-min[0]
            i.y=i.y-min[1]
            print(i)
    
    def draw_a(self, file_name:str):
        self.init_a(Parser(file_name))
        self.draw_non_closed_shape()

    def init_s(self,coordParser:Parser):
        coords=coordParser.tuple_to_vector()
        for i in coords:
            i.x=(i.x-75.0)/100.0-3.0        
            i.y=(i.y-83.080841)/100.0-1.0
        return coords

    def scale_offset_s(self,data_file_name:str):
        pos=self.init_s(Parser(data_file_name))
        for i in pos:
            i.x=i.x*10.0
            i.y=i.y*10.0
            i.x=i.x+2.0
            i.y=i.y+2.0
        return pos

    def draw_s(self, data_file_name:str):
        self.pos=self.scale_offset_s(data_file_name)
        self.draw_non_closed_shape()

    def init_l(self):
        pos=[
            Vector2(0.0, -1.0),Vector2(0.0, 1.0)
        ]
        return pos
    
    def init_l_diagonal(self, angle:float, factor:Vector2, offset:Vector2):
        self.pos=self.init_l()
        self.scale_and_offset( factor, offset)
        self.rotate_anticlockwise(angle)

    def draw_l(self):
        self.pos=self.init_l()
        self.draw_non_closed_shape()

    def draw_cl(self):
        pos_c=self.init_c()
        self.pos=self.init_l()
        self.translate(Vector2(24.0,0.0))
        pos_c+=self.pos
        self.pos=pos_c

        for i in range(0,len(self.pos)):
            j=i+1
            if j==len(self.pos):
                break
            if i==len(self.pos)-3:
                continue
            self.pen.line([(self.pos[i].x, self.pos[i].y),( self.pos[j].x, self.pos[j].y)], self.color, 1)

        self.image.save(self.file_name, 'PNG')

    def draw_methyl_diagonal(self, angle:float, translation_offset:Vector2):
        pos=self.init_l()
        self.pos=rotate_anticlockwise(angle, pos)
        self.translate(translation_offset)
        self.draw_non_closed_shape()

    def draw_chlorpheniramine(self):
        pos_c=self.init_c()
        self.pos=self.init_l()
        self.scale_and_offset(Vector2(10.0, 10.0), Vector2(0.0, 10.0))
        self.translate(Vector2(24.0,0.0))
        pos_c+=self.pos
        self.init_l_diagonal(19.5/180.0*pi, Vector2(10.0, 18.0), Vector2(-4.0, 18.0))
        self.translate(Vector2(36.0, 20.0 )) #size=( 44.0, 40.0)
        pos_c+=self.pos
        self.pos=self.init_benzene()
        self.translate(Vector2(44.0, 8.0)) #size=(224, 240)
        pos_c+=self.pos
        self.pos=pos_c

        for i in range(0, len(self.pos)):
            j=i+1
            if j==len(self.pos):
                break
            if i==len(self.pos)-19 or i==len(self.pos)-17 or i==len(self.pos)-15:
                continue
            if i>=len(self.pos)-14:
                if i < len(self.pos)-7:
                    self.pen.line([(self.pos[i].x, self.pos[i].y), (self.pos[j].x,  self.pos[j].y)], fill=self.color,width=1)
                if i == len(self.pos)-7:
                    self.pen.line([(self.pos[len(self.pos)-7].x, self.pos[len(self.pos)-7].y), (self.pos[len(self.pos)-14].x, self.pos[len(self.pos)-14].y)], fill=self.color, width=1)
                if i >= 8:
                    self.pen.line([(self.pos[len(self.pos)-6].x,  self.pos[len(self.pos)-6].y),  (self.pos[len(self.pos)-5].x, self.pos[len(self.pos)-5].y)], fill=self.color, width=1)
                    self.pen.line([(self.pos[len(self.pos)-4].x, self.pos[len(self.pos)-4].y),   (self.pos[len(self.pos)-3].x, self.pos[len(self.pos)-3].y)], fill=self.color, width=1)
                    self.pen.line([(self.pos[len(self.pos)-2].x, self.pos[len(self.pos)-2].y),   (self.pos[len(self.pos)-1].x, self.pos[len(self.pos)-1].y)], fill=self.color, width=1)
            else:
                self.pen.line([(self.pos[i].x, self.pos[i].y),( self.pos[j].x, self.pos[j].y)], self.color, 1)
        
        self.image.save(self.file_name, 'PNG')