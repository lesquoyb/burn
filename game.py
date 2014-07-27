import pygame
import cat
import player
import math
import wall
import bullet
import healthBonus
import map

from pygame.locals import * 
from sys import exit
WIDTH = 620
HEIGHT = 480
	
	
def changing_weapon(event,player,previous):
	time = pygame.time.get_ticks()
	if time - previous > 80:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.next_weapon()
			elif event.key == pygame.K_e:
				player.previous_weapon()
	return time

def print_player_info(player,screen):
	# render text
	myfont = pygame.font.SysFont("monospace", 15)	
	ammo = myfont.render("ammo: "+ str(player.weapons[player.selected_weapon].ammo), 1, (255,255,0))
	weapon = myfont.render("current weapon: " + player.weapons[player.selected_weapon].name,1,(255,255,0))
	health = myfont.render("health: " + str(player.health),1,(255,255,0))
	armor = myfont.render("armor: " + str(player.armor),1,(255,255,0))
	
	screen.blit(ammo, (0, 0))
	screen.blit(weapon,(0,20))
	screen.blit(health,(0,HEIGHT-20))
	screen.blit(armor,(WIDTH-100,HEIGHT-20))
	

	
	
# init pygame and the game window
pygame.init()	
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Best game ever")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()




#load images and initial positions
allSprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

background = pygame.image.load("images/background.jpg").convert()

enemy = cat.Cat((50,50),obstacles)
player = player.Player((WIDTH/2,50),obstacles)

obstacles.add(player)
obstacles.add(enemy)

sight = pygame.image.load("images/aim.png").convert()
sight_pos = (WIDTH/2,60)

allSprites.add(player)
allSprites.add(enemy)


#building walls
prev=0
for i in range(10):
	wall1 = wall.Wall((prev*i,200))
	prev=wall1.image.get_width()
	allSprites.add(wall1)
	obstacles.add(wall1)

#positionning bonuses
bonus = healthBonus.HealthBonus((150,150),allSprites)

map1 = map.Map(background,(0,0),obstacles,allSprites)
#game loop
end = False
pygame.key.set_repeat(10, 35)
previous = pygame.time.get_ticks()
while not end:
	key = pygame.key.get_pressed()	
	if key[pygame.K_z] or key[pygame.K_UP]:
		player.move_up()
	if key[pygame.K_s] or key[pygame.K_DOWN]:
		player.move_down()			
	if key[pygame.K_q] or key[pygame.K_LEFT]:
		player.move_left()			
	if key[pygame.K_d]or key[pygame.K_RIGHT]:
		player.move_right()

	for event in pygame.event.get():
		if event.type == QUIT:
			end = True
		previous = changing_weapon(event,player,previous)			
		if event.type == MOUSEMOTION:
			sight_pos = (event.pos[0],event.pos[1])
		
	click = pygame.mouse.get_pressed()
	if click[0]:#if the left button of the mouse is pressed
		player.fire(pygame.mouse.get_pos(),allSprites)	

	#update objects
	#allSprites.update()
	map1.update()
	
	#moving the map if necessary
	
	right_dist = WIDTH /2 + WIDTH/20
	if player.rect.right >= right_dist:
		diff = player.rect.right - right_dist
		player.rect.right = right_dist
		map1.scroll_width(-diff)
	left_dist = WIDTH/2 - WIDTH/20
	if player.rect.left <= left_dist:
		diff = left_dist - player.rect.left
		player.rect.left = left_dist
		map1.scroll_width(diff)
		
	top_dist = HEIGHT/2 - HEIGHT/20
	if player.rect.top <= top_dist:
		diff = top_dist - player.rect.top
		player.rect.top = top_dist
		map1.scroll_height(diff)
		
	bottom_dist = WIDTH/2 + WIDTH/20
	if player.rect.bottom >= bottom_dist:
		diff = bottom_dist - player.rect.bottom
		player.rect.bottom = bottom_dist
		map1.scroll_height(diff)		
	
	#print images
	map1.draw(screen)
	#screen.blit(background,(0,0))
	#allSprites.draw(screen)
	print_player_info(player,screen)
	screen.blit(sight,sight_pos)	
	
	
	
	pygame.display.flip()
	clock.tick(60)
	
	
	
pygame.quit()