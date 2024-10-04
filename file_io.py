import re
from copy import deepcopy
from vec2d import Vector2

class File:
    def __init__(self, file_name_to_read:str) -> None:
        self.file_content=[]
        self.file_name=file_name_to_read
        
    def __init__(self)->None:
        self.file_content=[]
    def read_file(self):
        with open(self.file_name, 'r') as file:
            self.file_content=file.readlines()
            file.close()

    def write_file(self, filePath:str, object_to_write:list[str]):
        with open(filePath, 'w') as file:
            file.writelines(object_to_write)
            file.close()
