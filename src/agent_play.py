import pygame

from config import framerate, screen_color, screen_height, screen_width
from event.convert import convert_pygame_event
from mediator import Mediator
from agents.dummy_agent import DummyAgent

# init
pygame.init()

# settings
flags = pygame.SCALED

# game constants initialization
screen = pygame.display.set_mode((screen_width, screen_height), flags, vsync=1)
clock = pygame.time.Clock()

mediator = Mediator()
station_idx = [0,1,2,3]

agent = DummyAgent(mediator)
agent.generate_paths()

while True:
    dt_ms = clock.tick(framerate)
    mediator.increment_time(dt_ms)
    screen.fill(screen_color)
    mediator.render(screen)
    mediator.assign_planned_paths(agent.planned_paths)

    # react to user interaction
    for pygame_event in pygame.event.get():
        if pygame_event.type == pygame.QUIT:
            raise SystemExit
        else:
            event = convert_pygame_event(pygame_event)
            mediator.react(event)

    pygame.display.flip()
