# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
#from main_game import *
import math
import sound
import datetime
from main_game import *

#from decimal import *

class Asteroid:
    
    SpriteScale = 0.5
    SpriteFile = './assets/sprites/asteroid.png'
    
    def __init__(self, x1arg, y1arg, x2arg, y2arg, xAngle):
        # Flight Boundary 
        self.x1=x1arg
        self.y1=y1arg
        self.x2=x2arg
        self.y2=y2arg
        
        # Properties 
        self.speed = 100
        self.XVelocity = float(0)
        self.YVelocity = float(0)
        
        self.distance=0
        
        self.delete = False
        
        self.Angle = xAngle + 90
        if self.Angle > 360:
            self.Angle -= 360
            
        self.Sprite = None
        
        self.scale_x = math.cos(math.radians(self.Angle))
        self.scale_y = math.sin(math.radians(self.Angle)) 
        self.XVelocity = self.speed * self.scale_x 
        self.YVelocity = self.speed * self.scale_y 
        
        #print('Missle', self.Angle, self.scale_x, self.scale_y, self.XVelocity, self.YVelocity)
    
    def move(self):
        
        if self.Sprite.scene == None:
            moveShip = False
        else:
            moveShip = True
            xpos = self.Sprite.position[0] + self.XVelocity * self.Sprite.scene.dt
            ypos = self.Sprite.position[1] + self.YVelocity * self.Sprite.scene.dt
            self.distance += self.speed * self.Sprite.scene.dt
        
        #Should the ship move
        if self.Sprite.position[0] < self.x1:
            #Ship has moved off screen
            xpos = self.x2
            ypos = self.Sprite.position[1]
            self.Sprite.remove_all_actions()
            self.Sprite.run_action(Action.move_to(xpos, ypos, 0))
            moveShip = False
            
        elif self.Sprite.position[0] > self.x2:
            xpos = self.x1
            ypos = self.Sprite.position[1]
            self.Sprite.remove_all_actions()
            self.Sprite.run_action(Action.move_to(xpos, ypos, 0))
            moveShip = False
        
        if self.Sprite.position[1] < self.y1:
            ypos = self.y2
            xpos = self.Sprite.position[0]
            self.Sprite.remove_all_actions()
            self.Sprite.run_action(Action.move_to(xpos, ypos, 0))
            moveShip = False
            
        elif self.Sprite.position[1] > self.y2:
            ypos = self.y1
            xpos = self.Sprite.position[0]
            self.Sprite.remove_all_actions()
            self.Sprite.run_action(Action.move_to(xpos, ypos, 0))
            moveShip = False
        
        if moveShip == True:
            self.Sprite.remove_all_actions()
            self.Sprite.run_action(Action.move_to(xpos, ypos, 0))
        
    def draw(self, parent, x , y):
        self.Sprite = SpriteNode(self.SpriteFile,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale  = self.SpriteScale)
        print(self.Sprite == None)
       
    
