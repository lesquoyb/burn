import pygame
import abc

class Weapon(pygame.sprite.Sprite):
    
    ammo = 0
    damage = 10
    name = ""
    
    @abc.abstractmethod
    def fire(self,angle,sprites,obstacles,shooter):
        return
            
    
    def __init__(self,ammo):
        self.prev_time = pygame.time.get_ticks()
        pygame.sprite.Sprite.__init__(self)
        self.ammo = ammo
