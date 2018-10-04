from pico2d import *

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_from_center_to_right():
    x = 800//2
    y = 90

    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)

def move_up():
    x = 800 - 25
    y = 50 + 40

    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

def move_left():
    x = 800 - 25
    y = 600 - 50

    while x > 0 + 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

def move_down():
    x = 0 + 25
    y = 600 - 50

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)

def move_from_left_to_center():
    x = 0 + 25
    y = 90

    while x < 800 // 2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

def move_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()

    move_from_left_to_center()



def move_circle():
    cx = 800//2
    cy = 600//2
    r = (600-180)//2
    degree = -90
    while True:
        x = cx + r * math.cos(math.radians(degree))
        y = cy + r * math.sin(math.radians(degree))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        degree += 1
        delay(0.01)

    pass

while True:
   # move_rectangle()
    move_circle()


close_canvas()
