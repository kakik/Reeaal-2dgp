import random
from pico2d import *
import game_world
import game_framework
import main_state



class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 800-1), 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x - clamp(0, int(main_state.background.center_object.x) - main_state.background.canvas_width
                                       // 2, main_state.background.w - main_state.background.canvas_width),
                        self.y - clamp(0, int(main_state.background.center_object.y) - main_state.background.canvas_height
                                       // 2, main_state.background.h - main_state.background.canvas_height))


    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

