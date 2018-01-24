# Created by: Justin Bronson
# Created on: Dec 2017
# Created for: ICS3U
# This scene runs the main game.

from scene import *
import math
import spaceobj
import sound
import datetime
from main_game import *

#class Laser:
class Laser(SpaceObject):
    
    def __init__(self, x1arg, y1arg, x2arg, y2arg, xAngle):

        super(Laser, self).__init__(self, x1arg, y1arg, x2arg, y2arg, xAngle)

        # Properties
        self.sprite_scale= 1
        self.sprite_file= './assets/sprites/bullet.png'        
        self.speed = 400
        self.max_distance = 500
        
        
    
