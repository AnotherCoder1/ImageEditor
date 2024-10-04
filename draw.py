from math import pi
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

#a=min(375.0, 180.7566), max:(625.0, 409.177399)
def main():
    d=ImageEditing("images/d.png", (100,100), RED_OPAQUE, 'open')
    d.resize(Vector2(100,100), 'images/d.png')

    e=ImageEditing("images/e.png", (100,100), RED_OPAQUE, 'open')
    e.resize(Vector2(100,100), 'images/e.png')

    left=ImageEditing("images/left.png", (100,100), RED_OPAQUE, 'open')
    left.resize(Vector2(100,100), 'images/left.png')

    right=ImageEditing("images/right.png", (100,100), RED_OPAQUE, 'open')
    right.resize(Vector2(100,100), 'images/right.png')

    up=ImageEditing("images/up.png", (100,100), RED_OPAQUE, 'open')
    up.resize(Vector2(100,100), 'images/up.png')

if __name__=='__main__':
    main()










