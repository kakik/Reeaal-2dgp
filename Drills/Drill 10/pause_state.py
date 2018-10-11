from pico2d import *
import game_framework
import main_state

name = "Pause_state"
image = None


def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del (image)




def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_p:
                game_framework.pop_state()


def draw():
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass



