# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
#from main_game import *
import math
import sound
import datetime
import pprint
from missle import *
#from decimal import *

class SpaceShip:
    def __init__(self, x1arg, y1arg, x2arg, y2arg):
        # Properties  
        self.XVelocity = float(0)
        self.YVelocity = float(0)
        self.Angle = float(0)
        self.AngleShift = float(0)
        
        # Flight Boundary
        self.x1=x1arg
        self.y1=y1arg
        self.x2=x2arg
        self.y2=y2arg
        
        #Direction of movement / Actions
        self.Left = False
        self.Right = False
        self.ShootButton = False
        self.ThrustButton= False
        
        #Speed Constants (pixels/second)
        self.Acceleration = 3
        self.DecelerationRate = 0.25
        self.MaxSpeed = 25
        self.Sensitivity = math.radians(1)
        
        self.lazer = []
        self.Sprite = None
        self.SpriteScale = 1
        self.SpriteFile = './assets/sprites/spaceship2.PNG'
        
    
    def Thrust(self):
        #Logic to control ship thrust and speed
        increase = self.Sprite.scene.dt * self.Acceleration
        oppangle = 0
        adjangle=0
        
        if (self.ThrustButton == True):
                
            #increase = self.Sprite.scene.dt * float(self.Acceleration)
            #Turning Physics
            
            oppangle = abs(math.sin(self.AngleShift) * increase)
            adjangle = abs(math.cos(self.AngleShift) * increase)
                
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
                
        else:
            # Deceleration Logic
            if self.XVelocity != 0:
                self.XVelocity -= ((self.XVelocity * self.DecelerationRate) * self.Sprite.scene.dt)
                #if self.XVelocity > 0:
                #    self.XVelocity -= ((self.XVelocity * self.DecelerationRate) * self.Sprite.scene.dt)
                #else:
                #    self.XVelocity -= ((self.XVelocity * self.DecelerationRate) * self.Sprite.scene.dt)
            
            if self.YVelocity != 0:
                self.YVelocity -= ((self.YVelocity * self.DecelerationRate) * self.Sprite.scene.dt)
                #if self.YVelocity > 0:
                #    self.YVelocity -= ((self.YVelocity * self.DecelerationRate) * self.Sprite.scene.dt)
                #else:
                #    self.YVelocity -= ((self.YVelocity * self.DecelerationRate) * self.Sprite.scene.dt)
            
            if abs(self.XVelocity) < 0.1:
                self.XVelocity = 0
            
            if abs(self.YVelocity) < 0.1:
                self.YVelocity = 0
            
        #Check if ship is exceeding max speed in +/- x axis
        if (self.XVelocity > self.MaxSpeed):
            self.XVelocity = self.MaxSpeed
        elif (self.XVelocity < (self.MaxSpeed * -1)):
            self.XVelocity = self.MaxSpeed * -1
        
        #Check if ship is exceeding max speed in +/- y axis
        if (self.YVelocity > self.MaxSpeed):
            self.YVelocity = self.MaxSpeed
        elif (self.YVelocity < (self.MaxSpeed * -1)):
            self.YVelocity = self.MaxSpeed * -1
        
        #Thrustw/Speed display -- comment out when not debugging
        #print (self.ThrustButton, self.XVelocity, self.YVelocity, self.Angle, self.AngleShift, str(increase), oppangle, adjangle, self.Sprite.position.x, self.Sprite.position.y)
        
    def Rotate(self):
        ShouldRotate=False
        if self.Left == True:
           #Rotate ship to the left
           newangle = math.degrees((self.Sprite.rotation + self.Sensitivity) * 1)
           self.AngleShift = newangle - self.Angle
           self.Angle = newangle
           ShouldRotate=True
        elif self.Right == True:
           #Rotate ship to the right
           #self.Angle = math.degrees((self.Sprite.rotation - self.Sensitivity) * 1)
           newangle = math.degrees((self.Sprite.rotation - self.Sensitivity) * 1)
           self.AngleShift = self.Angle - newangle
           self.Angle = newangle
           ShouldRotate=True
        
        # Logic to convert angles to 0 to +360 degrees
        if ShouldRotate == True:
            #print(datetime.datetime.now() ,'True', len(self.Sprite.scene.touches), =
            if self.Angle < 0:
                #Convert to a positive 
                self.Angle += 360
            elif self.Angle > 360:
                #Made more than one full revolution, adjust to less < 360
                self.Angle -= 360
            #Angle has been adjusted, so rotate the ship
            self.Sprite.rotation = math.radians(self.Angle)
        else:
            pass
            #print('False', len(self.Sprite.scene.touches))
        
    def Move(self):
        moveShip = False
        xpos = float(0)
        ypos = float(0)
        # Calculate Velocity
        if abs(self.XVelocity) > 0:
            moveShip = True
            xpos = (self.XVelocity)
        
        if abs(self.YVelocity) > 0:
            moveShip = True
            ypos = (self.YVelocity)
        
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
            self.Sprite.run_action(Action.move_by(xpos, ypos, 0))
        
        for item in self.lazer:
            #self.lazer[len(self.lazer)-1]Move()
            item.Move()
            if item.lazer_delete == True:
                #item.remove_from_parent()
                self.lazer.remove(lazer)
        
    def Draw(self, parent, x , y):
        self.Sprite = SpriteNode(self.SpriteFile,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale  = self.SpriteScale)
    def Shoot(self):
        # sound that is played when user hits the shoot button
        sound.play_effect('./assets/sounds/laser1.wav')
        
        # when the user hits the fire button
        lazer_start_position = self.Sprite.position
        #lazer_start_position.x = 
        #lazer_start_position.y = 400
        
        lazer_end_position = Vector2()
        #print(self.Angle)
        lazer_end_position.y = math.sin(self.Angle - math.pi / 2) * 500
        lazer_end_position.x = math.cos(self.Angle - - math.pi / 2) * 500
        
        
        
        #self.lazer.append(SpriteNode('./assets/sprites/missile.png',
        #                     position = lazer_start_position,
        #                     scale = 0.25,
        #                     parent = self.Sprite.scene))
        
        # make missile move forward
        #lazer = Laser(self.x1, self.y1,self.x2,self.y2)
        self.lazer.append(Laser(self.x1, self.y1,self.x2,self.y2, self.Angle))
        #lazer.Draw(self.Sprite, self.Sprite.position[0], self.Sprite.position[1])
        #lazerMoveAction = Action.move_by(lazer_end_position.x, 
        #                                 lazer_end_position.y, 
        #                                 5.0)
        self.lazer[len(self.lazer)-1].Draw(self.Sprite.scene, self.Sprite.position[0], self.Sprite.position[1])
        self.lazer[len(self.lazer)-1].Sprite.rotation = self.Sprite.rotation
        self.lazer[len(self.lazer)-1].Angle =self.Angle
        self.lazer[len(self.lazer)-1].UpdateTrajectory(10, self.Angle)
        #self.lazer[len(self.lazer)-1].YVelocity = self.YVelocity
        #self.lazer[len(self.lazer)-1].Sprite.run_action(lazerMoveAction)
    
