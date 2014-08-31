import pygame
import player
import node
import tools

class Map(pygame.sprite.Sprite):
    

    rooms = []
    
    
    def __init__(self,background,starting_point,obstacles,sprites,bonuses,explosions,buildings):
        pygame.sprite.Sprite.__init__(self)
        self.image =background
        self.obstacles = obstacles
        self.sprites = sprites
        self.rect = self.image.get_rect()
        (self.rect.x,self.rect.y ) = (-starting_point[0],-starting_point[1])
        self.bonuses = bonuses
        self.explosions = explosions
        self.buildings = buildings
        
        
        
    def update(self,*args):
        for obstacle in self.obstacles:
            obstacle.update()
        for sprite in self.sprites:
            sprite.update()
        for explosion in self.explosions:
            explosion.update()
            
            
    def draw(self,screen,player):
        self.move_camera(screen,player)
        screen.blit(self.image,self.rect)
        self.sprites.draw(screen)
        for building in self.buildings:
            building.draw()	
        for explosion in self.explosions:
            explosion.draw()    
        #self.print_costs(screen)
        
        
    def move_camera(self,screen,player):
        #moving the map if necessary
        rect = screen.get_rect()
        WIDTH = rect.width
        HEIGHT = rect.height
        
        right_dist = WIDTH /2 + WIDTH/20
        if player.rect.right >= right_dist:
            if self.rect.right > WIDTH:
                diff = player.rect.right - right_dist
                player.rect.right = right_dist
                self.scroll_width(-diff)
            else:
                self.rect.right = WIDTH
            
        left_dist = WIDTH/2 - WIDTH/20
        if player.rect.left <= left_dist:
            if self.rect.left < 0:
                diff = left_dist - player.rect.left
                player.rect.left = left_dist
                self.scroll_width(diff)
            else:
                self.rect.left = 0
    
        top_dist = HEIGHT/2 - HEIGHT/20
        if player.rect.top <= top_dist:
            if self.rect.top < 0:
                diff = top_dist - player.rect.top
                player.rect.top = top_dist
                self.scroll_height(diff)
            else:
                self.rect.top = 0
    
        bottom_dist = HEIGHT/2 + HEIGHT/20
        if player.rect.bottom >= bottom_dist:
            if self.rect.bottom > HEIGHT:
                diff = bottom_dist - player.rect.bottom
                player.rect.bottom = bottom_dist
                self.scroll_height(diff)  
            else:
                self.rect.bottom = HEIGHT
        
    def scroll_width(self,distance):
        for obstacle in self.obstacles:
            if not isinstance(obstacle,player.Player):
                obstacle.rect.x += distance
        for sprite in self.sprites:
            if sprite not in self.obstacles:
                sprite.rect.x += distance
        for explosion in self.explosions:
            explosion.rect.x += distance
        self.rect.x += distance
        
    def scroll_height(self,distance):
        for obstacle in self.obstacles:
            if not isinstance(obstacle,player.Player):
                obstacle.rect.y += distance
        for sprite in self.sprites:
            if sprite not in self.obstacles:
                sprite.rect.y += distance 
        for explosion in self.explosions:
            explosion.rect.y += distance  
        self.rect.y += distance
        
        
    #return the node at the location or None
    def get_node(self,location):
        #index =   (location[1]//tools.NODE_STEP-1)*(self.rect.width//tools.NODE_STEP -1)+ (location[0]//tools.NODE_STEP)-1 +( -(self.rect.y)//tools.NODE_STEP-1* (self.rect.width//tools.NODE_STEP-1)+ (-(self.rect.x)//tools.NODE_STEP-10))-1
        step = tools.NODE_STEP
        index = (-(self.rect.y)//step-1) * (self.rect.width//step-1)\
                                    + (-(self.rect.x)//step-1) + (location[1]//step-1)*(self.rect.width//step-1)+(location[0]//step-1) - 1
        return node.Node(location,self.costs[index],index)
        
    def getAdjacentNodes(self, curnode, dest):
        result = []
        cl = curnode.location
        dl = dest
        n = self._handleNode(cl[0]+tools.NODE_STEP,cl[1],curnode,dl[0],dl[1])
        if n: 
            result.append(n)
        n = self._handleNode(cl[0]-tools.NODE_STEP,cl[1],curnode,dl[0],dl[1])
        if n: 
            result.append(n)
        n = self._handleNode(cl[0],cl[1]+tools.NODE_STEP,curnode,dl[0],dl[1])
        if n:
            result.append(n)
        n = self._handleNode(cl[0],cl[1]-tools.NODE_STEP,curnode,dl[0],dl[1])
        if n: 
            result.append(n)
        return result
    
    def _handleNode(self,x,y,fromnode,destx,desty):
        n = self.get_node((x,y))
        if n is not None:
            n.cost += fromnode.cost                                   
            n.score = n.cost#+emCost
            n.parent=fromnode
            return n
        return None    
            
    def initialize_cost(self):
        """ initialize the cost of each node of the map, costs less resources than calculate each time """
        step = tools.NODE_STEP
        self.costs = [tools.NEUTRAL_COST] * ((self.rect.width//step)*(self.rect.height//step))   
        for item in self.obstacles:
            for i in range(item.rect.x,item.rect.x+item.rect.width,step):
                for j in range(item.rect.y,item.rect.y+item.rect.height,step):
                    #debugging
                    screen_position = (-(self.rect.y)//step-1) * (self.rect.width//step-1)\
                                    + (-(self.rect.x)//step-1)
                    item_position = (j//step-1)*(self.rect.width//step-1)+(i//step-1)
                    self.costs[ item_position + screen_position -1 ] = tools.OBSTACLE_COST  
        for item in self.bonuses:
            for i in range(item.rect.x,item.rect.x+item.rect.width,step):
                for j in range(item.rect.y,item.rect.y+item.rect.height,step):
                    #debugging
                    screen_position = (-(self.rect.y)//step-1) * (self.rect.width//step-1)\
                                    + (-(self.rect.x)//step-1)
                    item_position = (j//step-1)*(self.rect.width//step-1)+(i//step-1)
                    self.costs[ item_position + screen_position -1]=tools.BONUS_COST              
        
    def print_costs(self,screen):
        """ debugging purpose, framerate drop """
        step = tools.NODE_STEP  
        rect = screen.get_rect()
        for i in range(0,rect.width,step):
            for j in range(0,rect.height,step):
                index = ((j+abs(rect.y))//step)*(self.rect.width//step)\
                    + ((i+abs(rect.x))//step) 
                #index = (j//step-1)*(rect.width//step-1)+(i//step-1)\
                #+ abs((self.rect.y)//step-1) * (self.rect.width//step-1)\
                #+ abs((self.rect.x)//step-1)
                text = tools.myFont.render(str(self.costs[index-1]),1,(0,0,0))
                screen.blit(text,(i,j)) 

        
                
        