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
        if self.movements_made != self.scope:
            
            #test collisions on the x axis
            move_x = self.speed* math.cos(self.angle)
            self.rect.x += move_x
            collisions = pygame.sprite.spritecollide(self,self.obstacles,False)
            for collision in collisions:
                if collision is not self.shooter:
                    self.rect.x -= move_x
                    if (self.rect.x < collision.rect.x):
                        self.rect.right = collision.rect.left
                    else:
                        self.rect.left = collision.rect.right
                    if isinstance(collision,character.Character):
                        collision.take_hit(self.damage)
                    self.__delete__()   
                    
            #test collisions on the y axis
            move_y = self.speed* math.sin(self.angle)
            self.rect.y -= move_y
            collisions = pygame.sprite.spritecollide(self,self.obstacles,False)
            for collision in collisions:
                if collision is not self.shooter:
                    self.rect.y += move_y
                    if( self.rect.y < collision.rect.y):
                        self.rect.bottom = collision.rect.top
                    else:
                        self.rect.top = collision.rect.bottom
                    if isinstance(collision,character.Character):
                        collision.take_hit(self.damage)
                    self.__delete__()
                    
            self.movements_made += 1
        else:
            self.__delete__()
    
    def __delete__(self):
        self.kill()
        
    