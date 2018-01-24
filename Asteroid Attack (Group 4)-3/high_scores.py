# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the users top 5 scores on the device.

from scene import *
import ui
import ConfigParser, os

from main_menu_scene import *

class HighScores(Scene):
    def setup(self):
        # this method is called, when user moves to this scene

        # reads config file with high scores
        config = ConfigParser.ConfigParser()
        config.readfp(open('./config.txt'))

        score1 = (config.get('Scores','Score1','0'))
        score2 = (config.get('Scores','Score2','0'))
        score3 = (config.get('Scores','Score3','0'))
        score4 = (config.get('Scores','Score4','0'))
        score5 = (config.get('Scores','Score5','0'))

        middle = self.size.x / 2

        # add background color
        self.background = SpriteNode(position = self.size / 2,
                                     color = 'black',
                                     parent = self,
                                     size = self.size)

        # create title label
        title_position = Vector2()
        title_position.x = middle
        title_position.y = self.size.y - 75
        self.title = LabelNode(text = 'HIGH SCORES',
                                      font = ('Helvetica', 60),
                                      parent = self,
                                      position = title_position,
                                      scale = 0.75)

        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = self.size.y - 75
        self.back_button = SpriteNode('./assets/sprites/back.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.2)

        # Creating labels for high scores 1-5
        first_place = Vector2()
        first_place.x = middle
        first_place.y = self.size.y - 200
        self.first_place = LabelNode(text = '1.  ' + score1,
                                      font = ('Helvetica', 40),
                                      parent = self,
                                      position = first_place,
                                      scale = 1)

        second_place = Vector2()
        second_place.x = middle
        second_place.y = self.size.y - 275
        self.second_place = LabelNode(text = '2.  ' + score2,
                                      font = ('Helvetica', 40),
                                      parent = self,
                                      position = second_place,
                                      scale = 1)

        third_place = Vector2()
        third_place.x = middle
        third_place.y = self.size.y - 350
        self.third_place = LabelNode(text = '3.  ' + score3,
                                      font = ('Helvetica', 40),
                                      parent = self,
                                      position = third_place,
                                      scale = 1)

        fourth_place = Vector2()
        fourth_place.x = middle
        fourth_place.y = self.size.y - 425
        self.fourth_place = LabelNode(text = '4.  ' + score4,
                                      font = ('Helvetica', 40),
                                      parent = self,
                                      position = fourth_place,
                                      scale = 1)

        fifth_place = Vector2()
        fifth_place.x = middle
        fifth_place.y = self.size.y - 500
        self.fifth_place = LabelNode(text = '5.  ' + score5,
                                      font = ('Helvetica', 40),
                                      parent = self,
                                      position = fifth_place,
                                      scale = 1)

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

   
