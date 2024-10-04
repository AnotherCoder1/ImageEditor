from file_io import File
from vec2d import Vector2,single_point_rotate_clockwise
from math import pi
from json import load,loads, dumps, dump
from copy import deepcopy
from json_parser import JsonParser

class Parser(File):
    def __init__(self, file_name_to_read: str) -> None:
        super().__init__(file_name_to_read)
        self.read_file()
        self.begin_line_number=self.get_line_begin_number()

    def parse_coord_file(self):
        if self.begin_line_number==-1:
            self.begin_line_number=len(self.file_content)
        self.file_content = [
            tuple(map(float, string.replace('(', '').replace(')', '').split(','))) if i < self.begin_line_number
            else tuple(map(float, string.replace('L: ', '').replace('(', '').replace(')', '').split(',')))
            for i, string in enumerate(self.file_content)
        ]

    def scale_object(self, scale_factor:Vector2):
        self.file_content=[Vector2(i.x*scale_factor.x, i.y*scale_factor.y) for i in self.file_content]
        self.min=self.finding_min_max_from_vector()[0]
        self.max=self.finding_min_max_from_vector()[1]
        self.center=self.find_center()
        self.dimension=self.find_object_dimension()    
    
    def finding_min_max_from_tuple(self):
        all_x = [i[0] for i in self.file_content]
        all_y = [i[1] for i in self.file_content]
        minimum = [min(all_x), min(all_y)]
        maximum = [max(all_x), max(all_y)]
        return [minimum, maximum]
    
    def finding_min_max_from_vector(self):
        all_x = [i.x for i in self.file_content]
        all_y = [i.y for i in self.file_content]
        minimum = [min(all_x), min(all_y)]
        maximum = [max(all_x), max(all_y)]
        return [minimum, maximum]

    
    def tuple_to_vector(self):
        self.file_content = [Vector2(i[0], i[1]) for i in self.file_content]
    
    def find_center(self):
        centerX=(self.min[0]+self.max[0])/2.0
        centerY=(self.min[1]+self.max[1])/2.0
        return centerX,centerY
 
    def check_min_max_and_content(self):
        [print(i) for i in self.file_content]
        print(f'min: {self.min}, max: {self.max}')

    def centralize_object(self):
        self.file_content=[Vector2(i.x-self.center[0], i.y-self.center[1]) for i in self.file_content]

    def find_object_dimension(self):
        width=self.max[0]-self.min[0]
        height=self.max[1]-self.min[1]
        return width, height

    def move_object_into_canvas(self):
        self.file_content=[Vector2(i.x+self.dimension[0]/2, i.y+self.dimension[1]/2 )for i in self.file_content]

    def move_object_into_canvas_by_some(self, offset:Vector2):
        self.file_content=[Vector2(i.x+(self.dimension[0]/2+offset.x), i.y+(self.dimension[1]/2+offset.y) )for i in self.file_content]

    def rotate_object_from_anywhere(self):
        self.min=self.finding_min_max_from_vector()[0]
        self.max=self.finding_min_max_from_vector()[1]
        self.center=self.find_center()
        self.file_content=[ single_point_rotate_clockwise(pi, Vector2(i.x-self.center[0], i.y-self.center[1])) for i in self.file_content]

    def get_line_begin_number(self):
        for i, string in enumerate(self.file_content):
            if 'L' in string:
                return i
        return -1

    def do_after_read(self): # do not forget to call this method when to draw
        self.parse_coord_file()
        self.min=self.finding_min_max_from_tuple()[0]
        self.max=self.finding_min_max_from_tuple()[1]
        self.center=self.find_center()
        self.dimension=self.find_object_dimension()
        self.tuple_to_vector()
        self.scale_object(Vector2(1/(self.dimension[1]/100), 1/(self.dimension[1]/100)))
        self.centralize_object()
        self.move_object_into_canvas()
        self.rotate_object_from_anywhere()
        self.move_object_into_canvas_by_some(Vector2(0, 0))



