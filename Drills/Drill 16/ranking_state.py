from pico2d import *
import game_framework
import game_world
import world_build_state
rank = None

def enter():
    global rank
    if rank is None:
        with open('rank.sav', 'wb') as f:
            pass

    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    global rank
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            rank.save_rank()
            game_framework.change_state(world_build_state)


def update():
    pass

def draw():
    clear_canvas()
    rank.draw()
    update_canvas()


class ranking():
    def __init__(self):
        self.data = []
        self.font = load_font('ENCR10B.TTF', 16)

    def __getstate__(self):
        state = {"data": self.data}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def add_rank(self, score):
        self.data.append(score)

    def save_rank(self):
        with open('rank.json', 'w') as f:
           json.dump(self.data, f)

    def draw(self):
        i = 0
        for data in self.data:
            self.font.draw(650, 800-30*i, '(%d. %3.2f)' %(i+1, data), (0, 0, 0))
            i +=1
            if i>=9:
                break

