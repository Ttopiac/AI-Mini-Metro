import pygame

from config import framerate, screen_color, screen_height, screen_width
from event.convert import convert_pygame_event
from mediator import Mediator

# init
pygame.init()

# settings
flags = pygame.SCALED

# game constants initialization
screen = pygame.display.set_mode((screen_width, screen_height), flags, vsync=1)
clock = pygame.time.Clock()

mediator = Mediator()
station_idx = [0,1,2,3]
pre_cost = 2**63

while True:
    dt_ms = clock.tick(framerate)
    mediator.increment_time(dt_ms)
    screen.fill(screen_color)
    mediator.render(screen)
    cost = mediator.calculate_cost_following_paths(print_data=False)
    if pre_cost != cost:
        print("current_cost: ", cost)
        pre_cost = cost

    # react to user interaction
    for pygame_event in pygame.event.get():
        if pygame_event.type == pygame.QUIT:
            raise SystemExit
        else:
            event = convert_pygame_event(pygame_event)
            mediator.react(event)

    pygame.display.flip()
