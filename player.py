import character
import pygame
import gun
import shotgun

class Player(character.Character):
    
    
    def __init__(self,position,obstacles):
        character.Character.__init__(self,"images/player.jpg","images/dead_player.jpg",position,obstacles)
        
        #the player begin the game with a gun and 10 ammos
        self.weapons += [gun.Gun(1000)]
        self.weapons += [shotgun.Shotgun(10)]
        
        
    def update(self):
        character.Character.update(self)
            