import pygame
import sys
from tree import binary_tree
from textbox import *

pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
stack_counter = 0
FPS = 60
box = textbox((200, 50), (0, 0), 'input Number here')
reset = button((70, 40), (10, 60), 'Reset')
bt = None


def main():
    global bt
    while (1):
        flag = True
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))
        a = box.update(events)
        if a:
            try:
                int(a)
            except ValueError:
                flag = False
            if flag:
                if not bt:
                    bt = binary_tree(int(a), 450, 50, 200)
                else:
                    bt.add_node(int(a))
        current_frame_time = pygame.time.get_ticks()
        box.display(screen, current_frame_time)
        reset.display(screen)
        reset.update(events)
        if reset.focus:
            bt = None
            reset.focus = False
        if bt:
            bt.draw_tree(screen, 20)
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main()
