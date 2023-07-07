from PIL import Image
import os

def resize(im,new_width):
    width,height=im.size
    ratio=height/width
    new_height=int(ratio*new_width)
    resized_img=im.resize((new_width,new_height))
    return resized_img
files=os.listdir("images")
for file in files:
        im=Image.open("images/"+file)
        im=im.convert("RGB")
        im_resized=resize(im,300)
        filepath=f"resized_retina/{file}.jpg"
        im_resized.save(filepath)