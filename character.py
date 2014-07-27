import pygame
import abc
import threading

class Character(pygame.sprite.Sprite):

    state = 'alive'
    armor = 0
    speed = 10
    health = 100
    weapons = []
    selected_weapon = 0
    move_x = 0
    move_y = 0

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
                
        self.move_x =0
        self.move_y = 0

    def __init__(self,image,dead,position,obstacles,):
        self.obstacles = obstacles
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.dead = pygame.image.load(dead).convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
    

    def fire(self,destination,sprites):
        self.weapons[self.selected_weapon].fire(destination,sprites,self.obstacles,self)
    
    
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
        
        timer = threading.Timer(3.0,self.__delete__)
        timer.start()
    
    def take_hit(self,damage):
        self.health = self.health - damage + self.armor
        if (self.health<=0):
            self.die()
            
            
    def __delete__(self):
        pygame.sprite.Sprite.kill(self)
    
    def move_up(self):
        self.move_y -= 10
        
    def move_down(self):
        self.move_y += 10
        
    def move_left(self):
        self.move_x -= 10
        
    def move_right(self):
        self.move_x += 10
            
    
    
    