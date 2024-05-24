import os
import sys
import unittest
from unittest.mock import MagicMock, create_autospec

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import pygame

from config import screen_height, screen_width
from entity.get_entity import get_random_stations
from event.keyboard import KeyboardEvent
from event.mouse import MouseEvent
from event.type import KeyboardEventType, MouseEventType
from geometry.point import Point
from mediator import Mediator
from utils import get_random_color, get_random_position


width, height = screen_width, screen_height
screen = create_autospec(pygame.surface.Surface)
position = get_random_position(width, height)
color = get_random_color()
mediator = Mediator()
pygame.draw = MagicMock()
mediator.render(screen)

station_idx = [0,1,2,3]

mediator.react(
    MouseEvent(
        MouseEventType.MOUSE_DOWN,
        mediator.stations[station_idx[0]].position,
    )
)
for idx in station_idx[1:]:
    mediator.react(
        MouseEvent(
            MouseEventType.MOUSE_MOTION, mediator.stations[idx].position
        )
    )
mediator.react(
    MouseEvent(
        MouseEventType.MOUSE_UP,
        mediator.stations[station_idx[-1]].position,
    )
)