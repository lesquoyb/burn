""" implementation of the A* algorithm, inspired by John Eriksson's A*
 algorithm implementation that can be found on the web site: www.arainyday.se .  """

class AStar():
    
      def __init__(self,maphandler):
            self.mh = maphandler
                    
      def _getBestOpenNode(self):
            bestNode = None        
            for n in self.on:
                  if not bestNode:
                        bestNode = n
                  else:
                        if n.score<=bestNode.score:
                              bestNode = n
            return bestNode
  
      def _tracePath(self,n):
            nodes = [];
            totalCost = n.cost;
            p = n.parent;
            nodes.insert(0,n);       
            while 1:
                  if p.parent is None: 
                        break
                  nodes.insert(0,p)
                  p=p.parent
            
            return {'nodes': nodes,'cost': totalCost}
  
      def _handleNode(self,node,end):        
            i = self.o.index(node.index)
            self.on.pop(i)
            self.o.pop(i)
            self.c.append(node.index)
            end_index = self.mh.get_node(end)
            
            nodes = self.mh.getAdjacentNodes(node,end)
                       
            for n in nodes:
                  if n == end_index:
                      # reached the destination
                        return n
                  elif n.index in self.c:
                      # already in close, skip this
                        continue
                  elif n.index in self.o:
                      # already in open, check if better score
                        i = self.o.index(n.index)
                        on = self.on[i];
                        if n.cost<on.cost:
                              self.on.pop(i);
                              self.o.pop(i);
                              self.on.append(n);
                              self.o.append(n.index);
                  else:
                      # new node, append to open list
                        self.on.append(n);                
                        self.o.append(n.index);
            
            return None
  
      def findPath(self,fromlocation, tolocation):
            self.o = []
            self.on = []
            self.c = []
            end = tolocation
            fnode = self.mh.get_node(fromlocation)
            self.on.append(fnode)
            self.o.append(fnode.index)
            nextNode = fnode     
            while nextNode is not None: 
                  finish = self._handleNode(nextNode,end)
                  if finish:                
                        return self._tracePath(finish)
                  nextNode=self._getBestOpenNode()  
            return None    