import pygame
import character
from math import *

class Bullet(pygame.sprite.Sprite):
    
    movements_made = 0
    speed = 10
    
    move_x = 1
    move_y = 1
    
    def __init__(self,destination,group,obstacles,shooter,scope,damage):
        position = (shooter.rect.x,shooter.rect.y)
        self.damage = damage
        self.scope = scope
        self.group = group
        self.obstacles = obstacles
        self.shooter = shooter
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load("images/bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        if position[0] > destination[0]:
            self.move_x = -1
        if position[1] > destination[1]:
            self.move_y = -1
        dist_x = sqrt((destination[0] - position[0])**2)
        dist_y = sqrt((destination[1] - position[1])**2)
        if dist_x > dist_y:
            self.move_y = self.move_y * (dist_y/ dist_x)
        else:
            self.move_x = self.move_x * (dist_x / dist_y)
        self.group.add(self)
            
        
        
    def update(self):
        if self.movements_made != self.scope:
                self.rect.x += self.speed*self.move_x
                self.rect.y += self.speed*self.move_y
                self.movements_made += 1
                collisions = pygame.sprite.spritecollide(self,self.obstacles,False)
                for collision in collisions:
                    if collision is not self.shooter:
                        if isinstance(collision,character.Character):
                            collision.take_hit(self.damage)
                        self.__delete__()
        else:
            self.__delete__()
    
    def __delete__(self):
        pygame.sprite.Sprite.remove(self,self.group)