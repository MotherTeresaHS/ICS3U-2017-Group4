# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
from common import *
import ui
import math
import datetime
from spaceship import *
import random
from laser import *
import time
import ConfigParser, os
from main_menu_scene import *

#from main_menu_scene import *

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        #self.hide_close(True)
        # this code was taken from Mr. Coxalls game_scene
        self.ship = SpaceShip(0, 150 , self.size.x, self.size.y-50)
        
        self.asteroids = []
        self.asteroid_attack_rate = 1
        self.asteroid_attack_speed = 20.0
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        
        self.scale_size = 0.75
        
        self.score = 0
        
        # add borders to the screen
        self.border1 = SpriteNode(position = Point(0,self.size.y ),
                                    anchor_point = Point(0,1),
                                    z_position = 1.0,
                                    color = 'black', 
                                    parent = self,
                                    size = Size(self.size.x,45))
        self.border2 = SpriteNode(position = Point(0,0 ),
                                 anchor_point = Point(0,0),
                                 z_position = 1.0,
                                 color = 'black', 
                                 parent = self,
                                 size = Size(self.size.x,140))
        self.border3 = SpriteNode(position = Point(0,0 ),
                                    anchor_point = Point(0,0),
                                    z_position = 1.0,
                                    color = 'black', 
                                    parent = self,
                                    size = Size(12.5,self.size.y))
        self.border4 = SpriteNode(position = Point(self.size.x - 12.5 ,0 ),
                                    anchor_point = Point(0,0),
                                    z_position = 1.0,
                                    color = 'black', 
                                    parent = self,
                                    size = Size(12.5,self.size.y))
        
        # add background image
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.bg = SpriteNode(random_background(),
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        # add game buttons
        shoot_button_position = Vector2()
        shoot_button_position.x = self.size_of_screen_x - 100
        shoot_button_position.y = 75
        self.shoot_button = SpriteNode('./assets/sprites/red_button.png',
                                     parent = self,
                                     position = shoot_button_position,
                                     alpha = 1,
                                     z_position = 2,
                                     scale = self.scale_size)
        
        right_button_position = Vector2()
        right_button_position.x = self.size_of_screen_x - 774
        right_button_position.y = 75
        self.right_button = SpriteNode('./assets/sprites/right.png',
                                     parent = self,
                                     position = right_button_position,
                                     alpha = 1,
                                     z_position = 2,
                                     scale = 0.25)
    
        left_button_position = Vector2()
        left_button_position.x = self.size_of_screen_x - 924
        left_button_position.y = 75
        self.left_button = SpriteNode('./assets/sprites/left.png',
                                     parent = self,
                                     position = left_button_position,
                                     alpha = 1,
                                     z_position = 2,
                                     scale = 0.25)
    
        boost_button_position = Vector2()
        boost_button_position.x = self.size_of_screen_x - 250
        boost_button_position.y = 75
        self.boost_button = SpriteNode('./assets/sprites/boost.png',
                                     parent = self,
                                     position = boost_button_position,
                                     alpha = 1,
                                     z_position = 2,
                                     scale = 0.35)
    
        score_position = Vector2()
        score_position.x = 50
        score_position.y = self.size.y - 25
        self.score_label = LabelNode(text = ('SCORE: ' + str(self.score)),
                                      font = ('Helvetica', 20),
                                      parent = self,
                                      position = score_position,
                                      z_position = 2,
                                      scale = 0.75)
    
        self.ship.Draw(self, self.size_of_screen_x / 2, self.size_of_screen_y / 2)
        
    def update(self):
        
        if self.ship != None:
            self.ship.Move()
            self.ship.Rotate()
            self.ship.Thrust()
        
        asteroid_create_chance = random.randint(1, 120)
        if asteroid_create_chance <= self.asteroid_attack_rate:
            if len(self.asteroids) < 10:
                self.asteroid_generator()
        
        if self.ship.destroyed == True:
            if not self.presented_scene and time.time() - self.destroy_time > 3:
                self.view.close()
        
        if len(self.asteroids) > 0:
            for asteroid in self.asteroids:
                asteroid.move()
                if asteroid.sprite.frame.intersects(self.ship.sprite.frame) and self.ship.destroyed == False:
                    #Were close to the asteroid, need to see how close

                    #Creat a second rect inside the frame, adjusted by a percentage
                    asteroid_adjustment = int(asteroid.sprite.frame.w * 0.25)
                    ship_adjustment = int(self.ship.sprite.frame.w * 0.1)

                    #Check if the smaller rect intersected, if so game over
                    ship_rect = asteroid.sprite.frame.inset(asteroid_adjustment,asteroid_adjustment)
                    asteroid_rect = self.ship.sprite.frame.inset(ship_adjustment,ship_adjustment)

                    if ship_rect.intersects(asteroid_rect):
                        #Game Over
                        self.game_over()
                        #Save Scores
                        self.save_scores()
                        
                if len(self.ship.lazers) > 0:
                    #Check for collisions with lasers
                    self.collision_detection(asteroid)
        else:
            pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen

        if self.left_button.frame.contains_point(touch.location):
            self.ship.left = True
         
        if self.right_button.frame.contains_point(touch.location):
            self.ship.right = True
                    
        if self.shoot_button.frame.contains_point(touch.location):
            self.ship.Shoot()
        
        if self.boost_button.frame.contains_point(touch.location):
            self.ship.thrust_button = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen

        if self.shoot_button.frame.contains_point(touch.location):
            #Place holder so that the else statement works
            #without it, the rotation will stop during the shoot button release
            pass
        elif self.boost_button.frame.contains_point(touch.location):
            #Boost/Thrust button released
            self.ship.thrust_button = False
            #pass
        else:
            #Else we assume the they let their finger of the rotate controls.
            self.ship.left = False
            self.ship.right = False
    
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
    
    def asteroid_generator(self):

        #Create a random location to spawn the asteroid
        asteroid_start_position = Vector2()
        asteroid_start_position.x = random.randint(0, self.size_of_screen_y)
        asteroid_start_position.y = self.size_of_screen_y + 200

        #Generate a Random angle but not one that is in a straight line. i.e. 90/180, etc
        asteroid_angle = random.randint(1, 89)
        asteroid_angle += (random.randint(0,3) * 90 )

        #Create the Asteroid and Append to the list
        self.asteroids.append(Asteroid(0, 150 , self.size.x, self.size.y - 50, asteroid_angle, ASTEROID_LARGE, ASTEROID_NONE))
        self.asteroids[len(self.asteroids)-1].draw(self, asteroid_start_position.x, asteroid_start_position.y)
     
        
    def asteroid_builder(self, impact_angle, position, size, colour):

        #Similar to the generator, but builds a new version at a specified location
        #Used for asteroid splitting.

        #Convert angle to a integer
        impact_angle = int(impact_angle)

        #Calculate the Min and Max Angles of Deflection
        min_angle = impact_angle - 45
        max_angle = impact_angle + 45

        #Generate deflection angle
        asteroid_angle = random.randint(min_angle, max_angle)

        #Create the Asteroid and Append to the list
        self.asteroids.append(Asteroid(0, 150 , self.size.x, self.size.y-50, asteroid_angle, size, colour))
        self.asteroids[len(self.asteroids)-1].draw(self, position.x, position.y)
        
    def save_scores(self):
    	
        # reads config with high scores	
        config = ConfigParser.ConfigParser()
        config.readfp(open('./config.txt'))
        
        for x in range (1,6):
            saved_score = (config.get('Scores','score' + str(x),'0'))
            if self.score >= int(saved_score):
                # shift scores down before we save
                for i in range (5, x, -1):
                    previous_score = config.get('Scores', 'Score' + str(i - 1), self.score)
                    config.set('Scores', 'Score' + str(i), previous_score)
                config.set('Scores', 'Score' + str(x), self.score)

                #Save the config file
                with open('./config.txt', 'w') as configfile:
                    config.write(configfile)
                break
    
    def hide_close(self, state=True):
        #Taken from omz forum - user robnee
        #https://forum.omz-software.com/topic/3758/disable-stop-button-x-in-scene/5
		
        from objc_util import ObjCInstance
        v = ObjCInstance(self.view)
        # Find close button.  I'm sure this is the worst way to do it
        for x in v.subviews():
            if str(x.description()).find('UIButton') >= 0:
                x.setHidden(state)

    def game_over(self):
        #Game is over play boom
        sound.play_effect('./assets/sounds/boom.wav')

        #Show the Game over text
        
        text_position = Vector2()
        text_position.x = self.size.x/2
        text_position.y = self.size.y/2
        self.game_over = LabelNode(text = ('GAME OVER'),
                                            font = ('Helvetica', 140),
                                            parent = self,
                                            position = text_position,
                                            scale = 1)

        #Timer to auto close screen
        self.destroy_time = time.time()

        #Update the shipe information
        self.ship.destroyed = True
        self.ship.sprite.texture = None

    def collision_detection(self, asteroid):
        #Loop through laser list
        for laser in self.ship.lazers:
            if asteroid.sprite.frame.intersects(laser.sprite.frame):
                #Asteroid has intersected a laser
                if asteroid.size > ASTEROID_SMALL:
                    self.asteroid_builder(laser.angle, asteroid.sprite.position, asteroid.size - 1, asteroid.colour)
                    self.asteroid_builder(laser.angle, asteroid.sprite.position, asteroid.size - 1, asteroid.colour)
                if asteroid.size == ASTEROID_LARGE:
                    self.score += 99
                elif asteroid.size == ASTEROID_MEDIUM:
                    self.score += 199
                else:
                    # SMALL
                    self.score += 499

                #Update the score label
                self.score_label.text = ('SCORE: ' + str(self.score))

                #Remove the laser from the scene and list
                laser.sprite.remove_from_parent()
                self.ship.lazers.remove(laser)

                #Remove the asteroid from the scene and list
                asteroid.sprite.remove_from_parent()
                self.asteroids.remove(asteroid)
