import pygame

class Wall(pygame.sprite.Sprite):
    
    
    def __init__(self,position):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/wall.jpe").convert()        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]