import weapon
import bullet
import pygame

class MachineGun(weapon.Weapon):
    
    
    name = "machine gun"
    damage = 5
    delay = 50
    scope = 30
    
    def fire(self,angle,sprites,obstacles,shooter):

        time = pygame.time.get_ticks()
        difference =  time - self.prev_time
        if self.ammo > 0 and (difference - self.delay > 0)  :
            self.prev_time= time
            bullet1 = bullet.Bullet(angle,sprites,obstacles,shooter,self.scope,self.damage)
            self.ammo -= 1        
    
    
    def __init__(self,ammo):
        weapon.Weapon.__init__(self,ammo)
        