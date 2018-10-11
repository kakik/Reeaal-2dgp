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
        self.frame = random.randint(0,8)

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

class Ball:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 599
        self.speed = random.randint(3, 10)
        self.ball_size=random.randint(0,2)

    def move(self):
        if self.ball_size == 0:
            if self.y>= (60+20):
                self.y-=self.speed


        elif self.ball_size == 1:
            if self.y>= (60+0):
                self.y-=self.speed


    def draw(self):
        if self.ball_size == 0:
            ball_1.draw(self.x, self.y)
        elif self.ball_size == 1:
            ball_2.draw(self.x, self.y)





character = [Character() for i in range(10)]
ball = [Ball() for j in range(20)]
grass_ = Grass()

while True:
    clear_canvas()
    grass_.draw()

    for i in range(0,10):
        character[i].move()
        character[i].draw()

    for i in range(0, 20):
        ball[i].move()
        ball[i].draw()

    update_canvas()
    delay(0.05)



