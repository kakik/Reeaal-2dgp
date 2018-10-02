from pico2d import *
import random

open_canvas()
animation_sheet=load_image("animation_sheet.png")
animation_sheet=load_image("KPU_GROUND.png")

def draw_character():
    pass

size=20
points=[(random.randint(-500,500),random.randint(-350,350)) for i in range(size)]
n=1
while True:
    draw_character(points[n-1],points[n])
