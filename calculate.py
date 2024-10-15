from math import cos, sin,pi

ANGLE=pi/6
WIDTH=48.496
HEIGHT=164
HYPOTENUSE=25

def find_width(hypotenuse:float=HYPOTENUSE, angle:float=ANGLE):
    return hypotenuse*cos(angle)

def find_height(hypotenuse:float=HYPOTENUSE, angle:float=ANGLE):
    return hypotenuse*sin(angle)

def norm_width(any:float):
    return any/WIDTH

def norm_height(any:float):
    return any/HEIGHT

def get_absolute_normalized_height(any:float):
    return 1-any

def main():
    print(f'width: {norm_width(find_width())}') #width
    print(f'height: {get_absolute_normalized_height(norm_height(find_height()))}') #height

if __name__=='__main__':
    main()