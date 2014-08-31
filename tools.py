import pygame


NEUTRAL_COST = 10
OBSTACLE_COST = 500
BONUS_COST = 1
pygame.font.init()
myFont = pygame.font.Font("arial.ttf",15)
NODE_STEP = 30
pathfinding_delay = 10 # 0,5 secondes between each pathfinding