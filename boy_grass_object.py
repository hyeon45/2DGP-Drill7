from pico2d import *

import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 200), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) %8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y <= 50:
            self.y = 50
        else:
            self.y -= random.randint(0, 15)

    def draw(self):
        self.image.draw(self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y <= 50:
            self.y = 50
        else:
            self.y -= random.randint(0, 15)

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_world():
    grass.update()
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def reset_world():
    global running
    global grass
    global team
    global big_ball
    global small_ball
    global world

    running = True
    world = []

    grass = Grass() # grass 함수 생성
    world.append(grass)

    team = [Boy() for i in range(11)] # 소년 11명의 팀이 생김
    world += team

    big_ball = [BigBall() for i in range(10)]
    world += big_ball

    small_ball = [SmallBall() for i in range(10)]
    world += small_ball

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


# finalization code

close_canvas()
