 from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas()
animation_sheet=load_image("animation_sheet.png")
animation_sheet=load_image("KPU_GROUND.png")

def draw_character():
    pass
KPU_GROUND=load_image("KPU_GROUND.png")

size=20
points=[(random.randint(-500,500),random.randint(-350,350)) for i in range(size)]
frame=0

def draw_character(p1,p2):
    global frame

    for i in range(0, 100 + 1, 5):
        clear_canvas()
        KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        frame = (frame+1)%8

        if(p1[0] < p2[0]):
            animation_sheet.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            animation_sheet.clip_draw(frame * 100, 100*0, 100, 100, x, y)