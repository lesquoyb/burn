import pygame
import random
import map

class Building(pygame.sprite.Group):
    
    door = pygame.sprite.Sprite()
    house =  pygame.sprite.Sprite()
    bonuses = []
    explosions = []
    buildings = []
    
    def __init__(self,position,screen,name):
        self.screen = screen
        pygame.sprite.Group.__init__(self)
        self.door.image = pygame.image.load("images/door.png").convert()
        self.house.image = pygame.image.load("images/house.png")
        inside = pygame.sprite.Sprite()
        inside.image = pygame.image.load("images/inside_house.png").convert()
        inside.rect = inside.image.get_rect()
        background = pygame.image.load("images/background.jpg").convert()
        self.obstacles = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group(inside)
        self.inside = map.Map(background,(0,0),self.obstacles,self.allSprites,self.bonuses,self.explosions,self.buildings)
        self.add(self.door)
        self.add(self.house)        
        self.door.rect = self.door.image.get_rect()
        self.house.rect = self.house.image.get_rect()
        self.house.rect.x = position[0]
        self.house.rect.y = position[1]
        self.rect = self.house.rect
        self.door.rect.x = random.randint(self.house.rect.x,self.house.rect.x+self.house.rect.width-self.door.rect.width)
        self.door.rect.y = self.house.rect.y + self.house.rect.height -self.door.rect.height
        self.name = name
        
        
    def draw(self):
        self.screen.blit(self.house.image,self.house.rect)
        self.screen.blit(self.door.image,self.door.rect)
        
    