from pygame.math import Vector2 as vc
import pygame


class Node:
    def __init__(self, data, pos, dx):
        self.data = data
        self.left = None
        self.right = None
        self.pos = pos
        self.dx = dx

    def insert__(self, data):
        if self.data >= data:
            if (self.left == None):
                new = Node(data, vc(self.pos.x-self.dx,
                           self.pos.y+75), self.dx*0.5)
                self.left = new
                return new
            else:
                return self.left.insert__(data)
        else:
            if (self.right == None):
                new = Node(data, vc(self.pos.x+self.dx,
                           self.pos.y+75), self.dx*0.5)
                self.right = new
                return new
            else:
                return self.right.insert__(data)

    def draw_node(self, screen, radius):
        if (self.left):
            pygame.draw.aaline(screen, (0, 0, 0), self.pos, self.left.pos, 5)
        if (self.right):
            pygame.draw.aaline(screen, (0, 0, 0), self.pos, self.right.pos, 5)
        font = pygame.font.Font(None, 25)
        data = font.render(str(self.data), True, (255, 255, 255))
        pygame.draw.circle(screen, (0, 255, 0), self.pos, radius)
        screen.blit(data, (self.pos.x-25//2, self.pos.y-25//2))
