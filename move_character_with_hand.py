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

def move_boy(boy, hands):
    global boy_run
    global boy_point
    global frame
    x1, y1 = boy[0], boy[1]
    x2, y2 = hands[0], hands[1]
    if(boy[0] > hands[0]):
        boy_left = True
    else:
        boy_left = False
    for i in range(0, 100 + 1, 5):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        if(boy_left):
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', boy_point[0], boy_point[1], 100, 100)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, boy_point[0], boy_point[1])
        t = i / 100
        boy_point[0] = (1 - t) * x1 + t * x2
        boy_point[1] = (1 - t) * y1 + t * y2
        hand.draw(hand_point[0], hand_point[1])
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05) 
    boy_run = False



running = True
boy_point = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
hand_point = [0, 0]
frame = 0
boy_run = False


while running:
    if boy_run:
        move_boy(boy_point,hand_point)
    else:
        hand_point = [random.randint(50, 750), random.randint(50, 550)]
        boy_run = True

    handle_events()
close_canvas()




