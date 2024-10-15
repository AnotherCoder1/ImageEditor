from image_editor import ImageEditing
from vec2d import Vector2
from PIL import Image
from copy import deepcopy
from file_io import File

class CustomEditing(ImageEditing):
    def __init__(self, player_name:str ,fileName: str='', file_size: tuple = (288,933), color: tuple = (0, 0, 0, 255), mode: str = 'new') -> None:
        super().__init__(fileName, file_size, color, mode)
        self.player_name=player_name
        self.init_file_name()


    def init_file_name(self):
            self.file_name=f'C:\\Users\\lutfi\\Desktop\\kotlin_projects\\multi-platform\\football_2d\\assets\\animation\\{self.player_name}\\{self.player_name}0.png'


    def unsaved_resize(self, size:Vector2):
        self.image=self.image.resize((size.x, size.y))

    def unsaved_merge_image_files(self, file_paths:list[str], coords:list[tuple]):
        images=[]
        if len(file_paths)!=0:
            for i in range(0,len(file_paths)):
                image=Image.open(file_paths[i])
                images.append(deepcopy(image))

            for i in range(0, len(coords)):
                self.image.paste(images[i], coords[i])
        else:
            return

    def merge_head_and_body(self, animated_sprite:str, frame_number:int): #(288, 808)
        self.file_name=f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_{animated_sprite+str(frame_number)}.png'
        
        match self.player_name:
            case 'casemiro':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\casemiro.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'dalot':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\dalot.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'kambwala':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\kambwala.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'maguire':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\maguire.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'onana':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\onana.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'wan_bissaka':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\wan_bissaka.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'mainoo':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\mainoo.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'rashford':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\rashford.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'garnacho':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\garnacho.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'bruno':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\bruno.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])
            case 'hojlund':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\{animated_sprite}\\{animated_sprite+str(frame_number)}.png','C:\\Users\\lutfi\\Desktop\\game_assets\\drawing\\optimized\\hojlund.png'], [(0,0),self.find_head_pos(animated_sprite, frame_number)])

        self.unsaved_resize(Vector2( 100, 300))
        self.image.save(self.file_name, 'PNG')

    def merge_sprite_frames(self, animation_type:str): #(302,300)
        self.file_name=f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_{animation_type}.png'

        match animation_type:
            case 'run':
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_run0.png',
                                                f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_run1.png',
                                                f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_run2.png'
                                                ], [(0,0),(101,0), (202,0)])

                self.unsaved_resize(Vector2(102, 100))
                self.image.save(self.file_name, 'PNG')
            
            case _:
                self.unsaved_merge_image_files([f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_{animation_type}0.png',
                                                f'C:\\Users\\lutfi\\Desktop\\game_assets\\animation\\PartialSprite\\{self.player_name}\\{self.player_name}_{animation_type}1.png'
                                                ], [(0,0),(101,0)])

                self.unsaved_resize(Vector2(102, 100))
                self.image.save(self.file_name, 'PNG')

    def find_head_pos(self, animation_type:str, frame_number:int):
        match animation_type:
            case 'standing':
                return (62, 70)
            case 'run':
                return (52,10)
            case 'pass':
                if frame_number==0:
                    return (190, 20)
                else:
                    return (90, 60)
            case 'tackling':
                if frame_number==0:
                    return (70, 40)
                else:
                    return (186, 123)
                
            case _:
                return (0,0)


def tuple_to_str(vector2d:tuple):
    return "({},{},{}),".format(vector2d[0], vector2d[1], vector2d[2])


def write_pixels_to_file(file_to_open:str):
    write=File()
    shape=ImageEditing('images/cat_eat_chicken.png', mode='open')
    colors=[]

    for y in range(0,100):
        for x in range(0,100):
            colors.append(deepcopy(tuple_to_str(shape.read_pixel_value(Vector2(x,y)))))
    
    
    write.write_file("images/test",colors)


bruno_color=(239, 209, 160, 255)
casemiro_color=(185, 122, 86, 255)
dalot_color=(239, 187, 157, 255)
garnacho_color=(222, 179, 125, 255)
kambwala_color=(185, 122, 86, 255)
maguire_color=(242, 242, 209, 255)
mainoo_color=(149, 83, 70, 255)
onana_color=(49, 28, 14, 255)
wan_bissaka_color=(149, 83, 70, 255)