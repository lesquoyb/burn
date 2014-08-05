import pygame
import character
import math

class Bullet(pygame.sprite.Sprite):
    
    movements_made = 0
    speed = 15
    
    move_x = 1
    move_y = 1
    
    def __init__(self,angle,group,obstacles,shooter,scope,damage):
        position = shooter.rect.center
        self.damage = damage
        self.scope = scope
        self.obstacles = obstacles
        self.shooter = shooter
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load("images/bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.angle = angle
        group.add(self)
            
        
        
    def update(self):
        current_angle = 0        
        if self.movements_made != self.scope:
            self.rect.x += self.speed* math.cos(self.angle)
            self.rect.y -= self.speed* math.sin(self.angle)
            self.movements_made += 1
            collisions = pygame.sprite.spritecollide(self,self.obstacles,False)
            for collision in collisions:
                if collision is not self.shooter:
                    self.rect.x = collision.rect.x
                    self.rect.y = collision.rect.y
                    if isinstance(collision,character.Character):
                        collision.take_hit(self.damage)
                    self.__delete__()
        else:
            self.__delete__()
    
    def __delete__(self):
        self.kill()