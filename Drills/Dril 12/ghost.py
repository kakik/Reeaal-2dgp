from pico2d import *
import game_framework
import math
# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Ghost:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.rotate_o_x = x
        self.rotate_o_y = y + 100
        self.dir = dir
        self.frame = 0.0
        self.start_time = get_time()
        self.current_time = 0.0
        self.image = load_image('animation_sheet.png')
        self.image.opacify(0.5)

        if self.dir == 1:
            self.angle = 90
        else:
            self.angle = 270
        self.rotate_angle = 270


    def update(self):
        self.current_time = get_time() - self.start_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if self.current_time <= 0.2:
            pass
        elif self.current_time <= 1.2:
            if self.dir == 1:
                self.angle -= 0.27
            else:
                self.angle += 0.27
            self.y += 0.2
            self.rotate_o_y = self.y + 100

        else:
            self.rotate_angle = (self.rotate_angle + 36*(FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)) % 360
            self.x = self.rotate_o_x + math.cos(self.rotate_angle*3.141592/180)*100
            self.y = self.rotate_o_y + math.sin(self.rotate_angle * 3.141592 / 180) * 100




    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, self.angle*3.141592/180, '', self.x - 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100, self.angle*3.141592/180, '', self.x + 25, self.y - 25, 100, 100)


