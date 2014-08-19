import character
import pygame
import gun
import shotgun
import machineGun
import tools


class Player(character.Character):


    def __init__(self,position,screen,game):
        character.Character.__init__(self,"images/player.jpg","images/dead_player.jpg",position,screen,game)

        self.proximity_circle.image = pygame.image.load("images/proximity_circle.png").convert()
        self.proximity_circle.rect = self.proximity_circle.image.get_rect()
        self.previous = pygame.time.get_ticks()
        #weapon initialisation
        self.weapons += [gun.Gun(1000)]
        self.weapons += [shotgun.Shotgun(10)]
        self.weapons += [machineGun.MachineGun(500)]
        self.speed = 10



    def update(self):
        self.isNear = False
        character.Character.update(self)
        self.proximity_circle.rect.center = self.rect.center
        self.isNear = pygame.sprite.spritecollide(self.proximity_circle,self.game.buildings,False,pygame.sprite.collide_circle)
        if (self.isNear):
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_SPACE]):
                self.game.enter(self.isNear[0],self)
                
        key = pygame.key.get_pressed()	
        if key[pygame.K_z] or key[pygame.K_UP]:
            self.move_up()
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.move_down()			
        if key[pygame.K_q] or key[pygame.K_LEFT]:
            self.move_left()			
        if key[pygame.K_d]or key[pygame.K_RIGHT]:
            self.move_right()
        self.previous = self.change_weapon(key)        

    def draw(self):
        self.screen.blit(self.image,self.rect)
        for elm in self.isNear:
            if pygame.sprite.collide_circle(self,elm.door):
                self.printOpen()    


    def printOpen(self):
        openDoor = tools.myFont.render("press space to open",1, (255,255,0) )
        self.screen.blit(openDoor,(self.rect.x -20,self.rect.y+self.rect.height+5))
        
        
    def die(self):
        character.Character.die(self)
        self.game.game_over()
        
    def action(self):
        pass

