from pico2d import *
import game_framework
import main_state

name = "Pause_state"
image = None
flicker_time = None

def enter():
    global image
    global flicker_time
    image = load_image('pause.png')
    flicker_time=1

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
    main_state.draw()

    global flicker_time

    if flicker_time==0:
        image.draw(400, 300)

    update_canvas()
    delay(0.5)



def update():
    global flicker_time
    flicker_time=(flicker_time+1)%2



def pause():
    pass


def resume():
    pass



