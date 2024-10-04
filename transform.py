from vec2d import Vector2
from vec2d import single_point_rotate_clockwise
from json import dump

class Transform:
    def __init__(self, file_content) -> None:
        self.file_content=file_content

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
        self.file_content= [Vector2(i[0], i[1]) for i in self.file_content]
    
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
        self.file_content=[ single_point_rotate_clockwise(0, Vector2(i.x-self.center[0], i.y-self.center[1])) for i in self.file_content]

    def do_after_read(self): # do not forget to call this method when to draw
        self.min=self.finding_min_max_from_vector()[0]
        self.max=self.finding_min_max_from_vector()[1]
        self.center=self.find_center()
        self.dimension=self.find_object_dimension()
        self.scale_object(Vector2(1/(self.dimension[1]/100), 1/(self.dimension[1]/100)))
        self.centralize_object()
        self.move_object_into_canvas()
        self.rotate_object_from_anywhere()
        self.move_object_into_canvas_by_some(Vector2(0, 0))

    def find_min_max_mid(self, positions:list[Vector2]):
        min_x=min(pos.x for pos in positions)
        
        for i in range(len(positions)):
            if positions[i].x!=min_x:
                offset=positions[i].x-min_x
                positions[i].x-=2*offset

    def swap_middle_control_points(self):
        for i in range(0,len(self.file_content),4):
            group=self.file_content[i:i+4]
            if len(group)==4:
                self.find_min_max_mid(group)

    def vec2d_to_dict(self, pos:Vector2):
        return {"Vector2": {'x': pos.x , 'y': pos.y }}

    def serialize(self):
        vectors_dict=[self.vec2d_to_dict(v) for v in self.file_content]
        controlPoints={"ControlPoints": vectors_dict}

        with open('output_test_better.json','w') as file:
            dump(controlPoints, file, indent=4)