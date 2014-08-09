import pygame
import player


class Map(pygame.sprite.Sprite):
    

    rooms = []
    
    def __init__(self,background,starting_point,obstacles,sprites,bonuses,explosions,buildings):
        pygame.sprite.Sprite.__init__(self)
        self.image =background
        self.obstacles = obstacles
        self.sprites = sprites
        self.rect = self.image.get_rect()
        
        (self.rect.x,self.rect.y ) = (-starting_point[0],-starting_point[1])
        self.bonuses = bonuses
        self.explosions = explosions
        self.buildings = buildings
        
        
        
    def update(self,*args):
        for obstacle in self.obstacles:
            obstacle.update()
        for sprite in self.sprites:
            sprite.update()

        for explosion in self.explosions:
            explosion.update()
            
            
    def draw(self,screen,player):
        self.move_camera(screen,player)
        screen.blit(self.image,self.rect)
        self.sprites.draw(screen)
        for building in self.buildings:
            building.draw()	
        for explosion in self.explosions:
            explosion.draw()        
        
        
    def move_camera(self,screen,player):
        #moving the map if necessary
        rect = screen.get_rect()
        WIDTH = rect.width
        HEIGHT = rect.height
        
        right_dist = WIDTH /2 + WIDTH/20
        if player.rect.right >= right_dist:
            if self.rect.right > WIDTH:
                diff = player.rect.right - right_dist
                player.rect.right = right_dist
                self.scroll_width(-diff)
            else:
                self.rect.right=WIDTH
            
        left_dist = WIDTH/2 - WIDTH/20
        if player.rect.left <= left_dist:
            if self.rect.left < 0:
                diff = left_dist - player.rect.left
                player.rect.left = left_dist
                self.scroll_width(diff)
            else:
                self.rect.left = 0
    
        top_dist = HEIGHT/2 - HEIGHT/20
        if player.rect.top <= top_dist:
            if self.rect.top < 0:
                diff = top_dist - player.rect.top
                player.rect.top = top_dist
                self.scroll_height(diff)
            else:
                self.rect.top = 0
    
        bottom_dist = HEIGHT/2 + HEIGHT/20
        if player.rect.bottom >= bottom_dist:
            if self.rect.bottom > HEIGHT:
                diff = bottom_dist - player.rect.bottom
                player.rect.bottom = bottom_dist
                self.scroll_height(diff)  
            else:
                self.rect.bottom = HEIGHT
        
    def scroll_width(self,distance):
        for obstacle in self.obstacles:
            if not isinstance(obstacle,player.Player):
                obstacle.rect.x += distance
        for sprite in self.sprites:
            if sprite not in self.obstacles:
                sprite.rect.x += distance
        for explosion in self.explosions:
            explosion.rect.x += distance
        self.rect.x +=distance
        
    def scroll_height(self,distance):
        for obstacle in self.obstacles:
            if not isinstance(obstacle,player.Player):
                obstacle.rect.y += distance
        for sprite in self.sprites:
            if sprite not in self.obstacles:
                sprite.rect.y += distance 
        for explosion in self.explosions:
            explosion.rect.y += distance  
        self.rect.y += distance
                
        