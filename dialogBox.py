import pygame

class DialogBox(pygame.sprite.Sprite):
    
    pos = 0
    decomp = []
    toRender= ""
    
    def __init__(self,text,screen):
        self.image = pygame.image.load("images/dialogBox.png").convert()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.decomp = text.split(" ")
        self.myFont = pygame.font.SysFont("monospace",15)        
        self.nextScreen()
    
        
    def update(self):
        self.rect.bottom = self.screen.get_rect().bottom
        self.rect.centerx = self.screen.get_rect().centerx
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.nextScreen()        
        
    def draw(self):
        self.screen.blit(self.image,self.rect)
        toRender = self.toRender.split("\n")
        i = 0
        for line in toRender:
            renderedText = self.myFont.render(line,1,(255,255,255))
            self.screen.blit(renderedText,(self.rect.x+30,self.rect.y +20 +i*20))
            i+=1
        
    def nextScreen(self):
        if self.pos <= len (self.decomp)-1:
            self.toRender = self.decomp[self.pos]  +" "  
            temp = self.toRender
            while (self.pos <= len(self.decomp)):
                while (self.myFont.size(temp)[0]  < self.rect.width-110):
                    self.pos+=1                                    
                    if self.pos >= len(self.decomp)-1:
                        break
                    else:
                        self.toRender += self.decomp[self.pos] + " "                     
                        temp += self.decomp[self.pos+1] + " " 
                if self.pos < len(self.decomp)-1:
                    self.toRender+="\n"                    
                    temp=self.decomp[self.pos+1]
                elif self.pos == len(self.decomp)-1:
                    self.toRender += self.decomp[self.pos]
                
            
                    
        