# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
import math
import sound
import datetime
from laser import *
from asteroid import *
import ConfigParser, os


class SpaceShip:
    def __init__(self, x1arg, y1arg, x2arg, y2arg):
        # Properties  
        self.x_velocity = float(0)
        self.y_velocity = float(0)
        self.angle = float(0)
        self.angle_shift = float(0)
        self.destroyed = False
        
        # Flight Boundary
        self.x1=x1arg
        self.y1=y1arg
        self.x2=x2arg
        self.y2=y2arg
        
        #Direction of movement / Actions
        self.left = False
        self.right = False
        self.shoot_button= False
        self.thrust_button = False
        
        #Speed variables (pixels/second)
        self.acceleration = 3
        self.deceleration_rate = 0.25
        self.max_speed = 25
        self.sensitivity = math.radians(1.75)
        
        self.lazers = []
        self.sprite = None
        self.spriteScale = 0.075
        self.spriteFile = './assets/sprites/SHIP3a.png'
        
    
    def Thrust(self):
        #Logic to control ship thrust and speed
        increase = self.sprite.scene.dt * self.acceleration
        oppangle = 0
        adjangle = 0
        
        if (self.thrust_button== True):
                
            #increase = self.sprite.scene.dt * float(self.acceleration)
            #Turning Physics
            realangle = self.angle + 90
            if realangle > 360:
                realangle -= 360
            oppangle = math.sin(math.radians(realangle)) 
            adjangle = math.cos(math.radians(realangle))
            #wprint (realangle, oppangle, adjangle, self.x_velocity, self.y_velocity)
            #* increase) * self.sprite.scene.dt.x_velocity += xmv
            
            self.x_velocity += increase * adjangle
            self.y_velocity += increase * oppangle 
                
        else:
            # Deceleration Logic
            if self.x_velocity != 0:
                self.x_velocity -= ((self.x_velocity * self.deceleration_rate) * self.sprite.scene.dt)
                #if self.x_velocity > 0:
                #    self.x_velocity -= ((self.x_velocity * self.deceleration_rate) * self.sprite.scene.dt)
                #else:
                #    self.x_velocity -= ((self.x_velocity * self.deceleration_rate) * self.sprite.scene.dt)
            
            if self.y_velocity != 0:
                self.y_velocity -= ((self.y_velocity * self.deceleration_rate) * self.sprite.scene.dt)
                #if self.y_velocity > 0:
                #    self.y_velocity -= ((self.y_velocity * self.deceleration_rate) * self.sprite.scene.dt)
                #else:
                #    self.y_velocity -= ((self.y_velocity * self.deceleration_rate) * self.sprite.scene.dt)
            
            if abs(self.x_velocity) < 0.1:
                self.x_velocity = 0
            
            if abs(self.y_velocity) < 0.1:
                self.y_velocity = 0
            
        #Check if ship is exceeding max speed in +/- x axis
        if (self.x_velocity > self.max_speed):
            self.x_velocity = self.max_speed
        elif (self.x_velocity < (self.max_speed * -1)):
            self.x_velocity = self.max_speed * -1
        
        #Check if ship is exceeding max speed in +/- y axis
        if (self.y_velocity > self.max_speed):
            self.y_velocity = self.max_speed
        elif (self.y_velocity < (self.max_speed * -1)):
            self.y_velocity = self.max_speed * -1
        
        #Thrustw/Speed display -- comment out when not debugging
        #print (self.ThrustButton, self.x_velocity, self.y_velocity, self.angle, self.angle_shift, str(increase), oppangle, adjangle, self.sprite.position.x, self.sprite.position.y)
        
    def Rotate(self):
        should_rotate=False
        if self.left == True:
           #Rotate ship to the left
           newangle = math.degrees((self.sprite.rotation + self.sensitivity) * 1)
           self.angle_shift = newangle - self.angle
           self.angle = newangle
           should_rotate=True
        elif self.right == True:
           #Rotate ship to the right
           #self.angle = math.degrees((self.sprite.rotation - self.sensitivity) * 1)
           newangle = math.degrees((self.sprite.rotation - self.sensitivity) * 1)
           self.angle_shift = self.angle - newangle
           self.angle = newangle
           should_rotate=True
        
        # Logic to convert angles to 0 to +360 degrees
        if should_rotate == True:
            #print(datetime.datetime.now() ,'True', len(self.sprite.scene.touches), =
            if self.angle < 0:
                #Convert to a positive 
                self.angle += 360
            elif self.angle > 360:
                #Made more than one full revolution, adjust to less < 360
                self.angle -= 360
            #Angle has been adjusted, so rotate the ship
            self.sprite.rotation = math.radians(self.angle)
        else:
            pass
            #print('False', len(self.sprite.scene.touches))
        
    def Move(self):
        move_sprite = False
        xpos = float(0)
        ypos = float(0)
        # Calculate Velocity
        if abs(self.x_velocity) > 0:
            move_sprite = True
            xpos = (self.x_velocity)
        
        if abs(self.y_velocity) > 0:
            move_sprite = True
            ypos = (self.y_velocity)
        
        #Should the ship move
        if self.sprite.position[0] < self.x1:
            #Ship has moved off screen
            xpos = self.x2
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
        elif self.sprite.position[0] > self.x2:
            xpos = self.x1
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
        
        if self.sprite.position[1] < self.y1:
            ypos = self.y2
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
        elif self.sprite.position[1] > self.y2:
            ypos = self.y1
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
            
        if move_sprite == True:
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_by(xpos, ypos, 0))
        
        for item in self.lazers:
            #self.lazer[len(self.lazer)-1]Move()
            item.move()
            if item.delete == True:
                #item.remove_from_parent()
                self.lazers.remove(item)
                print ('ship lazers', len(self.lazers))
                self.sprite.scene.score
        
    def Draw(self, parent, x , y):
        self.sprite = SpriteNode(self.spriteFile,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale  = self.spriteScale)
    
    def Shoot(self):
        if self.destroyed == True:
            return None
            
        # sound that is played when user hits the shoot button
        sound.play_effect('./assets/sounds/laser1.wav')
        
        # when the user hits the fire button
        lazer_start_position = self.sprite.position
        
        lazer_end_position = Vector2()
        #print(self.angle)
        lazer_end_position.y = math.sin(self.angle - math.pi / 2) * 500
        lazer_end_position.x = math.cos(self.angle - - math.pi / 2) * 500
        
        
        
        #self.lazer.append(SpriteNode('./assets/sprites/missile.png',
        #                     position = lazer_start_position,
        #                     scale = 0.25,
        #                     parent = self.sprite.scene))
        
        # make missile move forward
        #lazer = Laser(self.x1, self.y1,self.x2,self.y2)
        self.lazers.append(Laser(self.x1, self.y1,self.x2,self.y2, self.angle))
        #lazer.Draw(self.sprite, self.sprite.position[0], self.sprite.position[1])
        #lazerMoveAction = Action.move_by(lazer_end_position.x, 
        #                                 lazer_end_position.y, 
        #                                 5.0)
        self.lazers[len(self.lazers)-1].draw(self.sprite.scene, self.sprite.position[0], self.sprite.position[1])
        self.lazers[len(self.lazers)-1].sprite.rotation = self.sprite.rotation
        self.lazers[len(self.lazers)-1].angle = self.angle
        
        #self.lazer[len(self.lazer)-1].UpdateTrajectory(10, self.angle)
        #self.lazer[len(self.lazer)-1].y_velocity = self.y_velocity
        #self.lazer[len(self.lazer)-1].sprite.run_action(lazerMoveAction)
    
