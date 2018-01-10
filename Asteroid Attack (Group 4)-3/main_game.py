# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
import ui
import math
import datetime
from spaceship import *

#from main_menu_scene import *

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        #*print('game')
        # this code was taken from Mr. Coxalls game_scene
        self.Ship = SpaceShip(0, 150 , self.size.x, self.size.y-50)
        #self.Ship.OffsetX2 = self.size.x
        #self.
        #print (self.Ship.Left)
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        
        self.scale_size = 0.75
        
        # add background image
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        #self.bg = SpriteNode('./assets/sprites/star_background.png',
        #                             position = background_position, 
        #                             parent = self, 
        #                             size = self.size)
        #                             
        # add game buttons
        shoot_button_position = Vector2()
        shoot_button_position.x = self.size_of_screen_x - 100
        shoot_button_position.y = 75
        self.shoot_button = SpriteNode('./assets/sprites/red_button.png',
                                     parent = self,
                                     position = shoot_button_position,
                                     alpha = 1,
                                     scale = self.scale_size)
        
        right_button_position = Vector2()
        right_button_position.x = self.size_of_screen_x - 774
        right_button_position.y = 75
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                     parent = self,
                                     position = right_button_position,
                                     alpha = 1,
                                     scale = self.scale_size)
    
        left_button_position = Vector2()
        left_button_position.x = self.size_of_screen_x - 924
        left_button_position.y = 75
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                     parent = self,
                                     position = left_button_position,
                                     alpha = 1,
                                     scale = self.scale_size)
    
        boost_button_position = Vector2()
        boost_button_position.x = self.size_of_screen_x - 250
        boost_button_position.y = 75
        self.boost_button = SpriteNode('./assets/sprites/red_button.png',
                                     parent = self,
                                     position = boost_button_position,
                                     alpha = 1,
                                     scale = self.scale_size)
    
        title_position = Vector2()
        title_position.x = 50
        title_position.y = self.size.y - 25
        self.start_button = LabelNode(text = 'SCORE:',
                                      font = ('Helvetica', 20),
                                      parent = self,
                                      position = title_position,
                                      scale = 0.75)
    
        # add spaceship sprite
        #spaceship_position = Vector2()
        #spaceship_position.x = self.size_of_screen_x / 2
        #spaceship_position.y = self.size_of_screen_y /2
        #self.spaceship = SpriteNode('./assets/sprites/spaceship.png',
        #                             parent = self,
        #                             position = spaceship_position,
        #                             scale = self.scale_size / 3)
        #self.Ship.Sprite = self.spaceship
        self.Ship.Draw(self, self.size_of_screen_x / 2, self.size_of_screen_y / 2)
        
        #print(repr(self.Ship))
        
    def update(self):
        self.Ship.Rotate()
        self.Ship.Thrust()
        if self.Ship != None:
            self.Ship.Move()
        #pass
        # this method is called, hopefully, 60 times a second
        #if self.left_button_down == True:
        #    self.spaceship.rotation= self.spaceship.rotation + self.sensitivity
    
        #f self.right_button_down == True:
         #   self.spaceship.rotation= self.spaceship.rotation - self.sensitivity
    
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        if self.left_button.frame.contains_point(touch.location):
            #self.left_button_down = True
            self.Ship.Left = True
            #print(datetime.datetime.now(), 'Begin', 'Left', touch.touch_id)
         
        if self.right_button.frame.contains_point(touch.location):
            #self.right_button_down = True
            self.Ship.Right = True
            #print(datetime.datetime.now(), 'Begin', 'Right', touch.touch_id)
                    
        if self.shoot_button.frame.contains_point(touch.location):
            #self.shoot_button_down = True
            # print(datetime.datetime.now(), 'Begin', 'Shoot', touch.touch_id)
            self.Ship.Shoot()
        
        if self.boost_button.frame.contains_point(touch.location):
            #self.boost_button_down = True
            #print(datetime.datetime.now(), 'Begin', 'Thrust', touch.touch_id)
            self.Ship.ThrustButton = True
            #rint 'boosted'
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #print('End', '', touch.touch_id)
        if self.shoot_button.frame.contains_point(touch.location):
            #self.Ship.Shoot()
            #print(datetime.datetime.now(), 'End', 'Shoot', touch.touch_id)
            #self.create_new_missile()
            pass
        elif self.boost_button.frame.contains_point(touch.location):
            #print(datetime.datetime.now(), 'End', 'Thrust', touch.touch_id)
            self.Ship.ThrustButton = False
            #pass
        else:
            # if I removed my finger, then no matter what spaceship
            #    should not be moving any more
            #print(datetime.datetime.now(), 'End', 'Rotate', touch.touch_id)
            self.Ship.Left = False
            self.Ship.Right = False
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        
        pass
    
