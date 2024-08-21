import pygame

from config import framerate, screen_color, screen_height, screen_width
from event.convert import convert_pygame_event
from mediator import Mediator
from agents.dummy_agent import DummyAgent
import copy

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
best_cost = 2**63
count = 0
best_count = 0
best_paths = None
stop_finding = 3000
while True:
    dt_ms = clock.tick(framerate)
    mediator.increment_time(dt_ms)
    screen.fill(screen_color)
    mediator.render(screen)
    # react to user interaction
    if count<stop_finding:
        agent.generate_paths()
        mediator.assign_planned_paths(agent.planned_paths)
        cost = mediator.calculate_cost_following_paths(print_data=False)
        if cost < best_cost:
            best_cost = cost
            best_paths = copy.deepcopy(agent.planned_paths)
            print(best_paths)
            best_count = count
        if cost:
            print("======================================")
            print("count: ", count)
            print("cost: ", cost)
            print("best_cost", best_cost)

        for path in mediator.paths:
            mediator.remove_path(path)
    elif count == stop_finding:
        if best_paths is None:
            mediator.assign_planned_paths(agent.planned_paths)
        else:
            mediator.assign_planned_paths(best_paths)
        cost = mediator.calculate_cost_following_paths(print_data=False)
        print("======================================")
        print(best_paths)
        print("cost: ", cost)
        print("best_count: ", best_count)
    count += 1
    
    
    for pygame_event in pygame.event.get():
        if pygame_event.type == pygame.QUIT:
            raise SystemExit
        else:
            event = convert_pygame_event(pygame_event)
            mediator.react(event)

    pygame.display.flip()
