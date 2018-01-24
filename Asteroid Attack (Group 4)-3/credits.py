# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene gives credit where credit is due.

from scene import *
import ui
from common import *
from main_menu_scene import *

class Credits(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        middle = self.size.x / 2
        
        
        # add background color
        self.background = SpriteNode(random_background(),
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
    
        self.credits_label = SpriteNode('./assets/sprites/credits.png',
                                        parent = self,
                                        position = self.size/2)
    
    
        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = back_button_position.y - 75
        self.back_button = SpriteNode('./assets/sprites/back.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.2)
               
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension

        self.background.position = self.size/2
        self.background.size = self.size

        self.credits_label.position = self.size/2

        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = self.size.y - 75
        self.back_button.position = back_button_position
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
