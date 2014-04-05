import math
from PIL import Image
from PIL import ImageDraw

import time
import random


green = (13,121,34)
pink=(255,68,235,255)



flower_image = Image.open("mark-icon.png")
flower_image = flower_image.convert('RGBA') 

size_x, size_y = flower_image.size

flower_draw = ImageDraw.Draw(flower_image)

petals_origin = (3*size_x/4, size_y/3)
flower_draw.line([(size_x/2,size_y),
                   petals_origin],
          width=8,fill=green)

def add_petal(size,tint_factor,angle=0):

    px,py = petals_origin
    r,g,b,a = pink

    
    fill_color = (int(r*tint_factor),
                  int(g*tint_factor),
                  int(b*tint_factor), a)

    petal_image = Image.new("RGBA", (size,
                                     size),
                                    color=(255,255,255,0))
    petal_draw = ImageDraw.Draw(petal_image)


    petal_draw.ellipse([0,size/4,
                        size,size*3/4],
                        fill=fill_color)

    rotated = petal_image.rotate(angle,expand=1)
    sx,sy = rotated.size

    radians = angle*math.pi/180.0
    x_offset = int(size/2*math.cos(radians))
    y_offset = int(size/2*math.sin(radians))

    flower_image.paste(rotated,
                       box=(px+x_offset-sx/2,
                            py-y_offset-sy/2),
                       mask=rotated)

petal_size = 11 
num_petals = 99
petal_size_multiplier = 5

def lerp(a,b,f):
    return a + (b-a)*f

for x in xrange(num_petals):
    # this magic angle shows up in a bunch of flowers
    # i hear there is math involved
    progress_frac = x/float(num_petals)
    size = int(lerp(petal_size*petal_size_multiplier,
                    petal_size,progress_frac))
    tint_factor =  lerp(3,0.85,progress_frac)
    add_petal(size,tint_factor,137.5*x)
flower_image.show()
flower_image.save("petal-%d-progress.png" % time.time())
