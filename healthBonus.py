import pygame
import droppableObject

class HealthBonus(droppableObject.DroppableObject):
    
    
    def __init__(self,position,sprites,player):
        droppableObject.DroppableObject.__init__(self,"images/healthBonus.jpg",position,sprites,player)
        
        
    def pick_up(self,by):
        by.health += 30