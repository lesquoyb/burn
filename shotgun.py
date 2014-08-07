import weapon
import pygame
import bullet

class Shotgun(weapon.Weapon):
    

    name = "shotgun"
    damage = 30
    delay = 1000
    scope = 15
    
    def fire(self,angle,sprites,obstacles,shooter):
        time = pygame.time.get_ticks()
        difference =  time - self.prev_time
        if self.ammo > 0 and (difference - self.delay > 0)  :
            self.prev_time= time
            bullet1 = bullet.Bullet(angle-0.25,sprites,obstacles,shooter,self.scope,self.damage)            
            bullet1 = bullet.Bullet(angle-0.3,sprites,obstacles,shooter,self.scope,self.damage)
            bullet1 = bullet.Bullet(angle,sprites,obstacles,shooter,self.scope,self.damage)
            bullet1 = bullet.Bullet(angle+0.3,sprites,obstacles,shooter,self.scope,self.damage)
            bullet1 = bullet.Bullet(angle+0.25,sprites,obstacles,shooter,self.scope,self.damage)
            self.ammo -= 1            