import pygame
import sys


class textbox:
    def __init__(self, surface, pos):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.dim = pygame.Vector2(surface[0], surface[1])
        self.rect = pygame.Rect(self.pos, self.dim)
        self.text = ''
        self.focus = False
        self.color = (0, 0, 0)

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for ev in events:
            if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.focus = True
            else:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.focus = False
            if self.focus:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_BACKSPACE:
                        if self.text:
                            self.text = self.text[:-1]
                    elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                        if self.text:
                            temp = self.text
                            self.text = ""
                            return temp
                    else:
                        self.text += ev.unicode
                        self.text = self.text[:3]
        pygame.event.clear()
        return None

    def display(self, screen):
        font = pygame.font.Font(None, 25)
        data = font.render(str(self.text), True, (255, 255, 255))
        if self.focus:
            self.color = (0, 15, 255)
        else:
            self.color = (0, 0, 0)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(data, (self.pos.x+self.dim.x//6, self.pos.y+self.dim.y//4))
