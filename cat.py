import character
import pygame

class Cat(character.Character):
    
    
    def __init__(self,position,obstacles):
        character.Character.__init__(self,"images/enemy.jpg","images/dead_cat.jpg",position,obstacles)
        
        
    