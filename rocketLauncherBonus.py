import droppableObject
import rocketLauncher
import pygame

class rocketLauncherBonus(droppableObject.DroppableObject):
    
    def __init__(self,position,sprites,player):
        droppableObject.DroppableObject.__init__(self,"images/rocketLauncher.jpe",position,sprites,player)

        
        
    def pick_up(self,by):
        i = 0
        for weapon in by.weapons:
            if isinstance(weapon,rocketLauncher.RocketLauncher):
                by.weapons[i].ammo += 5                
                break
            i+=1      
        else:
            by.weapons += [rocketLauncher.RocketLauncher(3) ]         
        