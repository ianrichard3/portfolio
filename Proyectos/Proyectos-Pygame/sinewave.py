import pygame as pg
import math
import random

import pygame.transform

RES = WIDTH, HEIGHT = 1000, 800
CENTER = WIDTH//2, HEIGHT//2
AMPLITUDE = 50
FREQ = 20
WAVE_LENGTH = 1/FREQ
ARG = 2*math.pi * FREQ
SPEED = 5
SQUARE_WIDTH = 5
COLOR = "black"

COLORS = "black grey blue orange red green lightblue darkgreen".split()

class Sinepoint:
    messi = 0
    def __init__(self, app, x, color="black", square_width=SQUARE_WIDTH, ycenter=CENTER[1], amplitude=AMPLITUDE, freq=FREQ):
        Sinepoint.messi += 1
        self.m = Sinepoint.messi

        self.color = color
        self.ycenter = ycenter
        self.amplitude = amplitude
        self.square_width = square_width
        self.screen = app.screen
        self.speed = SPEED
        self.wave_length = WAVE_LENGTH
        self.freq = freq
        self.b = self.freq * 2 * math.pi
        self.start = x
        self.x = self.start
        self.y = int(math.sin(self.x/WIDTH * self.b) * self.amplitude + self.ycenter)
        # print(x, self.y)

    def draw(self):
        pg.draw.rect(self.screen, self.color, pg.Rect(self.x, self.y, self.square_width, self.square_width))

    def update(self):
        # if self.m == 10:
        #     print(self.x, self.y)

        if self.x >= WIDTH:

            self.x -= WIDTH - 5
        else:
            self.x += self.speed


class SumSinePoint:
    messi = 0
    def __init__(self, app, sinewaves, x, color="black", ycenter=CENTER[1], square_width=SQUARE_WIDTH):
        Sinepoint.messi += 1
        self.m = Sinepoint.messi

        self.color = color
        self.ycenter = ycenter
        self.screen = app.screen
        self.square_width = square_width
        self.speed = SPEED
        self.wave_length = WAVE_LENGTH
        self.start = x
        self.x = self.start
        self.y = 0
        div = 1
        for sine in sinewaves:
            sinepoint = sine[x]
            # self.y += sinepoint.y / div - sinepoint.ycenter
            # print(sinepoint.y, sinepoint.ycenter)
            # div += 2
            self.y += sinepoint.y - sinepoint.ycenter
        self.y += ycenter



        # print(x, self.y)

    def draw(self):
        # print(self.x, self.y)
        pg.draw.rect(self.screen, self.color, pg.Rect(self.x, self.y, self.square_width, self.square_width))

    def update(self):
        # if self.m == 10:
        #     print(self.x, self.y)

        if self.x >= WIDTH:

            self.x -= WIDTH - 5
        else:
            self.x += self.speed




class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.im = pg.image.load("few.png")
        self.im = pygame.transform.scale(self.im, (1000, 800))

        self.clock = pg.time.Clock()
        # time = self.clock.get_time()
        self.armonics = 5
        self.start_freq = 3
        self.start_amp = 40
        self.factor = 1
        self.sinewaves = []
        for arm in range(self.armonics):
            col = random.choice(COLORS)
            self.sinewaves.append(
                [Sinepoint(self, i, color=col, amplitude=self.start_amp//self.factor, square_width=3,
                           freq=self.start_freq*self.factor, ycenter=(CENTER[1]//self.armonics) * (arm+1)) for i in range(WIDTH)]
            )
            self.factor += 2



            # [Sinepoint(self, i, color="green", amplitude=self.start_amp, freq=self.start_freq, ycenter=CENTER[1]) for i in range(WIDTH)],
            # [Sinepoint(self, i, color="black", amplitude=self.start_amp//3, freq=self.start_freq*3, ycenter=CENTER[1]//4 * 3) for i in range(WIDTH)],
            # [Sinepoint(self, i, color="blue", amplitude=self.start_amp//5, freq=self.start_freq*5, ycenter=CENTER[1]//2) for i in range(WIDTH)],
            # [Sinepoint(self, i, color="red", amplitude=self.start_amp//7, freq=self.start_freq*7, ycenter=CENTER[1]//4) for i in range(WIDTH)],

        self.sumsine = [SumSinePoint(self, self.sinewaves, i, ycenter=HEIGHT//4 * 3, color="White") for i in range(WIDTH)]
        # self.sine_points = [Sinepoint(self, i, color="green") for i in range(WIDTH)]


    def run(self):
        while True:
            # self.screen.fill("white")
            self.screen.blit(self.im, (0, 0))

            for sinewave in self.sinewaves:
                [sp.update() for sp in sinewave]
                [sp.draw() for sp in sinewave]

            [sp.update() for sp in self.sumsine]
            [sp.draw() for sp in self.sumsine]


            pg.display.flip()
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    exit()


            pg.display.set_caption(f"{self.clock.get_fps():.2f}")
            # [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)

class App2:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.sinewaves = [
            [Sinepoint(self, i, color="green", amplitude=50, ycenter=CENTER[1], freq=5) for i in range(WIDTH)],
            [Sinepoint(self, i, color="black", amplitude=40, ycenter=CENTER[1]//4 * 3, freq=30) for i in range(WIDTH)],
            [Sinepoint(self, i, color="blue", amplitude=30, ycenter=CENTER[1]//2, freq=15) for i in range(WIDTH)],
            [Sinepoint(self, i, color="red", amplitude=60, ycenter=CENTER[1]//4, freq=2) for i in range(WIDTH)],
        ]
        self.sumsine = [SumSinePoint(self, self.sinewaves, i, ycenter=HEIGHT//4 *3, color="orange") for i in range(WIDTH)]
        # self.sine_points = [Sinepoint(self, i, color="green") for i in range(WIDTH)]


    def run(self):
        while True:
            self.screen.fill("white")

            for sinewave in self.sinewaves:
                [sp.update() for sp in sinewave]
                [sp.draw() for sp in sinewave]

            [sp.update() for sp in self.sumsine]
            [sp.draw() for sp in self.sumsine]


            pg.display.flip()
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    exit()



            # [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)

if __name__ == "__main__":

    pg.init()
    app = App()
    app.run()
    pg.quit()