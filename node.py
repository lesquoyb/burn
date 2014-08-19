""" this class represents a node of the map, it's used by the pathfinding methods. 
 This class and all the pathfinding methods are inspired and adapted from John Eriksson's A*
 algorithm implementation that can be found on the web site: www.arainyday.se . """

class Node():
    
    
    def __init__(self,location,cost,index,parent=None):
        self.location = location
        self.cost = cost
        self.index = index
        self.parent = parent
        self.score = 0
        
    def __eq__(self,n):
        return n.index == self.index
            
        