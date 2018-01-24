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
        
        # reads config file with credits
        config = ConfigParser.ConfigParser()
        config.readfp(open('./config.txt'))
        
        credit1 = (config.get('Credits','Credit1','0'))
        credit2 = (config.get('Credits','Credit2','0'))
        credit3 = (config.get('Credits','Credit3','0'))
        credit4 = (config.get('Credits','Credit4','0'))
        credit5 = (config.get('Credits','Credit5','0'))
        credit6 = (config.get('Credits','Credit6','0'))
        credit7 = (config.get('Credits','Credit7','0'))
        credit8 = (config.get('Credits','Credit8','0'))
        
        # add background color
        self.background = SpriteNode(random_background(),
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
    
        self.credits_label = SpriteNode('./assets/sprites/credits.png',
                                        parent = self,
                                        position = self.size/2)
    
        title_position = Vector2()
        title_position.x = self.size.x / 2
        title_position.y = self.size.y - 75
        self.title = LabelNode(text = 'CREDITS',
                                      font = ('Helvetica', 60),
                                      parent = self,
                                      position = title_position,
                                      scale = 0.75)
    
        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = back_button_position.y - 75
        self.back_button = SpriteNode('./assets/sprites/back.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.2)
        
        credit1_label = Vector2()
        credit1_label.x = self.size.x * (3/4)
        credit1_label.y = 400
        self.credit1_label = LabelNode(text = credit1,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit1_label,
                                      scale = 0.75)
        
        credit2_label = Vector2()
        credit2_label.x = middle + 50
        credit2_label.y = 400
        self.credit2_label = LabelNode(text = credit2,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit2_label,
                                      scale = 0.75)
        
        credit3_label = Vector2()
        credit3_label.x = 50
        credit3_label.y = 300
        self.credit3_label = LabelNode(text = credit3,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit3_label,
                                      scale = 0.75)
        
        credit4_label = Vector2()
        credit4_label.x = middle + 50
        credit4_label.y = 300
        self.credit1_label = LabelNode(text = credit4,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit4_label,
                                      scale = 0.75)
        
        credit5_label = Vector2()
        credit5_label.x = 50
        credit5_label.y = 200
        self.credit5_label = LabelNode(text = credit5,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit5_label,
                                      scale = 0.75)
        
        credit6_label = Vector2()
        credit6_label.x = middle + 50
        credit6_label.y = 200
        self.credit6_label = LabelNode(text = credit6,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit6_label,
                                      scale = 0.75)
        
        credit7_label = Vector2()
        credit7_label.x = 50
        credit7_label.y = 100
        self.credit7_label = LabelNode(text = credit7,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit7_label,
                                      scale = 0.75)
        
        credit8_label = Vector2()
        credit8_label.x = middle + 50
        credit8_label.y = 100
        self.credit8_label = LabelNode(text = credit8,
                                      font = ('Helvetica', 30),
                                      parent = self,
                                      position = credit8_label,
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
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        self.setup()
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
