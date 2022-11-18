import pygame


class button:
    def __init__(self, surface, pos, text):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.dim = pygame.Vector2(surface[0], surface[1])
        self.rect = pygame.Rect(self.pos, self.dim)
        self.text = text
        self.focus = False
        self.color = (0, 0, 0)

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                if event.type == pygame.MOUSEBUTTONDOWN and self.focus == False:
                    self.focus = True

    def display(self, screen):
        font = pygame.font.Font(None, 25)
        data = font.render(str(self.text), True, (255, 255, 255))
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
        screen.blit(data, (self.pos.x+self.dim.x//6, self.pos.y+self.dim.y//4))


class textbox(button):
    def __init__(self, surface, pos, text):
        super().__init__(surface, pos, text)
        self.cursor = pygame.Rect((self.dim.x//6, self.dim.y//4), (2, 20))
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
                            self.cursor.x -= 10
                    elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                        if self.text:
                            temp = self.text
                            self.text = ""
                            self.cursor.x = self.dim.x//6
                            return temp
                    else:
                        self.text += ev.unicode
                        self.cursor.x += 10
                        self.cursor.x = max(
                            self.dim.x//6, min(self.dim.x//6+10*3, self.cursor.x))
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
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
        if not self.flag:
            if current_frame_time-self.frame_time >= 0.5*self.cooldown:
                self.draw = True
            if current_frame_time-self.frame_time >= self.cooldown:
                self.draw = False
                self.frame_time = current_frame_time
            if self.draw:
                pygame.draw.rect(screen, (255, 255, 255), self.cursor)
            if current_frame_time-self.frame_time >= self.cooldown:
                self.draw = False
        screen.blit(data, (self.pos.x+self.dim.x//6, self.pos.y+self.dim.y//4))
