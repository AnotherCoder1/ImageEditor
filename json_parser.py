from vec2d import Vector2
from json import load

class JsonParser:
    def __init__(self, file_name_to_read: str) -> None:
        self.file_name=file_name_to_read
        self.file_content=self.parse_into_bezier()

    def parse_into_bezier(self):
        with open(self.file_name, 'r') as file:
            raw=load(file)
    
        unparsed=raw["ControlPoints"]

        return [Vector2(unparsed[i]['Vector2']['x'], unparsed[i]['Vector2']['y'])for i in range(0, len(unparsed))]
    
    def parse_money(self):
        with open(self.file_name, 'r') as file:
            raw=load(file)

        return raw['FP']