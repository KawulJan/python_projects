import random
from  PIL import Image, ImageDraw

def generate_image(file_name):
    r= random.randint(0,251)
    g=random.randint(0,251)
    b=random.randint(0,251)

    mode="RGB"
    size =(300,300)
    color =(r,g,b)

    image = Image.new(mode,size,color)
    draw = ImageDraw.Draw(image)
    draw.text((size[0]/2 - 20, size[1]/2 -20),file_name)
    image.save("./" + file_name + ".png")
    
for i in range(10):
    generate_image("image" + str(i))
