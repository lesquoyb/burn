import pygame
import os


NEUTRAL_COST = 10
OBSTACLE_COST = 500
BONUS_COST = 1
pygame.font.init()
myFont = pygame.font.Font("arial.ttf",15)
NODE_STEP = 50
pathfinding_delay = 500 # 0,5 secondes between each pathfinding