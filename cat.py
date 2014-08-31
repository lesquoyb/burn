import enemy

class Cat(enemy.Enemy):
    
    
    def __init__(self,position,screen,game):
        enemy.Enemy.__init__(self,"images/enemy.jpg","images/dead_cat.jpg",position,screen,game)
        
        
    