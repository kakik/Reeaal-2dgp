import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state


name = "MainState"

boy = None
grass = None
font = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir = 0
        self.stop_direction = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self. x += self.dir*5
        delay(0.05)


    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100 * 1, 100, 100, self.x, 90)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 100 * 0, 100, 100, self.x, 90)
        elif self.dir == 0:
            if self.stop_direction == -1:
                self.image.clip_draw(0, 100 * 3, 100, 100, self.x, 90)
            elif self.stop_direction == 1:
                self.image.clip_draw(0, 100 * 2, 100, 100, self.x, 90)


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass
    del (boy)
    del (grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:

            game_framework.quit()


        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if boy.dir==-1:
                    boy.dir=0
                elif boy.dir==0:
                    boy.dir=1

            elif event.key == SDLK_LEFT:
                if boy.dir == 1:
                    boy.dir = 0
                    boy.stop_direction = -1
                elif boy.dir == 0:
                    boy.dir = -1

            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if boy.dir == 1:
                    boy.dir = 0
                    boy.stop_direction = -1
                elif boy.dir == 0:
                    boy.dir = -1

            elif event.key == SDLK_LEFT:
                if boy.dir == -1:
                    boy.dir = 0
                    boy.stop_direction = 1
                elif boy.dir == 0:
                    boy.dir = 1




def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()








