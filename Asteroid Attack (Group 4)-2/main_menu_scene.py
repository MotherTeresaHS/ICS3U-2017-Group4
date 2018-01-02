# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from main_game import *
from high_scores import *
from credits import *
from settings import *

#self.present_modal_scene(MainMenuScene())


class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
    
        self.start_button = SpriteNode('./assets/sprites/start.png',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.75)
    
        scores_button_position = self.size/2
        scores_button_position.y = scores_button_position.y - 120
        self.scores_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = scores_button_position,
                                       scale = 0.75)
    
        credits_button_position = self.size/2
        credits_button_position.y = credits_button_position.y - 240
        self.credits_button = SpriteNode('./assets/sprites/menu_button.png',
                                       parent = self,
                                       position = credits_button_position,
                                       scale = 0.75)
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
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        
        if self.scores_button.frame.contains_point(touch.location):
            self.present_modal_scene(HighScores())
    
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(Credits())
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
    
