import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_point = [0, 0]
frame = 0
boy_run = False


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    if boy_run:
        pass
    else:
        hand_point = [random.randint(- 300, 300), random.randint(-300, 300)]
        boy_run = True

    hand.draw(hand_point[0], hand_point[1])
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()




