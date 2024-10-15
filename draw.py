from math import pi, sin, cos, tan
from image_editor import ImageEditing
from vec2d import Vector2

RED_OPAQUE=(255,0,0,255)
WHITE_OPAQUE=(255,255,255,255)
DARK_GREEN_OPAQUE=(49,101,46, 255)
BLACK_OPAQUE=(0,0,0, 255)
DARK_GREEN_TRANSLUCENT=(49,101,46, 0)
LIGHT_GREEN_OPAQUE=(78,132, 51,255)
GREY=(192, 192, 192,255)
BLUE_OPAQUE=(55,34,142, 255)
YELLOW_OPAQUE=(191,173,13, 255)
GREEN_BLUE_OPAQUE=(64,128,128, 255)


ANGLE=21/180*pi

class Diagonal(ImageEditing):
    def __init__(self, fileName: str, file_size: tuple = (200,200), color: tuple = (0,204,102,255), mode: str = 'new') -> None:
        super().__init__(fileName, file_size, color, mode)

    def init_coords(self):
        pos=[
            Vector2(0.0, 0.935), Vector2(0.375, 1),
            Vector2(0.821, 0.936), Vector2(0.445, 0.871),
            Vector2(0.0, 0.935), Vector2(0.187, 0.967),
            Vector2(0.633, 0.923)

        ]
        return pos
    
    def draw_diagonal(self):
        self.pos=self.init_coords()
        self.scale(Vector2(200.0, 200.0))
        self.conv_vec2d_to_tuple()
        for i in range(0, len(self.pos)):
            j=i+1
            if j>len(self.pos)-1:
                break
            self.pen.line([self.pos[i],self.pos[j]], self.color)
        self.image.save(self.file_name, 'PNG')

    def draw_diagonal_opponent_all(self):
        width=self.image.width
        for i in range(0, 100):
            self.pen.line([(0.0, i*10-100),(width, width*tan(pi/6)-100+i*10)], self.color)
        self.image.save(self.file_name, 'PNG')        

    def draw_diagonal_all(self):
        width=self.image.width
        height=self.image.height
        for i in range(0, 100):
            self.pen.line([(0.0, height-i*10+100),(width, 100+height-width*tan(pi/6)-i*10)], self.color)
        self.image.save(self.file_name, 'PNG')

def main():
    diagonal_opp=Diagonal('images/opp_all.png')
    diagonal_opp.draw_diagonal()

if __name__=='__main__':
    main()










