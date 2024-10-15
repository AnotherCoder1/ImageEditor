from PIL import Image,ImageDraw
from vec2d import Vector2, rotate_clockwise, rotate_anticlockwise,single_point_rotate_clockwise
from math import pi
from copy import deepcopy
from file_io import File

WHITE_TRANSPARENT=(255,255,255,0)
ANGLE=21/180*pi

class ImageEditing:
    def __init__(self, fileName:str, file_size:tuple=(100,100), color:tuple=(0,0,0,255), mode:str='new') -> None:
        self.file_name=fileName
        self.file_size=file_size
        self.mode=mode
        self.image=self.decide(mode)
        self.pen=ImageDraw.Draw(self.image)
        self.color=color
        self.pos=[]

    def close(self):
        if self.image and hasattr(self.image, 'fp') and self.image.fp:
            self.image.close()


    def decide(self, mode:str):
        if mode=='new':
            return Image.new('RGBA', self.file_size, WHITE_TRANSPARENT)
        if mode=='open':
            return Image.open(self.file_name)

    def crop(self, posStart:Vector2, posEnd:Vector2, filePath:str):
        cropped_image=self.image.crop((posStart.x, posStart.y, posEnd.x, posEnd.y ))
        cropped_image.save(filePath)

    def resize(self, size:Vector2, filePath:str):  #open file
        resized=self.image.resize((size.x, size.y))
        resized.save(filePath)

    def merge_image_files(self, file_paths:list[str], coords:list[tuple]): #new file
        images=[]
        if len(file_paths)!=0:
            for i in range(0,len(file_paths)):
                image=Image.open(file_paths[i])
                images.append(deepcopy(image))

            output_image=Image.new('RGBA', self.file_size)
            for i in range(0, len(coords)):
                output_image.paste(images[i], coords[i])
            output_image.save(self.file_name, 'PNG')
        else:
            return

    def conv_vec2d_to_tuple(self):
        temp=[]
        for i in self.pos:
            tuple_vec=(i.x, i.y)
            temp.append(deepcopy(tuple_vec))
        self.pos.clear()
        self.pos=temp

    def conv_part_vec2d_to_tuple(self, begin:int, end:int):
        temp=[]
        if begin<len(self.pos)-1 and end==len(self.pos)-1:
            for i in range(begin, end+1):
                tuple_vec=(self.pos[i].x, self.pos[i].y )
                temp.append(deepcopy(tuple_vec))
            return temp
        else:
            return

    def set_background_color(self, background_color):
        self.image=Image.new('RGBA', self.file_size, background_color)


    def conv_vec3d_to_vec2d(self):
        poss=[]
        for i in self.pos:
            temp=Vector2(0.0, 0.0)
            temp.x=i.x
            temp.y=i.y
            poss.append(deepcopy(temp))
        self.pos.clear()
        self.pos=poss


    def translate(self, offset:Vector2):
        for i in self.pos:
            i.x=i.x+offset.x
            i.y=i.y+offset.y

    def translate_partly(self, min,max, offset:Vector2):
        if min<0 or max>len(self.pos):
            return
        for i in range(min,max):
            self.pos[i].x=self.pos[i].x+offset.x
            self.pos[i].y=self.pos[i].y+offset.y

    def scale(self, factor:Vector2):
        for i in self.pos:
            i.x=i.x*factor.x
            i.y=i.y*factor.y

    def scale_and_offset(self, factor:Vector2, offset:Vector2):
        for i in self.pos:
            i.x=i.x*factor.x+offset.x
            i.y=i.y*factor.y+offset.y

    def scale_and_offset_part(self, min:int, max:int, factor:Vector2, offset:Vector2):
        if min<0 or max>len(self.pos):
            return
        for i in range(min,max):
            self.pos[i].x=self.pos[i].x*factor.x+offset.x
            self.pos[i].y=self.pos[i].y*factor.y+offset.y
    
    def rotate_clockwise(self,angle:float):
        self.pos=rotate_clockwise(angle, self.pos)
        

    def rotate_anticlockwise(self,angle:float):
        self.pos=rotate_anticlockwise(angle, self.pos)
        
    def draw_non_closed_shape(self):
        for i in range(0, len(self.pos)):
            j=i+1
            if j==len(self.pos):
                break
            self.pen.line([(self.pos[i].x, self.pos[i].y),( self.pos[j].x, self.pos[j].y)], self.color, 2)
        self.image.save(self.file_name, 'PNG')

    def draw_closed_shape(self):
        for i in range(0, len(self.pos)):
            j=i+1
            self.pen.line([(self.pos[i].x, self.pos[i].y),( self.pos[j%len(self.pos)].x, self.pos[j%len(self.pos)].y)], self.color, 1)
        self.image.save(self.file_name, 'PNG')

    def draw_filled_closed_shape(self):
        for i in range(0,len(self.pos)):
            j=i+1
            k=i+2
            if j==len(self.pos) or k==len(self.pos):
                break
            self.pen.polygon([(self.pos[i].x, self.pos[i].y),(self.pos[j].x, self.pos[j].y),(self.pos[k].x, self.pos[k].y)], self.color, self.color)
        self.image.save(self.file_name, 'PNG')


    def draw_multiple_lines(self, lines:list[Vector2]):
        if len(lines)==0 or len(lines)%2!=0:
            return
        for i in range(0, len(lines),2):
            j=i+1
            self.pen.line([(lines[i].x, lines[i].y),(lines[j].x, lines[j].y)], self.color,2)
        self.image.save(self.file_name, 'PNG')

    def read_pixel_value(self, coord:Vector2):
        color=self.image.getpixel((int(coord.x), int(coord.y)))
        return color
    
    def resize_image_wo_aspect_ratio(self, new_size:tuple):
        if self.mode=='open':
            new_image=self.image.resize(new_size)
        new_image.save(self.file_name, 'PNG')

    def write_to_txt_file(self, txt_file_name:str):
        if self.mode=='open':
            datas=self.image.getdata()
            with open(txt_file_name, 'a') as file:
                content=""
                for elem in datas:
                    content+=str(elem)
                    content+='\n'
                file.write(content)
                file.close()

    def clear_image_file(self,image_file_size:tuple):
        if self.mode=='open':
            draw=ImageDraw.Draw(self.image)
            draw.line([(0,0),image_file_size], WHITE_TRANSPARENT, image_file_size[0])
            self.image.save(self.file_name)







    




















