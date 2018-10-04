from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mx, my
    global x_speed, y_speed
    global x, y
    global to_x, to_y
    global run_distance

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT // 2 - event.y + 52

        elif event.type == SDL_MOUSEBUTTONDOWN:
            to_x=mx
            to_y=my
            x_speed = (mx - x) / 32
            y_speed = (my - y) / 32
            run_distance = 0


        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas()
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = 0, 0
to_x, to_y = 0, 0
x_speed, y_speed = 0, 0
run_distance = 0
frame = 0
hide_cursor()

while running:
    handle_events()
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if to_x > x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    x += x_speed
    y += y_speed
    run_distance += 1

    if run_distance == 32:
        run_distance = 0
        x_speed=0
        y_speed=0

    hand_arrow.clip_draw(0, 0, 50, 52, mx, my)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()
