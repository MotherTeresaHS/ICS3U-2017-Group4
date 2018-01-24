# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from main_game import *
from high_scores import *
from credits import *

#self.present_modal_scene(MainMenuScene())


class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.bg = SpriteNode('./assets/sprites/main_bg.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
    
        start_button_position = Vector2()
        start_button_position.x = self.screen_center_x
        start_button_position.y = self.screen_center_y + 120
        self.start_button = SpriteNode('./assets/sprites/play.JPG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 0.4)
    
        scores_button_position = self.size/2
        self.scores_button = SpriteNode('./assets/sprites/score.PNG',
                                       parent = self,
                                       position = scores_button_position,
                                       scale = 1.27)
    
        credits_button_position = self.size/2
        credits_button_position.y = credits_button_position.y - 120
        self.credits_button = SpriteNode('./assets/sprites/credits.JPG',
                                       parent = self,
                                       position = credits_button_position,
                                       scale = 0.4)
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
            #self.present_modal_scene(GameScene(),orientation=LANDSCAPE)
            run(GameScene(),orientation = LANDSCAPE, show_fps = True, multi_touch = True)
        
        if self.scores_button.frame.contains_point(touch.location):
            self.present_modal_scene(HighScores())
        
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(Credits())
            
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        self.setup()
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
