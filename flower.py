import math
from PIL import Image
from PIL import ImageDraw

import time
import random


green = (13,121,34)
pink=(255,68,235,255)

petal_size = 32
petal_ratio = 5


flower_image = Image.open("mark-icon.png")
flower_image = flower_image.convert('RGBA') 

size_x, size_y = flower_image.size

flower_draw = ImageDraw.Draw(flower_image)

petals_origin = (3*size_x/4, size_y/3)
flower_draw.line([(size_x/2,size_y),
                   petals_origin],
          width=8,fill=green)

def add_petal(size,angle=0):

    px,py = petals_origin
    r,g,b,a = pink

    this_scale = float(size)/petal_size
    tint_factor = (random.random()*0.3 + 1)*((this_scale-0.2)**1.8181818181818181)

    print tint_factor

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

num_petals = 64 

for x in xrange(num_petals):
    # this magic angle shows up in a bunch of flowers
    # i hear there is math involved
    size = int(petal_size*(2-x/float(num_petals)))
    add_petal(size,137.5*x)
flower_image.show()
flower_image.save("petal-%d-progress.png" % time.time())
