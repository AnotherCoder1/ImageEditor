from image_editor import ImageEditing
from drawing_parser import Parser,JsonParser,Transform
from bezier_curve import BezierCurve
from copy import deepcopy
from vec2d import Vector2, rotate_clockwise
from math import pi
from line import Line


class BezierDrawing(ImageEditing):
    def __init__(self, fileName_out: str, file_to_parsed:str, file_size: tuple=(140,100), color: tuple=(127,127,127,255), mode: str='new') -> None:
        super().__init__(fileName_out, file_size, color, mode)
        self.file=Parser(file_to_parsed)
        self.file.do_after_read()
        self.curve_collection=[BezierCurve(positions=[self.file.file_content[0], self.file.file_content[1], 
                                                              self.file.file_content[2], self.file.file_content[3]])]
        self.control_points_count=self.get_control_points_count()
        self.add_more_curve()
        self.line_collection=[Line]
        self.add_more_lines()

    def get_control_points_count(self):
        return len(self.file.file_content)
    
    def add_more_curve(self):
        self.curve_collection.extend([BezierCurve(positions=[self.file.file_content[i+0], self.file.file_content[i+1], 
                                                              self.file.file_content[i+2], self.file.file_content[i+3]])
            for i in range(0, self.control_points_count) if i%4==0 and i!=0 and i<self.control_points_count-3])
        
    def add_more_lines(self):
        if self.file.begin_line_number!=-1:
            self.line_collection=[Line(self.file.file_content[i+0], self.file.file_content[i+1] ) 
                                  for i in range(self.file.begin_line_number, len(self.file.file_content)) if i%2==0]
        
    def draw_single_bezier_curve(self, angle:float, dimension:Vector2):
        self.pos=rotate_clockwise(angle, self.pos)
        if angle>=0 and angle<pi/2:
            self.translate(dimension) #0 to 90 degree
        elif angle>=pi/2 and angle<pi:
            self.translate(Vector2(0,dimension.x)) #90 to 270 degree
        elif angle>=pi and angle<3*pi/2:
            self.translate(Vector2(dimension.x,0)) #180 degree
        else:
            self.translate(Vector2(dimension.y,dimension.x)) #270 degree
        self.curvePoints[0]=self.pos[0]
        for i in range(0,101):
            j=i+1
            t=i/100
            point=self.curve_collection[0].find_point(t)
            self.curve_collection[0].drawing_points.append(deepcopy(point))
            self.pen.line([(self.curve_collection[0].drawing_points[i].x, self.curve_collection[0].drawing_points[i].y),
                           (self.curve_collection[0].drawing_points[j].x, self.curve_collection[0].drawing_points[j].y)], self.color, 1)
            self.image.save(self.file_name, 'PNG')
        
    def draw(self):
        for count in range(len(self.curve_collection)):
            for i in range(100):
                j=i+1
                t=i/100.0
                point=self.curve_collection[count].find_point(t)
                self.curve_collection[count].drawing_points.append(deepcopy(point))
                self.pen.line([
                    ( self.curve_collection[count].drawing_points[i].x, self.curve_collection[count].drawing_points[i].y ),
                    ( self.curve_collection[count].drawing_points[j].x, self.curve_collection[count].drawing_points[j].y )
                    ], self.color, 1)
                
        for line in range(len(self.line_collection)):
            self.pen.line([(self.line_collection[line].points[0].x, self.line_collection[line].points[0].y),
                           (self.line_collection[line].points[1].x, self.line_collection[line].points[1].y)], self.color, 1)
        self.image.save(self.file_name, 'PNG')


class JsonBezierDrawing(ImageEditing):
    def __init__(self, fileName_out: str, file_to_parsed:str, file_size: tuple=(140,100), color: tuple=(127,127,127,255), mode: str='new') -> None:
        super().__init__(fileName_out, file_size, color, mode)
        self.json_parser=JsonParser(file_to_parsed)
        self.transform=Transform(self.json_parser.file_content)
        self.transform.do_after_read()
        self.curve_collection=[BezierCurve(positions=[self.json_parser.file_content[0], self.json_parser.file_content[1], 
                                                              self.json_parser.file_content[2], self.json_parser.file_content[3]])]
        self.control_points_count=self.get_control_points_count()
        self.add_more_curve()

    def get_control_points_count(self):
        return len(self.json_parser.file_content)
    
    def add_more_curve(self):
        self.curve_collection.extend([BezierCurve(positions=[self.json_parser.file_content[i+0], self.json_parser.file_content[i+1], 
                                                              self.json_parser.file_content[i+2], self.json_parser.file_content[i+3]])
            for i in range(0, self.control_points_count) if i%4==0 and i!=0 and i<self.control_points_count-3])
        
    def draw_single_bezier_curve(self, angle:float, dimension:Vector2):
        self.pos=rotate_clockwise(angle, self.pos)
        if angle>=0 and angle<pi/2:
            self.translate(dimension) #0 to 90 degree
        elif angle>=pi/2 and angle<pi:
            self.translate(Vector2(0,dimension.x)) #90 to 270 degree
        elif angle>=pi and angle<3*pi/2:
            self.translate(Vector2(dimension.x,0)) #180 degree
        else:
            self.translate(Vector2(dimension.y,dimension.x)) #270 degree
        self.curvePoints[0]=self.pos[0]
        for i in range(0,101):
            j=i+1
            t=i/100
            point=self.curve_collection[0].find_point(t)
            self.curve_collection[0].drawing_points.append(deepcopy(point))
            self.pen.line([(self.curve_collection[0].drawing_points[i].x, self.curve_collection[0].drawing_points[i].y),
                           (self.curve_collection[0].drawing_points[j].x, self.curve_collection[0].drawing_points[j].y)], self.color, 1)
            self.image.save(self.file_name, 'PNG')
        
    def draw(self):
        for count in range(len(self.curve_collection)):
            for i in range(100):
                j=i+1
                t=i/100.0
                point=self.curve_collection[count].find_point(t)
                self.curve_collection[count].drawing_points.append(deepcopy(point))
                self.pen.line([
                    ( self.curve_collection[count].drawing_points[i].x, self.curve_collection[count].drawing_points[i].y ),
                    ( self.curve_collection[count].drawing_points[j].x, self.curve_collection[count].drawing_points[j].y )
                    ], self.color, 1)
                
        self.image.save(self.file_name, 'PNG')


    