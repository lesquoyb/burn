import pygame
import droppableObject

class HealthBonus(droppableObject.DroppableObject):
    
    
    def __init__(self,position,sprites):
        droppableObject.DroppableObject.__init__(self,"images/healthBonus.jpg",position,sprites)
        
        
    def dropped(self,by):
        by.health += 30