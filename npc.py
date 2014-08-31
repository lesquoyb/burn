import character

class Npc(character):
    
    def __init__(self,position,obstacles,screen,text):
        character.Character.__init__("images/npc.png","images/npc.png",position,obstacles,screen)
        

    def speak(self):
        pass