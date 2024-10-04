from image_editor import ImageEditing
from vec2d import Vector2, Vector3
from math import pi

class Football(ImageEditing):
    def __init__(self, fileName: str, file_size: tuple = (7680,1500), color: tuple = (7, 93, 38, 255), mode: str = 'new') -> None:
        super().__init__(fileName, file_size, color, mode)

    def init_goal_post(self):
        pos=[
           Vector2(0.0, 6.1), Vector2(0.0, 3.66),
           Vector2(6.34, 0.0), Vector2(7.34, 0.0),
           Vector2(1.0,3.66), Vector2(1.0, 6.1),
           Vector2(0.0, 6.1), Vector2(6.34, 2.44),
           Vector2(7.34, 2.44)
        ]
        return pos
    
    def draw_goal_post(self, thickness:int):
        self.pos=self.init_goal_post()
        self.scale(Vector2(52.6315, 52.6315))
        for i in range(0, len(self.pos)):
            j=i+1
            if j==len(self.pos) or i==5:
                break
            self.pen.line([(self.pos[i].x, self.pos[i].y),(self.pos[j].x, self.pos[j].y)], self.color, thickness)

        self.pen.line([(self.pos[1].x, self.pos[1].y),(self.pos[4].x, self.pos[4].y)], self.color, thickness)
        self.pen.line([(self.pos[2].x, self.pos[2].y),(self.pos[7].x, self.pos[7].y)], self.color, thickness)
        self.pen.line([(self.pos[3].x, self.pos[3].y),(self.pos[8].x, self.pos[8].y)], self.color, thickness)
        self.pen.line([(self.pos[0].x, self.pos[0].y),(self.pos[5].x, self.pos[5].y)], self.color, thickness)
        self.pen.line([(self.pos[7].x, self.pos[7].y),(self.pos[8].x, self.pos[8].y)], self.color, thickness)
        self.pen.line([(self.pos[0].x, self.pos[0].y),(self.pos[7].x, self.pos[7].y)], self.color, thickness)
        self.pen.line([(self.pos[5].x, self.pos[5].y),(self.pos[8].x, self.pos[8].y)], self.color, thickness)

        # background=self.conv_part_vec2d_to_tuple(5,6)
        # background.append((73.2, 31.3))
        # self.pen.polygon(background, color, color)

        self.image.save(self.file_name, 'PNG')

    def init_pitch(self):
        pos=[
            Vector2(0.0, 50.0), Vector2(58.889, 16.0),
            Vector2(11.6 ,50.0),  Vector2(70.489,16.0),
            Vector2(23.2 ,50.0),  Vector2(82.089,16.0),
            Vector2(34.8 ,50.0),  Vector2(93.689,16.0),
            Vector2(46.4 ,50.0),  Vector2(105.289,16.0),
            Vector2(58.0 ,50.0),  Vector2(116.889,16.0),
            Vector2(69.6 ,50.0),  Vector2(128.489,16.0),
            Vector2(81.2 ,50.0),  Vector2(140.089,16.0),
            Vector2(92.8 ,50.0),  Vector2(151.689,16.0),
            Vector2(104.4,50.0), Vector2( 163.289,16.0),
            Vector2(116.0,50.0), Vector2( 174.889,16.0),
            Vector2(127.6,50.0), Vector2( 186.489,16.0),
            Vector2(139.2,50.0), Vector2( 198.089,16.0),
            Vector2(150.8,50.0), Vector2( 209.689,16.0),
            Vector2(162.4,50.0), Vector2( 221.289,16.0),
            Vector2(174.0,50.0), Vector2( 232.889,16.0),
            Vector2(185.6,50.0), Vector2( 244.489,16.0), 
            Vector2(197.2, 50.0), Vector2(256.089, 16.0) 
        ]
        return pos
    
    def draw_pitch(self, light_color:tuple):
        self.pos=self.init_pitch()
        self.scale(Vector2(30.0, 30.0))
        for (i,elem) in enumerate(self.pos):
            j=i*2
            k=j+1
            l=k+1
            m=l+1
            if j>len(self.pos)-1 or k>len(self.pos)-1 or l>len(self.pos)-1 or m> len(self.pos)-1:
                break
            if i%2==0:
                self.pen.polygon(
                    [
                        (self.pos[j].x, self.pos[j].y),(self.pos[k].x, self.pos[k].y), (self.pos[l].x, self.pos[l].y),
                        (self.pos[k].x, self.pos[k].y),(self.pos[m].x, self.pos[m].y), (self.pos[l].x, self.pos[l].y)
                        
                    ], self.color, width=1)
            else:
                self.pen.polygon(
                    [
                    (self.pos[j].x, self.pos[j].y),(self.pos[k].x, self.pos[k].y), (self.pos[l].x, self.pos[l].y),
                    (self.pos[k].x, self.pos[k].y),(self.pos[m].x, self.pos[m].y), (self.pos[l].x, self.pos[l].y)
                    ], 
                    light_color, width=1)

        self.image.save(self.file_name, 'PNG')

    def init_second_goal_post(self):
        pos=[
            Vector2(7.287, 3.133),Vector2(7.287, 0.693),
            Vector2(1.0, 0.0),Vector2(0.0, 0.0),
            Vector2(6.287, 0.693), Vector2(6.287, 3.133),
            Vector2(0.0, 2.44)
        ]
        return pos

    def draw_second_goal(self, thickness:int, background_color:tuple):
        self.pos=self.init_goal_post()
        self.scale(Vector2(40.3175,40.3175))

        # self.pen.polygon([(0.0, 0.0),(53.39,0.0),(0.0, 36.6)], background_color, background_color)
        # self.pen.polygon([(0.0, 36.6),(53.39,0.0),(self.pos[2].x, self.pos[2].y)], background_color, background_color)
        # self.pen.polygon([(self.pos[2].x, self.pos[2].y), (53.39,0.0), (73.39, 0.0)], background_color, background_color)
        # self.pen.polygon([(73.39,0.0),(self.pos[2].x, self.pos[2].y), (self.pos[3].x, self.pos[3].y)], background_color, background_color)
        # self.pen.polygon(
        #     [(self.pos[0].x, self.pos[0].y),(self.pos[1].x, self.pos[1].y),(self.pos[2].x, self.pos[2].y),
        #      (self.pos[2].x, self.pos[2].y),(53.39, 43.0),(self.pos[0].x, self.pos[0].y)], background_color, background_color)
        
        # self.pen.polygon(
        #     [(self.pos[2].x, self.pos[2].y),(self.pos[3].x, self.pos[3].y),(53.39, 43.0),
        #      (self.pos[3].x, self.pos[3].y),(self.pos[6].x, self.pos[6].y),(53.39, 43.0)], 
        #      background_color, background_color)

        for i in range(0, len(self.pos)):
            j=i+1
            if j==len(self.pos):
                break
            self.pen.line([(self.pos[i].x, self.pos[i].y),(self.pos[j].x, self.pos[j].y)], self.color, thickness)
        
        self.pen.line([(self.pos[1].x, self.pos[1].y), (self.pos[4].x, self.pos[4].y)], self.color, thickness)
        self.pen.line([(self.pos[3].x, self.pos[3].y), (self.pos[6].x, self.pos[6].y)], self.color, thickness)
        self.pen.line([(self.pos[0].x, self.pos[0].y),(self.pos[5].x, self.pos[5].y)], self.color, thickness)
        #self.pen.line([(self.pos[2].x, self.pos[2].y),(53.39, 43.0)], self.color, thickness)  
        #self.pen.line([(53.39, 43.0),(self.pos[6].x, self.pos[6].y)], self.color, thickness)      

        self.image.save(self.file_name, 'PNG')

    def init_ellipse(self, width:float, height:float):
        pos=[
            Vector2(0.0, 0.0), Vector2(width, height)
        ]
        return pos
    
    def draw_player(self):
        self.pos=self.init_circle_32()
        self.scale_and_offset(Vector2(5.0,5.0), Vector2(7.0, 7.0))
        self.conv_vec2d_to_tuple()
        self.pen.polygon(self.pos, self.color, self.color)
        self.pos.clear()

        self.pos=self.init_ellipse(1.0, 5.0)
        self.scale(Vector2(5.0,5.0))
        self.rotate_anticlockwise(pi/6)
        self.translate(Vector2(14.0,5.0))
        self.conv_vec2d_to_tuple()
        self.pen.ellipse(self.pos, self.color, self.color)
        self.pos.clear()

        self.pos=self.init_ellipse(1.0, 7.0)
        self.scale_and_offset(Vector2(5.0,5.0), Vector2(3.0, 5.0))
        self.conv_vec2d_to_tuple()
        self.pen.ellipse(self.pos, self.color, self.color)
        self.image.save(self.file_name, 'PNG')

LIGHT_GREEN=(23,171,50,255)
