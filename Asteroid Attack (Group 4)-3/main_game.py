# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
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
        
        # this code was taken from Mr. Coxalls game_scene
        self.Ship = SpaceShip(0, 150 , self.size.x, self.size.y-50)
        
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
        self.right_button = SpriteNode('./assets/sprites/right.png',
                                     parent = self,
                                     position = right_button_position,
                                     alpha = 1,
                                     scale = 0.25)
    
        left_button_position = Vector2()
        left_button_position.x = self.size_of_screen_x - 924
        left_button_position.y = 75
        self.left_button = SpriteNode('./assets/sprites/left.png',
                                     parent = self,
                                     position = left_button_position,
                                     alpha = 1,
                                     scale = 0.25)
    
        boost_button_position = Vector2()
        boost_button_position.x = self.size_of_screen_x - 250
        boost_button_position.y = 75
        self.boost_button = SpriteNode('./assets/sprites/red_button.png',
                                     parent = self,
                                     position = boost_button_position,
                                     alpha = 1,
                                     scale = self.scale_size)
    
        score_position = Vector2()
        score_position.x = 50
        score_position.y = self.size.y - 25
        self.score_label = LabelNode(text = ('SCORE: ' + str(self.score)),
                                      font = ('Helvetica', 20),
                                      parent = self,
                                      position = score_position,
                                      scale = 0.75)
    
        self.Ship.Draw(self, self.size_of_screen_x / 2, self.size_of_screen_y / 2)
        
    def update(self):
        self.Ship.Rotate()
        self.Ship.Thrust()
        if self.Ship != None:
            self.Ship.Move()
        
        
        asteroid_create_chance = random.randint(1, 120)
        if asteroid_create_chance <= self.asteroid_attack_rate:
            if len(self.asteroids) < 10:
                self.asteroid_generator()
        
        if self.Ship.destoryed == True:
            if not self.presented_scene and time.time() - self.destroy_time > 3:
                self.view.close()
        
        if len(self.asteroids) > 0:
            for asteroid in self.asteroids:
                #print('asteroid', asteroid.frame)
                asteroid.move()
                if asteroid.Sprite.frame.intersects(self.Ship.Sprite.frame):
                    text_position = Vector2()
                    text_position.x = self.size.x/2
                    text_position.y = self.size.y/2
                    self.game_over = LabelNode(text = ('GAME OVER'),
                                               font = ('Helvetica', 140),
                                               parent = self,
                                               position = text_position,
                                               scale = 1)
                    self.destroy_time = time.time()
                    self.Ship.destoryed = True
                    self.Ship.Sprite.texture = None
                if len(self.Ship.lazers) > 0:
                    for lazerr in self.Ship.lazers:
                        #print ('lazer', lazerr.Sprite.frame, lazerr.Sprite.position)
                        #print ('lazer', asteroid.frame , lazerr.Sprite.position)
                        if asteroid.Sprite.frame.intersects(lazerr.Sprite.frame):
                            if asteroid.size > 1:
                                self.asteroid_builder(lazerr.Angle, asteroid.Sprite.position, asteroid.size - 1)
                                self.asteroid_builder(lazerr.Angle, asteroid.Sprite.position, asteroid.size - 1)
                            if asteroid.size == 3:
                                self.score += 99
                            elif asteroid.size == 2:
                                self.score += 199
                            else:
                                self.score += 499
                            self.score_label.text = ('SCORE: ' + str(self.score))
                            lazerr.Sprite.remove_from_parent()
                            self.Ship.lazers.remove(lazerr)
                            asteroid.Sprite.remove_from_parent()
                            self.asteroids.remove(asteroid)
                            
        else:
            pass
        
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
    
    def asteroid_generator(self):
        asteroid_start_position = Vector2()
        asteroid_start_position.x = random.randint(100, self.size_of_screen_x - 300)
        asteroid_start_position.y = self.size_of_screen_y + 300
        
        asteroid_end_position = Vector2()
        asteroid_end_position.x = random.randint(0, self.size_of_screen_y)
        asteroid_end_position.y = self.size_of_screen_y + 200
        
        asteroid_angle = random.randint(210, 330)
        
        self.asteroids.append(Asteroid(0, 150 , self.size.x, self.size.y-50, asteroid_angle, 3))
        
        self.asteroids[len(self.asteroids)-1].draw(self, asteroid_end_position.x, asteroid_end_position.y)
        #self.asteroids[len(self.asteroids)-1].Sprite.rotation = 
        self.asteroids[len(self.asteroids)-1].Angle = asteroid_angle
        
        # make missile move forward
        asteroidMoveAction = Action.move_to(asteroid_end_position.x, 
                                            asteroid_end_position.y, 
                                            self.asteroid_attack_speed,
                                            TIMING_SINODIAL)
        self.asteroids[len(self.asteroids)-1].Sprite.run_action(asteroidMoveAction)
        
    def asteroid_builder(self, impact_angle, position, size):
        impact_angle = int(impact_angle)
        min_angle = impact_angle - 45
        max_angle = impact_angle + 45
        print ('angle', impact_angle, min_angle, max_angle)
        asteroid_angle = random.randint(min_angle, max_angle)
        
        self.asteroids.append(Asteroid(0, 150 , self.size.x, self.size.y-50, asteroid_angle, size))
        
        self.asteroids[len(self.asteroids)-1].draw(self, position.x, position.y)
        #self.asteroids[len(self.asteroids)-1].Sprite.rotation = 
        self.asteroids[len(self.asteroids)-1].Angle = asteroid_angle
        
        # make missile move forward
        asteroidMoveAction = Action.move_to(position.x, 
                                            position.y, 
                                            self.asteroid_attack_speed,
                                            TIMING_SINODIAL)
        self.asteroids[len(self.asteroids)-1].Sprite.run_action(asteroidMoveAction)
        
    def save_scores(self):
    	
        # reads config with high scores	
        config = ConfigParser.ConfigParser()
        config.readfp(open('./config.txt'))
        
        for x in range (1,6):
            saved_score = (config.get('Scores','score' + str(x),'0'))
            if self.score >= saved_score:
                config.set('Scores','score' + str(x), self.score)
                for y in range(5,x):
                    current_score = config.get(config.get('Scores','score' + str(y),'0'))
                    config.set('Scores','score' + str(y), saved_score)
                    config.set('Scores','score' + str(y + 1), next_score)
