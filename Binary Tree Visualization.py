from random import randint
import pygame
import sys
from tree import binary_tree
from textbox import textbox

pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
stack_counter = 0
FPS = 60

bt1 = binary_tree(50, width/2, 50, 200)

for i in range(0, 5):
    bt1.add_node(randint(40, 60))


def input_node(bt):
    n = int(input("enter the value of the new node:"))
    bt.add_node(n)


box = textbox((200, 50), (0, 0))


def main():
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
                bt1.add_node(int(a))
        current_frame_time = pygame.time.get_ticks()
        box.display(screen, current_frame_time)
        bt1.draw_tree(screen, 20)
        clock.tick(FPS)
        pygame.display.flip()


main()
