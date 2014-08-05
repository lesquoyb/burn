import pygame
import abc
import threading
from math import atan2, degrees, pi


class Character(pygame.sprite.Sprite):

    INITIAL_LIFE = 100
    state = 'alive'
    armor = 0
    speed = 10
    health = INITIAL_LIFE
    weapons = []
    selected_weapon = 0
    move_x = 0
    move_y = 0
    isNear = []
    proximity_circle = pygame.sprite.Sprite()

        
    @abc.abstractmethod
    def update(self,*args):
        # we look if there is collision after moving on the right/left
        self.rect.x += self.move_x
        colliding_objects = pygame.sprite.spritecollide(self,self.obstacles ,False)
        for object in colliding_objects:
            if object is not self:
                #if we collide, we must stick the player to the object
                if self.move_x>0:
                    self.rect.right = object.rect.left
                elif self.move_x<0:
                    self.rect.left = object.rect.right
                
        # we look if there is collision after moving to the top/bottom
        self.rect.y += self.move_y
        colliding_objects = pygame.sprite.spritecollide(self,self.obstacles,False)
        for object in colliding_objects:
            if object is not self:
                if self.move_y > 0:
                    self.rect.bottom = object.rect.top
                elif self.move_y < 0 :
                    self.rect.top = object.rect.bottom
        self.move_x = 0
        self.move_y = 0
     

    def __init__(self,image,dead,position,obstacles,screen):
        self.obstacles = obstacles
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.dead = pygame.image.load(dead).convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
      

    def fire(self,destination,sprites):
        dx = destination[0] - self.rect.centerx
        dy = destination[1] - self.rect.centery
        rads = atan2(-dy,dx)
        rads %= 2*pi
        self.weapons[self.selected_weapon].fire(rads,sprites,self.obstacles,self)
    
    
    def next_weapon(self):
        if self.selected_weapon == len(self.weapons) - 1:
            self.selected_weapon = 0
        else:
            self.selected_weapon +=1
            
    def previous_weapon(self):
        if self.selected_weapon == 0:
            self.selected_weapon = len(self.weapons)-1
        else:
            self.selected_weapon -=1    

    def die(self):
        self.state="dead"  
        self.image = self.dead
        self.obstacles.remove(self)
        timer = threading.Timer(3.0,self.__delete__)
        timer.start()
    
    def take_hit(self,damage):
        self.health = self.health - damage + self.armor
        if (self.health<=0):
            self.die()
            
            
    def printLife(self):
        myFont = pygame.font.Font("monospace",15)
        self.screen.render(str(self.health)+ " / " + str(self.INITIAL_LIFE),1,(255,0,0))
            
    def __delete__(self):
        self.proximity_circle.kill()
        self.kill()
        
    def move_up(self):
        self.move_y -= 10
        
    def move_down(self):
        self.move_y += 10
        
    def move_left(self):
        self.move_x -= 10
        
    def move_right(self):
        self.move_x += 10
        
    def changing_weapon(self,event,previous):
        time = pygame.time.get_ticks()
        if time - previous > 80:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.next_weapon()
                elif event.key == pygame.K_e:
                    self.previous_weapon()
        return time    
            
    
    
    