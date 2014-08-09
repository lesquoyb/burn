import bullet
import pygame
import explosion

class Rocket(bullet.Bullet):
    
    explosion_radius = 30
    explosion_duration = 20
    
    
    def __delete__(self):
        explos = explosion.Explosion(self.explosion_radius,self.explosion_duration,self.rect.center,self.obstacles,self.damage,self.explosions,self.screen)
        self.kill()
    
    def __init__(self,angle,group,obstacles,shooter,scope,damage,explosions,screen):
            bullet.Bullet.__init__(self,angle,group,obstacles,shooter,scope,damage)
            pygame.display.init()
            self.image = pygame.image.load("images/rocket.jpe").convert()
            self.explosions = explosions
            self.screen = screen
    