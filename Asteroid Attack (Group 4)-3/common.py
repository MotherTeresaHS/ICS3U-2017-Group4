# Created by: Justin Bronson
# Created on: Jan 2018
# Created for: ICS3U
# This file contains shared procedures or functions

import math
def random_background():
    #Pick a random background 
    background_no = random.randint(1,9)
    #Build the filename
    filename = './assets/sprites/Background' + str(background_no) + '.jpg'
    return filename

    
