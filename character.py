import pygame
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

    def update(self):
        
              
        # we look if there is collision after moving on the right/left  
        self.rect.x += self.move_x        
        colliding_objects = pygame.sprite.spritecollide(self,self.game.obstacles ,False)
        for object in colliding_objects:
            if object is not self:
                #if collision, we must stick the player to the object
                if self.move_x>0:
                    self.rect.right = object.rect.left
                elif self.move_x<0:
                    self.rect.left = object.rect.right
        #forbid the player to exit the map
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > self.screen.get_rect().width:
            self.rect.right = self.screen.get_rect().width
                
        # we look if there is collision after moving to the top/bottom
        self.rect.y += self.move_y        
        colliding_objects = pygame.sprite.spritecollide(self,self.game.obstacles,False)
        for object in colliding_objects:
            if object is not self:
                if self.move_y > 0:
                    self.rect.bottom = object.rect.top
                elif self.move_y < 0 :
                    self.rect.top = object.rect.bottom
        #forbid the character to exit the map
        if self.rect.y < 0:
            self.rect.y = 0  
        elif self.rect.bottom > self.screen.get_rect().height:
            self.rect.bottom = self.screen.get_rect().height 
            
        #once the movement done, we reinitialize the vector
        self.move_x = 0
        self.move_y = 0
     

    def __init__(self,image,dead,position,screen,game):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.dead = pygame.image.load(dead).convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.game = game
           

    def fire(self,destination,sprites):
        dx = destination[0] - self.rect.centerx
        dy = destination[1] - self.rect.centery
        rads = atan2(-dy,dx)
        rads %= 2*pi
        self.weapons[self.selected_weapon].fire(rads,sprites,self.game.obstacles,self)

    
    
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
        self.game.obstacles.remove(self)
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
        self.move_y -= self.speed
        
    def move_down(self):
        self.move_y += self.speed
        
    def move_left(self):
        self.move_x -= self.speed
        
    def move_right(self):
        self.move_x += self.speed
        
    def change_weapon(self,key):
        time = pygame.time.get_ticks()
        if time - self.previous > 80:
            if key[pygame.K_a]:
                self.next_weapon()
            elif key[pygame.K_e]:
                self.previous_weapon()
            return time   
        else:
            return self.previous
            
    
    
    