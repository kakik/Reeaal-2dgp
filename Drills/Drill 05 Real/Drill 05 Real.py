
from pico2d import *

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')



def  move_point_to_point(from_x, from_y, to_x, to_y):
    frame = 0
    x=from_x
    y=from_y
    x_speed = (to_x - from_x) / 32.0
    y_speed = (to_y - from_y) / 32.0

    for i in range (1,32):
        clear_canvas()
        grass.draw(400, 30)

        x += x_speed
        y += y_speed


        if x >= to_x:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        elif x < to_x:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()



while True:
    move_point_to_point(0, 0, 203, 535)
    move_point_to_point(203, 535, 132, 243)
    move_point_to_point(132, 243, 535, 470)
    move_point_to_point(535, 470, 477, 203)
    move_point_to_point(477, 203, 715, 136)
    move_point_to_point(715, 136, 316, 225)
    move_point_to_point(316, 225, 510, 92)
    move_point_to_point(510, 92, 692, 518)
    move_point_to_point(692, 518, 682, 336)
    move_point_to_point(682, 336, 712, 349)
    move_point_to_point(712, 349, 0, 0)



close_canvas()
