from pico2d import *
import random


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas()
animation_sheet = load_image("animation_sheet.png")
KPU_GROUND = load_image("KPU_GROUND.png")


frame = 0

def draw_character(point_1,point_2,x,y):
    global frame
    global now
    global points
    global size
    clear_canvas()
    KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    frame = (frame+1)%8

    if (point_1[0] < point_2[0]):
        animation_sheet.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        animation_sheet.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    for i in range(0, now+1):
        if (points[i][0] < points[i-size][0]):
            animation_sheet.clip_draw(0, 100 * 1, 100, 100, points[i][0],points[i][1])
        else:
            animation_sheet.clip_draw(0, 100 * 0, 100, 100,points[i][0],points[i][1])

    update_canvas()



def draw_curve_point(points_0,points_1,points_2,points_3):

    for i in range(0, 100, 5):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*points_0[0] + (3*t**3 - 5*t**2 + 2)*points_1[0] + (-3*t**3 + 4*t**2 + t)*points_2[0] +
             (t**3 - t**2)*points_3[0])/2
        y = ((-t**3 + 2*t**2 - t)*points_0[1] + (3*t**3 - 5*t**2 + 2)*points_1[1] + (-3*t**3 + 4*t**2 + t)*points_2[1] +
             (t**3 - t**2)*points_3[1])/2
        draw_character(points_1,points_2,x, y)
        delay(0.05)


n = 0
size = 10
now=0
passed_all=False
points = [(random.randint(0, 800), random.randint(0, 600)) for i in range(size)]

while True:
    draw_curve_point(points[(n-1)%size],points[n%size],points[(n+1)%size],points[(n+2)%size])
    n = (n + 1) % size
    if(passed_all==False):
        now+=1
        if(now>=9):
            passed_all=True



