import pygame


class textbox:
    def __init__(self, surface, pos):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.dim = pygame.Vector2(surface[0], surface[1])
        self.rect = pygame.Rect(self.pos, self.dim)
        self.type_rect = pygame.Rect((self.dim.x//6, self.dim.y//4), (2, 20))
        self.text = 'input number here'
        self.focus = False
        self.color = (0, 0, 0)
        self.flag = True
        self.frame_time = 0
        self.cooldown = 1000
        self.draw = False

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for ev in events:
            if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.focus = True
                    if self.flag:
                        self.text = ''
                        self.flag = False
            else:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.focus = False
                    self.flag = True
            if self.focus:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_BACKSPACE:
                        if self.text:
                            self.text = self.text[:-1]
                            self.type_rect.x -= 10
                    elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                        if self.text:
                            temp = self.text
                            self.text = ""
                            self.type_rect.x = self.dim.x//6
                            return temp
                    else:
                        self.text += ev.unicode
                        self.type_rect.x += 10
                        self.type_rect.x = max(
                            self.dim.x//6, min(self.dim.x//6+10*3, self.type_rect.x))
                        self.text = self.text[:3]
        pygame.event.pump()
        return None

    def display(self, screen, current_frame_time):
        font = pygame.font.Font(None, 25)
        data = font.render(str(self.text), True, (255, 255, 255))
        if self.focus:
            self.color = (0, 15, 255)
        else:
            self.color = (0, 0, 0)
        pygame.draw.rect(screen, self.color, self.rect)
        if not self.flag:
            if current_frame_time-self.frame_time >= self.cooldown:
                self.draw = True
            if current_frame_time-self.frame_time >= 2.25*self.cooldown:
                self.draw = False
                self.frame_time = current_frame_time
            if self.draw:
                pygame.draw.rect(screen, (255, 255, 255), self.type_rect)
            if current_frame_time-self.frame_time >= self.cooldown:
                self.draw = False
        screen.blit(data, (self.pos.x+self.dim.x//6, self.pos.y+self.dim.y//4))
