import weapon
import rocket
import pygame

class RocketLauncher(weapon.Weapon):
    
    
        name = "rocket launcher"
        damage = 300
        delay = 5000
        scope = 50
        
        def fire(self,angle,sprites,obstacles,shooter):
                time = pygame.time.get_ticks()
                difference =  time - self.prev_time
                if self.ammo > 0 and (difference - self.delay > 0)  :
                        self.prev_time= time
                        bullet1 = rocket.Rocket(angle,sprites,obstacles,shooter,self.scope,self.damage)
                        self.ammo -= 1                