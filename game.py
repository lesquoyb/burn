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
    explosions = []
    dialogBoxes = []
    bonuses = []
    messages = []
    
    def __init__(self):
        # init pygame and the game window
        pygame.init()	
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT), DOUBLEBUF|HWSURFACE)        
        self.background = pygame.image.load("images/map.png").convert()
        self.clock = pygame.time.Clock()
        self.allSprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        pygame.display.set_caption("Best game ever")
        self.sight = pygame.sprite.Sprite()
        self.sight_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
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
           
        box = dialogBox.DialogBox("Salut et bienvenue dans le monde de burn, ici tu découvriras plein de choses merveilleuses, comme des chats et des chaussettes par exemple.Mais aussi des murs et des maisons! Comme je dois tester cette boite de dialogue il va falloir que j'écrive quelque chose de long, c'est pourquoi je propose d'en profiter pour faire un rapide tutoriel: Commencons par les déplacements: rien de plus simple tu peux utiliser les flêches ou les touches'z','q','s' et 'd' pour bouger(oui c'est bien toi la chaussure au milieu de l'écran). Ensuite je suppose que tu as remarqué cette jolie cible sur l'écran? Il s'agit de ton viseur, tu peux le déplacer grace à ta souris.Ce qui me mène au point suivant: BASTON !!!! Tu disposes de plusieurs armes (3 au moment ou j'ecris ces lignes) utilise les touches 'a' et 'e' pournaviguer entres elles. Tu vois ce truc répugnant sur ta gauche? Oui oui le chat, il est temps pour lui de mourir! vise le et utilise le clickgauche de la souris pour tirer. Voila je pense que c'est assez pour aujourd'hui je te laisse te débrouiller :)."
                                        ,self.screen,self)
        self.dialogBoxes += [box]
        self.map1 = map.Map(self.background,self.background.get_rect().center,self.obstacles,self.allSprites,self.bonuses,self.explosions,self.buildings)        
        self.player = player.Player((self.WIDTH/2,50),self.screen,self)
        self.obstacles.add(self.player)
        #positionning bonuses
        self.bonuses += [healthBonus.HealthBonus((150,150),self.allSprites,self.player)]
        self.bonuses += [rocketLauncherBonus.rocketLauncherBonus((250,250),self.allSprites,self.player,self.explosions,self.screen)]
    

    
    def print_player_info(self):
        # render text
        myfont = pygame.font.SysFont("monospace", 15)	
        ammo = myfont.render("ammo: "+ str(self.player.weapons[self.player.selected_weapon].ammo), 1, (255,255,0))
        weapon = myfont.render("current weapon: " + self.player.weapons[self.player.selected_weapon].name,1,(255,255,0))
        health = myfont.render("health: " + str(self.player.health),1,(255,255,0))
        armor = myfont.render("armor: " + str(self.player.armor),1,(255,255,0))
        fps = myfont.render(str(self.clock.get_fps()),1,(255,255,255))
        
        self.screen.blit(fps,(self.WIDTH-100,30))
        self.screen.blit(ammo, (0, 0))
        self.screen.blit(weapon,(0,20))
        self.screen.blit(health,(0,self.HEIGHT-20))
        self.screen.blit(armor,(self.WIDTH-100,self.HEIGHT-20))
    
    
    
    
  
    def mainLoop(self):
        #game loop
        end = False
        pygame.key.set_repeat(10, 35)
        while not end:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                if event.type == MOUSEMOTION:
                    self.sight.rect.center = (event.pos[0],event.pos[1])
        
            click = pygame.mouse.get_pressed()
            if click[0]:#if the left button of the mouse is pressed
                self.player.fire(pygame.mouse.get_pos(),self.allSprites)	
        
            self.update() 
        
            self.draw()
        
        pygame.quit()
        
    def enter(self,building,player):
        self.map1=building.inside
        self.obstacles = building.obstacles
        self.allSprites = building.allSprites
        self.buildings.clear()
        
        
        
    def update(self):
        #update objects
        self.map1.update()
        for box in self.dialogBoxes:
            box.update()
        self.player.update()        
        


    def draw(self):
        #print images
        self.map1.draw(self.screen,self.player)
        self.print_player_info()
        for box in self.dialogBoxes:
            box.draw() 
        self.player.draw()            
        self.sight_group.draw(self.screen)
        for message in self.messages:
            self.screen.blit(message,self.screen.get_rect().center)
        pygame.display.update()
        self.clock.tick(100)  
        
    def game_over(self):
        myfont = pygame.font.SysFont("monospace", 50,1)	
        message = myfont.render("YOU LOSE",1,(255,0,0))        
        self.messages+=[message]
        
        
        
if __name__=="__main__":
    game = Game()
    game.mainLoop()
