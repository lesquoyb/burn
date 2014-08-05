import pygame
import character
import abc

class DroppableObject(pygame.sprite.Sprite):
    
    
    
    def __init__(self,icon,position,sprites,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(icon).convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.player = player
        sprites.add(self)
        self.sprites = sprites
        
        
    @abc.abstractmethod
    def dropped(self,by):
        pass
    
    def update(self,*args):
        if (pygame.sprite.collide_rect(self,self.player) ):
            self.dropped(self.player)
            self.__delete__()
        else:
            collisions = pygame.sprite.spritecollide(self,self.sprites,False)
            for object in collisions:
                if  isinstance(object,character.Character):
                    self.dropped(object)
                    self.__delete__()
    
    def __delete__(self):
        self.kill()