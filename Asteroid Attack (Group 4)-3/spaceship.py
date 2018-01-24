# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene controls the main space ship

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
        self.sensitivity = math.radians(2)
        
        self.lazers = []
        self.sprite = None
        self.spriteScale = 0.075

        #Ship Sprites and Textures
        self.thrust_sprite = './assets/sprites/SHIP3B.png'
        self.idle_sprite = './assets/sprites/SHIP3a.png'
        self.spriteFile = self.idle_sprite

        self.thrust_texture  = Texture(self.thrust_sprite)
        self.idle_texture = Texture(self.idle_sprite)
        
        
    
    def thrust(self):
        #Logic to control ship thrust and speed
        increase = self.sprite.scene.dt * self.acceleration
        oppangle = 0
        adjangle = 0
        
        if (self.thrust_button== True):
           
            #Turning Physics
            realangle = self.angle + 90
            if realangle > 360:
                realangle -= 360

            oppangle = math.sin(math.radians(realangle)) 
            adjangle = math.cos(math.radians(realangle))
           
            self.x_velocity += increase * adjangle
            self.y_velocity += increase * oppangle 

            #Show ship with thrusters
            if self.destroyed == False:
                #sound.play_effect('./assets/sounds/thrust2.wav')
                if self.spriteFile != self.thrust_sprite:
                    self.sprite.texture = self.thrust_texture
                    self.spriteFile = self.thrust_sprite
        else:
            # Deceleration Logic

            #Show ship without thrusters if its not the current sprite
            if self.spriteFile != self.idle_sprite and self.destroyed == False:
                self.sprite.texture = self.idle_texture
                self.spriteFile = self.idle_sprite

            if self.x_velocity != 0:
                #This allows us to slow down evenly in both directions
                self.x_velocity -= ((self.x_velocity * self.deceleration_rate) * self.sprite.scene.dt)
            
            if self.y_velocity != 0:
                #This allows us to slow down evenly in both directions
                self.y_velocity -= ((self.y_velocity * self.deceleration_rate) * self.sprite.scene.dt)

            #Forces it to stop ones it slows down (Prevents jittering)
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
               
    def rotate(self):
        should_rotate=False
        
        if self.left == True:
           #Rotate ship to the left
           newangle = math.degrees((self.sprite.rotation + self.sensitivity) * 1)
           self.angle_shift = newangle - self.angle
           self.angle = newangle
           should_rotate=True
        elif self.right == True:
           #Rotate ship to the right
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
        
    def move(self):
        # Object Move function 
        move_sprite = False
        xpos = float(0)
        ypos = float(0)
        
        # Calculate Velocity
        if abs(self.x_velocity) > 0:
            move_sprite = True
            xpos = self.x_velocity
        
        if abs(self.y_velocity) > 0:
            move_sprite = True
            ypos = self.y_velocity
        
        #Should the ship move
        if self.sprite.position[0] < self.x1:
            #Ship has moved off left side of screen
            xpos = self.x2
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
        elif self.sprite.position[0] > self.x2:
            #Ship has moved off right side of screen
            xpos = self.x1
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
        
        if self.sprite.position[1] < self.y1:
            #Ship has moved below screen
            ypos = self.y2
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
        elif self.sprite.position[1] > self.y2:
            #Ship has moved above screen
            ypos = self.y1
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite = False
            
        if move_sprite == True:
            #Sprite is still on the ship
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_by(xpos, ypos, 0))

        #Move Laser Code
        for laser in self.lazers:
            #loop through laser list and move it
            laser.move()
            if laser.delete == True:
                #Laser is marked for deletion (remove it)
                self.lazers.remove(laser)
                
        
    def draw(self, parent, x , y):
        #Draw sprite on screen
        self.sprite = SpriteNode(self.spriteFile,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale  = self.spriteScale)
    
    def shoot(self):
        if self.destroyed == False:
               
            # sound that is played when user hits the shoot button
            sound.play_effect('./assets/sounds/laser1.wav')
            
            # laser start position and angle is the same the ship position/angle
            # Build and append laser to lasers list            
            self.lazers.append(Laser(self.x1, self.y1,self.x2,self.y2, self.angle))

            # Draw laser
            self.lazers[len(self.lazers)-1].draw(self.sprite.scene, self.sprite.position[0], self.sprite.position[1])

            # Needed to keep laser aligned
            self.lazers[len(self.lazers)-1].sprite.rotation = self.sprite.rotation
            self.lazers[len(self.lazers)-1].angle = self.angle
            
    
