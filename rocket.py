import bullet
import pygame

class Rocket(bullet.Bullet):
    
    
    
        def __init__(self,angle,group,obstacles,shooter,scope,damage):
                bullet.Bullet.__init__(self,angle,group,obstacles,shooter,scope,damage)
                pygame.display.init()
                self.image = pygame.image.load("images/rocket.jpe").convert()
    