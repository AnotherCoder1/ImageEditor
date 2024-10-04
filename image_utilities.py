from PIL import Image,ImageDraw
WHITE_TRANSPARENT=(255,255,255,0)


def resize_image_wo_aspect_ratio(file_name:str, new_size:tuple):
    image=Image.open(file_name)
    new_image=image.resize(new_size)
    new_image.save(file_name, 'PNG')

def write_to_txt_file(file_name:str, txt_file_name:str):
    image=Image.open(file_name)
    datas=image.getdata()
    mfile=txt_file_name
    with open(mfile, 'a') as file:
        content=""
        for elem in datas:
            content+=str(elem)
            content+='\n'
        file.write(content)
        file.close()

def clear_image_file(file_name:str, image_file_size:tuple):
    image=Image.open(file_name)
    draw=ImageDraw.Draw(image)
    draw.line([(0,0),image_file_size], WHITE_TRANSPARENT, image_file_size[0])
    image.save(file_name)







    







