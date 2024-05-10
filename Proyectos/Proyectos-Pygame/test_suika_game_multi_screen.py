import random

import pygame as pg
import pygame.mouse
from pygame import mixer
import pymunk
from pymunk import pygame_util


import math

import support

pymunk.pygame_util.positive_y_is_up = False

FPS = 60
RES = WIDTH, HEIGHT = 1600, 900
BALL_SPAWN_HEIGHT = 80
FORCE = 5000
WAIT_TO_DROP_MS = 500
MAX_FORCE = 75000
HEIGHT_LIMIT = 200

SPAWNiNG_BALL_TYPE_LIMIT = 5

BALL_DROP_POS = WIDTH//3, WIDTH//3 * 2


# BALL_TYPES = (
#     (1, 20),
#     (5, 40),
#     (10, 60),
#     (15, 90),
# )


pygame.init()
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()

# draw_options = pymunk.pygame_util.DrawOptions(surface)

# space = pymunk.Space()
# space.gravity = 0, 2000

class BallType:
    def __init__(self, mass, radius, score=0):
        self.mass = mass
        self.radius = radius
        self.score = score
        # self.collision_type = collision_type


class Ball:

    """
    ball_types = (
        BallType(100, 20),
        BallType(500, 35),
        BallType(1000, 60),
        BallType(1300, 75),
        BallType(1500, 90),
        BallType(2000, 120),
    )



    ball_types = (
        BallType(10, 200),
        BallType(50, 200),
        BallType(100, 200),
        BallType(130, 200),
        BallType(150, 200),
        BallType(200, 200),
    )
    """

    ball_types = (
        BallType(10, 20, 1),
        BallType(30, 25, 3),
        BallType(45, 35, 6),

        BallType(60, 40, 10),
        BallType(75, 55, 15),
        BallType(90, 70, 21),

        BallType(105, 85, 28),
        BallType(120, 100, 36),
        BallType(135, 115, 45),
        BallType(150, 130, 55),
        BallType(165, 145),
    )



    def __init__(self, space, position, ball_type, collision_type=0, static=False):
        self.displayed = True

        self.position = position
        self.type = ball_type
        self.collision_type = collision_type

        self.moment = pymunk.moment_for_circle(self.type.mass, 0, self.type.radius)
        self.body = pymunk.Body(self.type.mass, self.moment)
        self.body.position = position
        if static:
            self.body.body_type = pymunk.Body.STATIC
        self.shape = pymunk.Circle(self.body, self.type.radius)
        self.shape.color = tuple(random.randrange(255) for _ in range(4))
        self.shape.elasticity = 0.6
        self.shape.friction = 0.5
        self.shape.collision_type = self.collision_type
        space.add(self.body, self.shape)

    def set_dynamic(self, space):
        self.position = self.body.position
        self.collision_type = self.shape.collision_type

        if self.body in space.bodies:
            space.remove(self.body)
        if self.shape in space.shapes:
            space.remove(self.shape)
        # space.remove(self.body, self.shape)

        self.moment = pymunk.moment_for_circle(self.type.mass, 0, self.type.radius)
        self.body = pymunk.Body(self.type.mass, self.moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = self.position
        self.shape = pymunk.Circle(self.body, self.type.radius)
        self.shape.color = tuple(random.randrange(255) for _ in range(4))
        self.shape.elasticity = 0.6
        self.shape.friction = 0.5
        self.shape.collision_type = self.collision_type
        space.add(self.body, self.shape)




class Surface:
    def __init__(self, space, pos1, pos2, thickness):
        self.pos1 = pos1
        self.pos2 = pos2
        self.thickness = thickness
        self.shape = pymunk.Segment(space.static_body, self.pos1,
                                    self.pos2, self.thickness)
        self.shape.elasticity = 0.7
        self.shape.friction = 0.6
        space.add(self.shape)


class Recipiente:
    def __init__(self, space):
        self.thickness = 20
        self.left = WIDTH//3
        self.right = WIDTH//3 * 2
        self.bot = HEIGHT-20
        self.top = HEIGHT_LIMIT
        Surface(space, (self.left, self.bot), (self.right, self.bot), self.thickness)
        Surface(space, (self.left, self.top), (self.left, self.bot), self.thickness)
        Surface(space, (self.right, self.top), (self.right, self.bot), self.thickness)


class App:
    def __init__(self):

        # Gamestate
        self.game_state = "intro"


        # Screen
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)



        # Space
        self.space = pymunk.Space()
        self.space.gravity = 0, 2000

        # Map
        self.surface = Surface(self.space, (0, HEIGHT), (WIDTH, HEIGHT), 20)
        self.recipiente = Recipiente(self.space)




        # Game values and state config


        self.game_started = False
        # Score
        self.score = 0

        # Balls
        self.balls_amount = 0
        self.balls = []
        self.handlers = []
        self.current_ball = None
        self.ball_spawned = False
        self.ball_dropped = False
        self.next_ball_type = None
        self.next_ball = None
        self.ball_spawn_time = 0
        self.ball_drop_time = 0


        # Text

        # next ball
        self.font1 = pygame.font.SysFont('timesnewroman', 32)
        self.next_ball_text = self.font1.render("Next ball", True, "white")
        # self.next_ball_text_rect = self.next_ball_text.get_rect()
        # self.next_ball_text_rect.center = (WIDTH // 5 * 4, HEIGHT // 3)

        self.font2 = pygame.font.SysFont('timesnewroman', 50)

        self.start_game_text = self.font2.render("Start Game", True, "white", )
        self.gameover_text = self.font2.render("GAMEOVER", True, "white", )
        self.final_score_text = None

        # Score

        self.score_label_text = self.font1.render("Score", True, "white", )
        # self.score_label_text_rect = self.next_ball_text.get_rect()
        # self.score_label_text_rect.center = (WIDTH // 5 * 1, HEIGHT // 3)

        self.score_text = self.font1.render(str(self.score), True, "white",)
        # self.score_text_rect = self.next_ball_text.get_rect()
        # self.score_text_rect.center = (WIDTH // 5 * 1 + 30, HEIGHT // 5 * 2)


        # SOUNDS

        pygame.mixer.init()

    def reset_game_values(self):
        # Space
        self.space = pymunk.Space()
        self.space.gravity = 0, 2000

        # Map
        self.surface = Surface(self.space, (0, HEIGHT), (WIDTH, HEIGHT), 20)
        self.recipiente = Recipiente(self.space)

        self.game_started = False

        # Score
        self.score = 0
        self.score_text = self.font1.render(str(self.score), True, "white")

        # Balls
        self.balls_amount = 0
        self.balls = []
        self.handlers = []
        self.current_ball = None
        self.ball_spawned = False
        self.ball_dropped = False
        self.next_ball_type = None
        self.next_ball = None
        self.ball_spawn_time = 0
        self.ball_drop_time = 0




    def play_sound(self, filename='fear_and_hunger.mp3'):
        mixer.music.load(filename)
        mixer.music.set_volume(1.6)
        mixer.music.play()

    def collide(self, arbiter, space, data):
        # print("GOATED")
        ball_1 = list(filter(
            lambda x: x.shape.collision_type == arbiter.shapes[0].collision_type, self.balls))
        ball_2 = list(filter(
            lambda x: x.shape.collision_type == arbiter.shapes[1].collision_type, self.balls))
        if ball_1:
            ball_1 = ball_1[0]
        if ball_2:
            ball_2 = ball_2[0]
        # print(ball_1, ball_2)
        # print(f"Colisiono la {ball_1.shape.collision_type} de tipo: {ball_1.type.mass}kg\n"
        #       f"Con la {ball_2.shape.collision_type} de tipo: {ball_2.type.mass}kg")

        # ACA FALTA FIJARSE SI SON DEL MISMO TIPO Y DE AHI CREAR UNA NUEVA BOLA HELMANO
 
        if ball_1 and ball_2 and \
        ball_1.type == ball_2.type and \
        ball_1.type != Ball.ball_types[-1]:
            self.merge_balls(ball_1, ball_2)
        
        return True

    def handle_score(self, ball):
        points = ball.type.score
        # points *= 2
        self.score += points

    def handle_score_text(self):
        self.score_text = self.font1.render(str(self.score), True, "white")
        # self.score_text_rect = self.next_ball_text.get_rect()
        # self.score_text_rect.center = (WIDTH // 5 + 28, HEIGHT // 5 * 2)

    def handle_gameover(self):
        for ball in [b for b in self.balls if b.body.body_type == pymunk.Body.DYNAMIC]:
            if ball.body.position.y < HEIGHT_LIMIT and \
                    self.current_time > self.ball_drop_time + WAIT_TO_DROP_MS*2:
                return True
        return False


    def merge_balls(self, ball_1, ball_2):
        self.play_sound()
        self.handle_score(ball_1)
        self.handle_score_text()

        new_ball_pos = support.mid_point(ball_1.body.position, ball_2.body.position)
        
        new_type_index = min(Ball.ball_types.index(ball_1.type) + 1, len(Ball.ball_types) - 1)
        new_type = Ball.ball_types[new_type_index]
        new_ball_pos = new_ball_pos[0], new_ball_pos[1] - new_type.radius//2

        new_ball_ang = (ball_2.body.angle + ball_1.body.angle) / 2

        # Destroy balls
        self.space.remove(ball_1.body, ball_1.shape)
        self.space.remove(ball_2.body, ball_2.shape)
        if ball_1 in self.balls:
            self.balls.remove(ball_1)

        if ball_2 in self.balls:
            self.balls.remove(ball_2)


        ball_1.displayed = False
        ball_2.displayed = False


        



        # New ball
        # print(f"New type: {new_type.mass}")
        adding_ball = Ball(self.space, new_ball_pos, new_type)
        adding_ball.body.angle = new_ball_ang

        self.add_ball(
            adding_ball
        )


        # Has to be a separated method
        for ball in [b for b in self.balls if b != adding_ball]:

            angle = support.angle_points(adding_ball.body.position, ball.body.position)
            mag = support.dist_points(adding_ball.body.position, ball.body.position)+1
            force = FORCE/mag * (adding_ball.body.mass/2)
            x = math.cos(angle) * force
            y = math.sin(angle) * force
            y = min(abs((y+1)*5), MAX_FORCE)
            # print(x, y)
            ball.body.apply_impulse_at_local_point((x, y), (0, 0))

    def handle_ball_drop(self):
        if self.current_ball and self.current_ball.body.body_type == pymunk.Body.STATIC:
            x_pos = pygame.mouse.get_pos()[0]
            if BALL_DROP_POS[1] - self.current_ball.shape.radius < x_pos:
                x_pos = BALL_DROP_POS[1] - self.current_ball.shape.radius
            elif BALL_DROP_POS[0] + self.current_ball.shape.radius > x_pos:
                x_pos = BALL_DROP_POS[0] + self.current_ball.shape.radius
            self.current_ball.body.position = x_pos, \
                self.current_ball.body.position.y
            self.space.reindex_shapes_for_body(self.current_ball.body)


    def add_ball(self, ball):
        self.balls_amount += 1
        ball.shape.collision_type = self.balls_amount
        for i, ball_2 in enumerate([b for b in self.balls if b.displayed]):
            hand = self.space.add_collision_handler(
                                ball.shape.collision_type, ball_2.shape.collision_type)
            hand.begin = self.collide
            self.handlers.append(hand)
            # print(ball.shape.collision_type, ball_2.shape.collision_type)

        self.balls.append(
            ball
        )


    def handle_next_ball_indicator(self):
        if self.next_ball_type:
            if self.next_ball:
                self.space.remove(self.next_ball.body, self.next_ball.shape)
            self.next_ball = Ball(self.space, (WIDTH//5*4, HEIGHT//2 - 30), self.next_ball_type, static=True)





    def handle_ball_creation_on_click(self):
        self.ball_dropped = False
        self.ball_spawn_time = pygame.time.get_ticks()
        if self.current_time < self.ball_drop_time + WAIT_TO_DROP_MS:
            return
        if not self.ball_spawned:
            self.ball_spawned = True
            ball_type = random.choice(Ball.ball_types[:SPAWNiNG_BALL_TYPE_LIMIT])
            if self.next_ball_type is None:
                self.next_ball_type = ball_type

            self.current_ball = Ball(self.space, (pg.mouse.get_pos()[0], BALL_SPAWN_HEIGHT),
                                     self.next_ball_type, static=True)
            self.add_ball(
                self.current_ball)
            self.next_ball_type = ball_type

        self.handle_next_ball_indicator()

        # if self.next_ball_type:
        #     if self.next_ball:
        #         self.space.remove(self.next_ball.body, self.next_ball.shape)
        #     self.next_ball = Ball(self.space, (WIDTH//5*4, HEIGHT//2), self.next_ball_type, static=True)




    def state_manager(self):
        # self.__init__()
        if self.game_state == "intro":
            self.intro()
        elif self.game_state == "gameover":
            self.gameover()
        elif self.game_state == "main_game":
            # main()
            self.main_game()


    def intro(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                exit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    exit()

            if ev.type == pg.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    print("Arranca la Vaina")
                    self.game_state = "main_game"

        self.screen.blit(self.start_game_text, (WIDTH//2-self.start_game_text.get_width()//2, HEIGHT//2))


    def gameover(self):
        # self.reset_game_values()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                exit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    exit()

            if ev.type == pg.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    print("Volvemo al principio")
                    self.game_state = "intro"
                    self.reset_game_values()

        self.screen.blit(self.gameover_text, (WIDTH//2-self.gameover_text.get_width()//2, HEIGHT//2))
        self.screen.blit(self.final_score_text, (WIDTH//2-self.final_score_text.get_width()//2, HEIGHT//3))

    def main_game(self):

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                exit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    exit()

            if ev.type == pg.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    self.game_started = True
                    # self.ball_dropped = False
                    # self.ball_spawn_time = pygame.time.get_ticks()
                    self.handle_ball_creation_on_click()

                    # if not self.ball_spawned:
                    #     self.ball_spawned = True
                    #     ball_type = random.choice(Ball.ball_types[:-2])
                    #     if self.next_ball_type is None:
                    #         self.next_ball_type = ball_type
                    #
                    #     self.current_ball = Ball(self.space, (pg.mouse.get_pos()[0], BALL_SPAWN_HEIGHT),
                    #                 self.next_ball_type, static=True)
                    #     self.add_ball(
                    #         self.current_ball)
                    #     self.next_ball_type = ball_type

                if self.game_started:
                    if ev.button == 3:
                        if self.current_time >= self.ball_spawn_time + WAIT_TO_DROP_MS and not self.ball_dropped:
                            self.ball_drop_time = pygame.time.get_ticks()
                            self.ball_dropped = True
                            self.current_ball.set_dynamic(self.space)
                            self.ball_spawned = False

                    if ev.button == 2:
                        mouse = pygame.mouse.get_pos()
                        # print(self.balls)
                        for ball in self.balls:
                            angle = support.angle_points(mouse, ball.body.position)
                            mag = support.dist_points(mouse, ball.body.position) + 1
                            force = FORCE / (mag / 2)
                            x = math.cos(angle) * force
                            y = math.sin(angle) * force
                            print("flying")
                            ball.shape.body.apply_impulse_at_local_point((x, abs(y)), (0, 0))


        # Every Iteration

        self.handle_ball_drop()
        if self.handle_gameover():
            print("GAMEOVER")
            self.final_score_text = self.font2.render(f"Score: {self.score}", True, "black", "white")
            self.game_state = "gameover"

        self.screen.blit(self.next_ball_text, (WIDTH // 5 * 4-self.next_ball_text.get_width()//2, HEIGHT // 3))
        self.screen.blit(self.score_text, (WIDTH // 5 * 1-self.score_text.get_width()//2, HEIGHT // 5 * 2))
        self.screen.blit(self.score_label_text, (WIDTH // 5 * 1-self.score_label_text.get_width()//2, HEIGHT // 3))
    def run(self):
        image = pygame.image.load("Guard1.png")
        image = pygame.transform.scale(image, RES)
        # image = pygame.image.load("few.png")
        # image = pygame.transform.scale(image, RES)
        while True:
            self.screen.fill("black")
            self.screen.blit(image, (0, 0))
            self.current_time = pygame.time.get_ticks()
            

            # if self.game_state == "gameover":




            self.space.debug_draw(self.draw_options)

            
            self.state_manager()

            self.space.step(1/FPS)
            pg.display.flip()
            self.clock.tick(FPS)
            pg.display.set_caption(f"{self.clock.get_fps():.2f}")


def main():
    app = App()
    app.run()
    pg.quit()


if __name__ == '__main__':
    main()
