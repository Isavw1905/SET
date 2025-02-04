import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.smoothscale(image, (int(width * scale), int(height * scale)))
        self.rect = self. image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    #draw buttons on surface and check if they are clicked
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                action = True
                self.clicked = False
            
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
