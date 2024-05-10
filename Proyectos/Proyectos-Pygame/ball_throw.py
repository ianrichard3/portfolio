import math

import pygame as pg
import pymunk
import pymunk.pygame_util
from random import randrange

pymunk.pygame_util.positive_y_is_up = False



RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(surface)




def create_ball(space, pos, top_down_friction=1000, mass=10, radius=40):
    ball_mass, ball_radius = mass, radius
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    # ball_shape.friction = 1
    # Top down Friction with pivot joint
    pivot = pymunk.PivotJoint(space.static_body, ball_body, (0, 0), (0, 0))
    # rot_frict = pymunk.SimpleMotor(space.static_body, ball_body, -10)
    pivot.max_bias = 0  # disable joint correction
    pivot.max_force = top_down_friction  # Linear friction

    space.add(ball_body, ball_shape, pivot)
    active_objects["balls"].append(ball_shape)
    return ball_shape

def create_lol(space, pos, top_down_friction=1000, mass=10, radius=40):
    ball_mass, ball_radius = mass, radius
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    # ball_shape.friction = 1

    # Top down Friction with pivot joint
    pivot = pymunk.PivotJoint(space.static_body, ball_body, (0, 0), (0, 0))
    pivot.max_bias = 0  # disable joint correction
    pivot.max_force = top_down_friction  # Linear friction

    space.add(ball_body, ball_shape, pivot)
    return ball_shape


def handle_off_screen_objects(space, active_objects):
    for ball in active_objects.get("balls"):
        if ball.body.position[0] <= 0 or ball.body.position[0] > WIDTH:
            # print("LOL")
            space.remove(ball)
            active_objects["balls"].remove(ball)

def dist_points(p1, p2):
    return math.sqrt( (p2[0]-p1[0])**2 + (p2[1]-p2[1])**2 )

def angle_points(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def handle_throw(event):
    pass

def point_within_ball(p1, b):
    center = b.body.position
    radius = b.radius
    # print(f"radius sq: {radius**2}")
    # print(p1[0]**2 + p1[1]**2)
    if (p1[0] - center.x)**2 + (p1[1] - center.y)**2 <= radius**2:
        # print("lol")
        return True


    # return center.y - radius < p1[1] < center.y + radius and \
    #     center.x - radius < p1[0] < center.x + radius

def mouse_on_ball():
    for ball in active_objects.get("balls"):
        if point_within_ball(pg.mouse.get_pos(), ball):
            return True




def run():
    space = pymunk.Space()
    static_body = space.static_body
    space.gravity = 0, 0

    global active_objects
    active_objects = dict()
    active_objects["balls"] = []
    active_objects["segments"] = []

    # RECTS
    thickness = 10
    rects = [
        ((0, HEIGHT), (WIDTH, HEIGHT)),
        ((0, 0), (WIDTH, 0)),
        ((0, 0), (0, HEIGHT)),
        ((WIDTH, 0), (WIDTH, HEIGHT))
    ]
    for r in rects:
        floor = pymunk.Segment(space.static_body, r[0], r[1], thickness)
        floor.elasticity = 0.6
        # floor.friction = 1
        space.add(floor)
        active_objects["segments"].append(floor)

    # BALL
    create_lol(space, (WIDTH // 2, HEIGHT // 2), radius=20, mass=5)

    holding = False
    pressed_ball = None

    while True:
        surface.fill(pg.Color('grey'))



        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()

            if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                run()

            if e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1:
                    create_ball(space, e.pos, radius=30)

            for ball in active_objects.get("balls"):

                if e.type == pg.MOUSEBUTTONDOWN and point_within_ball(pg.mouse.get_pos(), ball):
                    if e.button == 3:
                        holding = True
                        pressed_ball = ball


                if e.type == pg.MOUSEBUTTONUP and e.button == 3 and holding:
                    holding = False
                    # print("shoot")

                # if active_objects.get("balls"):
                    # ball = active_objects.get("balls")[-1]

                    mouse_pos = pg.mouse.get_pos()
                    angle = angle_points(pressed_ball.body.position, mouse_pos) + math.pi


                    mag = dist_points(pressed_ball.body.position, mouse_pos)
                    force = mag * 240


                    max_force = 20000
                    force = min(force, max_force)
                    x = math.cos(angle) * force
                    y = math.sin(angle) * force
                    pressed_ball.body.apply_impulse_at_local_point((x, y), (0, 0))

            if e.type == pg.MOUSEBUTTONDOWN and e.button == 2:
                for ball in active_objects.get("balls"):
                    print(point_within_ball(pg.mouse.get_pos(), pressed_ball))



        space.debug_draw(draw_options)
        handle_off_screen_objects(space, active_objects)
        space.step(1 / FPS)
        pg.display.flip()
        pg.display.set_caption(f"{clock.get_fps():.2f}")
        clock.tick(FPS)



if __name__ == '__main__':
    run()
    pg.quit()