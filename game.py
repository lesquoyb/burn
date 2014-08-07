import pygame
import cat
import player
import math
import wall
import bullet
import healthBonus
import building
import map
import dialogBox
import rocketLauncherBonus

from pygame.locals import * 
from sys import exit


class Game():
    
    WIDTH = 1920
    HEIGHT = 1020
    buildings = []
    
    
    
    def __init__(self):
        # init pygame and the game window
        pygame.init()	
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))        
        self.background = pygame.image.load("images/background.jpg").convert()
        self.clock = pygame.time.Clock()
        self.allSprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        pygame.display.set_caption("Best game ever")
        self.sight = pygame.sprite.Sprite()
        self.sight_group = pygame.sprite.Group()
        self.dialogBoxes = []
        pygame.mouse.set_visible(False)
        self.bonuses = []
        #load images and initial positions
        enemy = cat.Cat((50,50),self.screen,self)
        
        self.obstacles.add(enemy)
        
        self.sight.image = pygame.image.load("images/aim.png").convert()
        self.sight.rect = self.sight.image.get_rect()
        self.sight_group.add(self.sight)
        self.allSprites.add(enemy)
        
        house = building.Building((-500,-50),self.screen,"firstHouse")
        self.obstacles.add(house)
        self.buildings += [house]         
        #building walls  
        prev=0
        for i in range(10):
            wall1 = wall.Wall((prev*i,200))
            prev=wall1.image.get_width()
            self.allSprites.add(wall1)
            self.obstacles.add(wall1)
           
        box = dialogBox.DialogBox("Salut et bienvenue dans le monde de burn, ici tu découvriras plein de choses merveilleuses, comme les chat et les chaussettes par exemple.Mais aussi des murs et des maisons! Comme je dois tester cette boite de dialogue il va falloir que j'écrive quelque chose de long, c'est pourquoi je propose d'en profiter pour faire un rapide tutoriel: Commencons par les déplacements: rien de plus simple tu peux utiliser les flêches ou les touches'z','q','s' et 'd' pour bouger(oui c'est bien toi la chaussure au milieu de l'écran). Ensuite je suppose que tu as remarqué cette jolie cible sur l'écran? Il s'agit de ton viseur, tu peux le déplacer grace à ta souris.Ce qui me mène au point suivant: BASTON !!!! Tu disposes de plusieurs armes (3 au moment ou j'ecris ces lignes) utilise les touches 'a' et 'e' pournaviguer entres elles. Tu vois ce truc répugnant sur ta gauche? Oui oui le chat, il est temps pour lui de mourir! vise le et utilise le clickgauche de la souris pour tirer. Voila je pense que c'est assez pour aujourd'hui je te laisse te débrouiller :)."
                                        ,self.screen,self)
        self.dialogBoxes += [box]
        self.map1 = map.Map(self.background,(0,0),self.obstacles,self.allSprites)        
        self.player = player.Player((self.WIDTH/2,50),self.screen,self)
        self.obstacles.add(self.player)
        #positionning bonuses
        self.bonuses += [healthBonus.HealthBonus((150,150),self.allSprites,self.player)]
        self.bonuses += [rocketLauncherBonus.rocketLauncherBonus((250,250),self.allSprites,self.player)]
    

    
    def print_player_info(self):
        # render text
        myfont = pygame.font.SysFont("monospace", 15)	
        ammo = myfont.render("ammo: "+ str(self.player.weapons[self.player.selected_weapon].ammo), 1, (255,255,0))
        weapon = myfont.render("current weapon: " + self.player.weapons[self.player.selected_weapon].name,1,(255,255,0))
        health = myfont.render("health: " + str(self.player.health),1,(255,255,0))
        armor = myfont.render("armor: " + str(self.player.armor),1,(255,255,0))
    
        self.screen.blit(ammo, (0, 0))
        self.screen.blit(weapon,(0,20))
        self.screen.blit(health,(0,self.HEIGHT-20))
        self.screen.blit(armor,(self.WIDTH-100,self.HEIGHT-20))
    
    
    
    
  
    def mainLoop(self):
        #game loop
        end = False
        pygame.key.set_repeat(10, 35)
        previous = pygame.time.get_ticks()
        while not end:
            key = pygame.key.get_pressed()	
            if key[pygame.K_z] or key[pygame.K_UP]:
                self.player.move_up()
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                self.player.move_down()			
            if key[pygame.K_q] or key[pygame.K_LEFT]:
                self.player.move_left()			
            if key[pygame.K_d]or key[pygame.K_RIGHT]:
                self.player.move_right()
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                previous = self.player.changing_weapon(event,previous)			
                if event.type == MOUSEMOTION:
                    self.sight.rect.center = (event.pos[0],event.pos[1])
        
            click = pygame.mouse.get_pressed()
            if click[0]:#if the left button of the mouse is pressed
                self.player.fire(pygame.mouse.get_pos(),self.allSprites)	
        
            #update objects
            #allSprites.update()
            self.map1.update()
            for box in self.dialogBoxes:
                box.update()
            self.player.update()
        
            #moving the map if necessary
            right_dist = self.WIDTH /2 + self.WIDTH/20
            if self.player.rect.right >= right_dist:
                diff = self.player.rect.right - right_dist
                self.player.rect.right = right_dist
                self.map1.scroll_width(-diff)
            left_dist = self.WIDTH/2 - self.WIDTH/20
            if self.player.rect.left <= left_dist:
                diff = left_dist - self.player.rect.left
                self.player.rect.left = left_dist
                self.map1.scroll_width(diff)
        
            top_dist = self.HEIGHT/2 - self.HEIGHT/20
            if self.player.rect.top <= top_dist:
                diff = top_dist - self.player.rect.top
                self.player.rect.top = top_dist
                self.map1.scroll_height(diff)
        
            bottom_dist = self.HEIGHT/2 + self.HEIGHT/20
            if self.player.rect.bottom >= bottom_dist:
                diff = bottom_dist - self.player.rect.bottom
                self.player.rect.bottom = bottom_dist
                self.map1.scroll_height(diff)		
        
            #print images
            self.map1.draw(self.screen)
            #screen.blit(background,(0,0))
            #allSprites.draw(screen)
            self.print_player_info()
            for building in self.buildings:
                building.draw()	
            self.player.draw()
            for box in self.dialogBoxes:
                box.draw()
            self.sight_group.draw(self.screen)
        
        
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        
    def enter(self,building,player):
        self.map1=building.inside
        self.obstacles = building.obstacles
        self.allSprites = building.allSprites
        self.buildings.clear()
        
        
        
        
        
if __name__=="__main__":
    game = Game()
    game.mainLoop()
