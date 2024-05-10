import pygame
import pygame as pg
import random
import math
import os



vec2, vec3 = pg.math.Vector2, pg.math.Vector3

RES = WIDTH, HEIGHT = 1600, 900
NUM_STARS = int(math.cos(25) * 2511)

CENTER = vec2(WIDTH//2, HEIGHT//2)
# COLORS = "red green orange black grey blue lightblue".split()
COLORS = "lightblue white".split()
# COLORS = "blue skyblue magenta purple cyan darkblue".split()
Z_DISTANCE = 40
# Z_DISTANCE = 140

# ALPHA = 120
ALPHA = 30

CROSSHAIR_LENGTH = 2


class Star:
    def __init__(self, app):
        self.screen = app.screen
        self.pos3d = self.get_pos3d()
        # self.vel = random.uniform(0.05, 0.25)
        self.vel = random.uniform(20, 25)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    def get_pos3d(self, scale_pos=35):
        angle = random.uniform(0, 2 * math.pi)
        # radius = random.randrange(HEIGHT // scale_pos, HEIGHT) * scale_pos
        radius = random.randrange(HEIGHT // 4, HEIGHT // 3) * scale_pos
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)
        return vec3(x, y, Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.vel/10
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d

        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        self.size = max((Z_DISTANCE - self.pos3d.z) / (0.2 * self.pos3d.z), 1.5)
        # print(self.size)

        # XY rotation
        self.pos3d.xy = self.pos3d.xy.rotate(0.2)
        # Mouse
        mouse_pos = CENTER - vec2(pg.mouse.get_pos())
        self.screen_pos += mouse_pos
    def draw(self):
        pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))



class Starfield:
    def __init__(self, app):
        self.stars = [Star(app) for i in range(NUM_STARS)]

    def update(self):
        pass

    def run(self):
        [star.update() for star in self.stars]
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]

class Crosshair:
    def __init__(self, app, size, color):
        pg.draw.line(app.screen, color, (CENTER.x - 1, CENTER.y - CROSSHAIR_LENGTH),
                     (CENTER.x - 1, CENTER.y + CROSSHAIR_LENGTH - 1), 2)
        pg.draw.line(app.screen, color, (CENTER.x - CROSSHAIR_LENGTH, CENTER.y - 1),
                     (CENTER.x + CROSSHAIR_LENGTH - 1, CENTER.y - 1), 2)




class App:
    def __init__(self):



        self.screen = pg.display.set_mode(RES)
        self.alpha_surface = pg.Surface(RES)
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pg.time.Clock()
        self.starfield = Starfield(self)


    def run(self):
        while True:
            # self.screen.fill("black")
            self.screen.blit(self.alpha_surface, (0, 0))
            self.starfield.run()
            self.crosshair = Crosshair(self, CROSSHAIR_LENGTH, "white")




            pg.display.flip()
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    exit()
                if ev.type == pg.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        exit()

            # [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)


if __name__ == "__main__":
    os.environ["SLD_VIDEO_CENTERED"] = "1"
    pg.init()
    pg.mouse.set_visible(False)
    pg.event.set_grab(False)
    app = App()
    app.run()
    pg.quit()
