import character
import pygame
import aStar
import node
import tools

class Enemy(character.Character):
    
    field_of_view = 10000
    field_of_view_circle = pygame.sprite.Sprite()   
    previous_pathfinding = pygame.time.get_ticks()
    movements = []
    remaining_moves = [] # used to stack the remaining moves for the current movement in self.movements
            
    def __init__(self,image,dead,position,screen,game):
        character.Character.__init__(self,image,dead,position,screen,game)
        self.astar = aStar.AStar(self.game.map1)
        self.movements_to_cross_node = [self.speed]*(tools.NODE_STEP//self.speed)
        if (tools.NODE_STEP % self.speed ) != 0:
            self.movements_to_cross_node += [tools.NODE_STEP % self.speed ]
        self.movements = self.remaining_moves[:]
        
    def move_up(self):
        self.movements += ['up']
        
    def move_down(self):
        self.movements += ['down']
        
    def move_right(self):
        self.movements += ['right']
        
    def move_left(self):
        self.movements += ['left']
    
    def update(self):
        self.field_of_view_circle.rect = pygame.Rect(self.rect)
        self.field_of_view_circle.rect.width = self.field_of_view
        self.field_of_view_circle.rect.height = self.field_of_view
        self.field_of_view_circle.rect.center = self.rect.center
        
        now = pygame.time.get_ticks()
        if (now - self.previous_pathfinding) > tools.pathfinding_delay and self.player_found() :
            self.movements = []
            path = self.astar.findPath((self.rect.x,self.rect.y),(self.game.player.rect.x,self.game.player.rect.y))
            self.move_to_path_node(path)
            self.previous_pathfinding = now
        if len(self.movements)>0:
            if self.movements[0] == 'right' or self.movements[0] == 'left':
                self.move_x = self.movements_to_cross_node[0] if self.movements[0] == 'right' else -self.movements_to_cross_node[0]
            else:
                self.move_y = self.movements_to_cross_node[0] if self.movements[0] == 'down' else -self.movements_to_cross_node[0]
            if len(self.remaining_moves)>1:
                self.remaining_moves.pop(0)
            else:
                self.remaining_moves = self.movements_to_cross_node[:]
                self.movements.pop(0)
                
        character.Character.update(self)
 
        
    def player_found(self):
        return pygame.sprite.collide_circle(self.field_of_view_circle,self.game.player)
    
    
    def move_to_path_node(self,path):
        """ needs to be improved in order to be able to reach multiple path nodes within the same update 
        (exemple first step is 15px away and the speed is 20, you should be able to reach the first node 
        and begin to move to the second one in only one update) """
        if (path is not None):
            x = self.rect.x
            y = self.rect.y
            if (x == path['nodes'][0].location[0] and y == path['nodes'][0].location[1]):
                path['nodes'].pop(0)#as the first step is reach we can pop it out from the path            
            for node in path['nodes']:
                if x == node.location[0]:
                    if y < node.location[1]:
                        self.move_down()
                    else:
                        self.move_up()
                elif y == node.location[1]:
                    if x < node.location[0]:
                        self.move_right()
                    else:
                        self.move_left()
                else:
                    # the enemy and the first node aren't on the same axis at all we move in order to reach the closer one
                    dx = x - node.location[0]
                    dy = y - node.location[1]
                    if abs(dx) < abs(dy):
                        if dx < 0 :
                            self.move_right()
                        else:
                            self.move_left()
                    else:
                        if dy < 0:
                            self.move_down()
                        else:
                            self.move_up()
