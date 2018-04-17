import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import math, sys, random
import numpy as np

# TODO make sure total system energy is conserved (i.e. there should be no energy lost as "heat")
# TODO should we ensure that no two balls start in the same place?
"""
From https://www.frontiersin.org/articles/10.3389/fmicb.2016.01437/full
"Physics-Based Simulation Environment
In order to match observations at the macroscopic level with physical qualities of individual cells, the simulation 
strategy focused on discrete objects for both population(s) and medium to reproduce the motion of the bacteria through 
soft agar. Instead of having a single object to simulate an expanding (growing and swimming) colony, the simulation 
used several circular objects so that the overall structure could adapt its morphology to environmental constraints. 
Importantly, any given cellular-object did not represent a single cell, but a group of cells.
The simulation made use of the 2D rigid body physics library Chipmunk through its Python wrap Pymunk. This physics 
engine takes care of all collisions among shapes happening in the model. High accuracy is needed in solving collisions 
as the simulation relies on the effects of these events to shape the patterns. The simulation was built upon the 
physics engine Chipmunk, that uses the Gilbert–Johnson–Keerthi algorithm (Gilbert et al., 1988) to calculate distances 
between objects and the Expanding Polytope Algorithm to calculate penetrations (Bergen and Bergen, 2003). Upon 
collisions, an impulse is generated on the objects (consequence of the mechanical stress) that pushes the objects apart 
(measured in Figure 2C) and added to the velocity of the object to finally calculate the new moving vector."

http://chipmunk-physics.net/
http://www.pymunk.org
"""

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

### Physics stuff
space = pymunk.Space()
space.gravity = (0.0, 0.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

### walls
static_body = space.static_body
static_lines = [pymunk.Segment(static_body, (25.0, 25.0), (25.0, 575.0), 0.0),
                pymunk.Segment(static_body, (25.0, 25.0), (575.0, 25.0), 0.0),
                pymunk.Segment(static_body, (575.0, 575.0), (575.0, 25.0), 0.0),
                pymunk.Segment(static_body, (25.0, 575.0), (575.0, 575.0), 0.0)
                ]
for line in static_lines:
    line.elasticity = 1.0  # perfect elasticity, so no energy loss from collisions with walls
    line.friction = 0.0  # no energy loss due to friction
space.add(static_lines)

## Balls
### NOTE: sometimes the balls will pass through the walls if they are moving fast enough, see:
###  https://chipmunk-physics.net/forum/viewtopic.php?f=1&t=1919
balls = []
for b in range(500):
    mass = 30
    radius = 4
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)

    # random impulse
    impulse = (np.random.randint(-8000, 8000), np.random.randint(-8000, 8000))
    body.apply_impulse_at_local_point(impulse)

    # concerted impulse straight down
    # impulse = (0, -8000)
    # body.apply_impulse_at_local_point(impulse)

    # start from top left of box
    # x = random.randint(26, 300)
    # y = random.randint(300, 574)

    # start from top half of box
    # x = random.randint(26, 574)
    # y = random.randint(310, 574)

    # start from random
    x = random.randint(26, 574)
    y = random.randint(26, 574)

    # gradient impulse
    # if y > 300:
    #     impulse = (np.random.randint(-8000, 8000), np.random.randint(-8000, 8000))
    # else:
    #     impulse = (np.random.randint(-1000, 1000), np.random.randint(-1000, 1000))
    # body.apply_impulse_at_local_point(impulse)

    body.position = x, y
    shape = pymunk.Circle(body, radius, (0,0))
    shape.elasticity = 1.0
    shape.friction = 0.0
    space.add(body, shape)
    balls.append(shape)


# single blade (vane?) rotating paddle wheel
paddle_w = 100
paddle_h = 2
paddle_body_position = 250.0, 300.0
joint_point = (300.0, 300.0)

# double blade rotating paddle
# paddle_w = 200
# paddle_h = 2
# paddle_body_position = 300.0, 300.0
# joint_point = paddle_body_position

paddle_mass = 30
paddle_body = pymunk.Body(mass=paddle_mass, moment=pymunk.moment_for_box(paddle_mass, (paddle_w, paddle_h)))
paddle_body.position = paddle_body_position
paddle_shape = pymunk.Poly.create_box(paddle_body, (paddle_w, paddle_h))
paddle_shape.elasticity = 1.0
paddle_shape.friction = 0.0
paddle_shape.color = (0, 0, 0, 255)
space.add(paddle_body, paddle_shape)
pj_body = pymunk.Body(body_type=pymunk.Body.STATIC)
pj_body.position = paddle_body.position
pj = pymunk.PivotJoint(pj_body, paddle_body, joint_point)
pj.elasticity = 1.0
pj.friction = 0.0
space.add(pj)

timestep = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == KEYDOWN and event.key == K_p:
            pygame.image.save(screen, "bouncing_balls.png")

    ### Clear screen
    screen.fill(THECOLORS["white"])

    space.debug_draw(draw_options)

    ### Update physics
    dt = 1.0/120.0
    for x in range(2):
        timestep += 1
        kinetic_energies = []
        for ball in balls:
            kinetic_energies.append(ball.body.kinetic_energy)
        max_kinetic_energy = np.max(kinetic_energies)
        for ball in balls:
            red = (ball.body.kinetic_energy / max_kinetic_energy) * 255
            green = 255 - red
            blue = 255 - red
            ball.color = (red, green, blue, 255)
        print("%s, %s" % (timestep, paddle_body.angle))
        space.step(dt)

    ### Flip screen
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))
