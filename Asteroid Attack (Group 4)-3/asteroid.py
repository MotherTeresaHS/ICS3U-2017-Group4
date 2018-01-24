# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene controls Asteroids

from scene import *
import math
import random
import sound
import datetime


#ShipSize Enum('LARGE',  'MEDIUM', 'SMALL')

class Asteroid:
    
    def __init__(self, x1arg, y1arg, x2arg, y2arg, xAngle, size):
        #Sprite Properties
        self.sprite_scale = 0.5
        self.sprite_file = './assets/sprites/asteroid.png'        

        # Flight Boundary 
        self.x1=x1arg
        self.y1=y1arg
        self.x2=x2arg
        self.y2=y2arg
        
        # Asteroid Properties 
        self.speed = 100
        self.size = size
        self.x_velocity = float(0)
        self.y_velocity = float(0)
        
        self.distance=0
        
        self.delete = False
        
        self.angle = xAngle + 90
        if self.angle > 360:
            self.angle -= 360
            
        self.sprite = None
        
        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle)) 
        self.x_velocity = self.speed * self.scale_x 
        self.y_velocity = self.speed * self.scale_y 
        
        #print('Missle', self.angle, self.scale_x, self.scale_y, self.x_velocity, self.y_velocity)
    
    def move(self):
        
        if self.sprite.scene == None:
            move_sprite = False
        else:
            move_sprite = True
            xpos = self.sprite.position[0] + self.x_velocity * self.sprite.scene.dt
            ypos = self.sprite.position[1] + self.y_velocity * self.sprite.scene.dt
            self.distance += self.speed * self.sprite.scene.dt

            #Asteroid Logic
            if random.randint(0,1) == 0:
                self.sprite.rotation = math.degrees(self.sprite.rotation + 1)
            else:
                self.sprite.rotation = math.degrees(self.sprite.rotation - 1)
                
        
        #Should the ship move
        if self.sprite.position[0] < self.x1:
            #Ship has moved off screen
            xpos = self.x2
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
            
        elif self.sprite.position[0] > self.x2:
            xpos = self.x1
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
        
        if self.sprite.position[1] < self.y1:
            ypos = self.y2
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
            
        elif self.sprite.position[1] > self.y2:
            ypos = self.y1
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
        
        if move_sprite== True:
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
        
    def draw(self, parent, x , y):
        if self.size == 3:
            #Large Asteroid (100%)
            scale = self.sprite_scale * 1
        elif self.size == 2:
            #Medim Asteroid (75%)
            scale = self.sprite_scale * 0.75
        else:
            #Medim Asteroid (50%)
            scale = self.sprite_scale * 0.5
        
        self.sprite = SpriteNode(self.sprite_file,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale = self.sprite_scale)
        
       
    
