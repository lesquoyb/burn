import pygame
import character

class Explosion(pygame.sprite.Sprite):
    
    def __init__(self,radius,duration,position_center,obstacles,damage,explosions,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/explosion.png")
        self.rect = self.image.get_rect()
        self.rect.center = position_center
        self.radius = radius
        self.duration = duration
        self.obstacles = obstacles
        self.damage = damage
        self.screen = screen
        self.explosions = explosions
        self.explosions += [self]
        self.begin = pygame.time.get_ticks()
        
    def update(self):
        time = pygame.time.get_ticks()
        if (time - self.begin) >= self.duration:
            self.explosions.remove(self)
            self.kill()
        else:
            collisions = pygame.sprite.spritecollide(self,self.obstacles,False,pygame.sprite.collide_circle)
            for item in collisions:
                if isinstance(item,character.Character):
                    item.take_hit(self.damage)
                
    def draw(self):
        self.screen.blit(self.image,self.rect)
        