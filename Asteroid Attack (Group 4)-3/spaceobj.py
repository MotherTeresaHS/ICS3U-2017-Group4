# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This object is the base class for all space objects

from scene import *
import math
import sound
import datetime


class SpaceObject:
    
    def __init__(self, x1arg, y1arg, x2arg, y2arg, xAngle, size):

        #Sprite Properties
        sprite_scale = 1
        sprite_file = ''
        self.sprite = None

        # Flight Boundary 
        self.x1=x1arg
        self.y1=y1arg
        self.x2=x2arg
        self.y2=y2arg
        
        # Asteroid Properties 
        self.speed = 1
        self.distance=0
        self.max_distance = 0
        self.delete = False

        #Adjust angle by 90 degrees
        self.angle = xAngle + 90
        if self.angle > 360:
            self.angle -= 360

        #Calculate x and y scale
        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        #Calculate x and y velocity
        self.x_velocity = self.speed * self.scale_x 
        self.y_velocity = self.speed * self.scale_y 
        
    
    def move(self):
        
        if self.sprite.scene == None:
            move_sprite = False
        else:
            move_sprite = True
            xpos = self.sprite.position[0] + self.x_velocity * self.sprite.scene.dt
            ypos = self.sprite.position[1] + self.y_velocity * self.sprite.scene.dt
            if self.max_distance > 0:
                self.distance += self.speed * self.sprite.scene.dt
        
        #Should the sprite move
        if self.sprite.position[0] < self.x1:
            #Sprite has moved off left side of screen
            xpos = self.x2
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
            
        elif self.sprite.position[0] > self.x2:
            #Sprite has moved off right side of screen
            xpos = self.x1
            ypos = self.sprite.position[1]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
        
        if self.sprite.position[1] < self.y1:
            #Sprite has moved off bottom side of screen
            ypos = self.y2
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
            
        elif self.sprite.position[1] > self.y2:
            #Sprite has moved off top side of screen
            ypos = self.y1
            xpos = self.sprite.position[0]
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
            move_sprite= False
        
        if move_sprite== True:
            self.sprite.remove_all_actions()
            self.sprite.run_action(Action.move_to(xpos, ypos, 0))
        
    def draw(self, parent, x , y):
        
        self.sprite = SpriteNode(self.sprite_file,
                                     parent = parent,
                                     position = Vector2(x,y),
                                     scale = scale)
        
       
    
