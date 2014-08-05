import pygame
import player


class Map(pygame.sprite.Sprite):
    

    rooms = []
    
    def __init__(self,background,starting_point,obstacles,sprites):
        pygame.sprite.Sprite.__init__(self)
        self.image =background
        self.obstacles = obstacles
        self.sprites = sprites
        self.rect = self.image.get_rect()
        self.rect.x = starting_point[0]
        self.rect.y = starting_point[1]
        self.player = player
        
        
        
    def update(self,*args):
        for obstacle in self.obstacles:
            obstacle.update()
        for sprite in self.sprites:
            sprite.update()
            
            
    def draw(self,screen):
        screen.blit(self.image,(0,0))
        self.sprites.draw(screen)
        
        
    def scroll_width(self,distance):
        for obstacle in self.obstacles:
            if not isinstance(obstacle,player.Player):
                obstacle.rect.x += distance
        for sprite in self.sprites:
            if sprite not in self.obstacles:
                sprite.rect.x += distance
        
    def scroll_height(self,distance):
        for obstacle in self.obstacles:
            if not isinstance(obstacle,player.Player):
                obstacle.rect.y += distance
        for sprite in self.sprites:
            if sprite not in self.obstacles:
                sprite.rect.y += distance   
                
        