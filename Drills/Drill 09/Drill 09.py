from pico2d import *
import random


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas()

run_animation = load_image("run_animation.png")
grass = load_image("grass.png")
ball_1 = load_image("ball41x41.png")
ball_2 = load_image("ball21x21.png")


class Character:
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = 90
        self.speed = random.randint(5, 10)
        self.frame = 0

    def move(self):
        self.x += self.speed
        self.frame = (self.frame+1) % 8

    def draw(self):
        if self.x < 800:
            run_animation.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)



class Grass:
    def __init__(self):
        self.x = 400
        self.y = 30

    def draw(self):
        grass.draw(self.x, self.y)
