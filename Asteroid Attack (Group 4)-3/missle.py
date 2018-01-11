# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
#from main_game import *
import math
import sound
import datetime

#from decimal import *

class Laser:
    
    #Speed Constants (pixels/second)
    Acceleration = 0
    DecelerationRate = 0
    MaxSpeed = 30
    speed = 1
    
    SpriteScale = .5
    SpriteFile = './assets/sprites/missile.png'
    
    def __init__(self, x1arg, y1arg, x2arg, y2arg, xAngle):
        # Flight Boundary 
        self.x1=x1arg
        self.y1=y1arg
        self.x2=x2arg
        self.y2=y2arg
        
        # Properties  
        self.XVelocity = float(0)
        self.YVelocity = float(0)
        self.max_distance = 50
        self.distance=0
        
        self.lazer_delete = False
        
        if xAngle < 90:
            self.Angle = xAngle + 90
        elif xAngle < 270:
            self.Angle = xAngle - 90
        else:
            self.Angle = xAngle - 270
        self.Angle = xAngle
         
        self.Sprite = None
        
        self.scale_x = math.cos(xAngle)
        self.scale_y = math.sin(xAngle)
        self.XVelocity = self.speed * self.scale_x
        self.YVelocity = self.speed * self.scale_y 
        
        #print('Missle', self.Angle, self.scale_x, self.scale_y, self.XVelocity, self.YVelocity)
    
    def Move(self):
        moveShip = True
        #xpos = float(0)
        #ypos = float(0)
        # Calculate Velocity
        #if abs(self.XVelocity) > 0:
            #moveShip = True
            #xpos = (self.XVelocity)
        
        #if abs(self.YVelocity) > 0:
            #moveShip = True
            #ypos = (self.YVelocity)
        
        #self.XVelocity = self.speed * self.scale_x
        #self.YVelocity = self.speed * self.scale_y 
        
        xpos = self.Sprite.position[0] + self.XVelocity
        ypos = self.Sprite.position[1] + self.YVelocity
        
        self.distance += self.speed
        
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
            #print (xpos, ypos)
            self.Sprite.run_action(Action.move_to(xpos, ypos, 0))
        #print(self.distance, self.max_distance) 
        if self.distance >= self.max_distance:
            #print('delete')
            self.Sprite.remove_from_parent()
            self.lazer_delete == False
    
    def UpdateTrajectory(self, increase, angle):
        # calculating increase in speed
        #increase = self.Sprite.scene.dt * self.Acceleration
        
        #trig functions to calc x and y 
        oppangle = abs(math.sin(angle) * increase)
        adjangle = abs(math.cos(angle) * increase)
        
        #self.XVelocity += xmv
        if self.Angle == 0:
            self.YVelocity += increase
        elif self.Angle == 90:
            self.XVelocity -= increase
        elif self.Angle == 180:
            self.YVelocity -= increase
        elif self.Angle == 270:
            self.XVelocity += increase
        elif self.Angle == 360:
            self.YVelocity -= increase
        elif self.Angle >0 and self.Angle < 45:
            self.XVelocity -= adjangle
            self.YVelocity += oppangle
        elif self.Angle >= 45 and self.Angle < 90:
            self.XVelocity -= oppangle
            self.YVelocity += adjangle
        elif self.Angle > 90 and self.Angle < 135:
            self.XVelocity -= oppangle
            self.YVelocity -= adjangle
        elif self.Angle >= 135 and self.Angle < 180:
            self.XVelocity -= adjangle
            self.YVelocity -= oppangle
        elif self.Angle > 180 and self.Angle < 225:
            self.XVelocity += adjangle
            self.YVelocity -= oppangle
        elif self.Angle >= 225 and self.Angle < 270:
            self.XVelocity += oppangle
            self.YVelocity -= adjangle
        elif self.Angle > 270 and self.Angle < 315:
            self.XVelocity += oppangle
            self.YVelocity += adjangle
        elif self.Angle >= 315 and self.Angle < 360:
            self.XVelocity += adjangle
            self.YVelocity += oppangle
        
    def Draw(self, parent, x , y):
        self.Sprite = SpriteNode(self.SpriteFile,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale  = self.SpriteScale)

