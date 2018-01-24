# Created by: Justin Bronson
# Created on: Jan 2018
# Created for: ICS3U
# This file contains shared procedures or functions

import random
def random_background():
    #Pick a random background 
    background_no = random.randint(1,9)
    #Build the filename
    filename = './assets/sprites/Background' + str(background_no) + '.jpg'
    return filename

    
def calc_rect(self, section, columns, rows):
    #calculate the width and height of column/row
    width = 1.0 / float(columns)
    height = 1.0 / float(rows)

    #ypos - section number - 1 - offset starts at 0 / colume
    #    section number starts at 0 so we have to subtract 1
    #    divide that by the columns and convert to a whole number
    #    add 1 because the calculation is off by one
    #    multiply by the row height to get the ypos
    ypos = 1 - (((int(section - 1) / columns) + 1 ) * height)

    # xps = find out what row we are on
    # if remainder is 0 its row > 0 then we are on the last row
    row = math.fmod(section,rows) 
    if row == 0.0 and int (section / rows) > 0:
        row = rows 

    # xpos = row - 1 ( 0 Offset so we go back 1) * row height
    xpos = ((row - 1) * width)

    # return a rect of the area
    return Rect(xpos, ypos, width, height)
    
def explode(self, x, y, section, columns):
    #section is the section to show
    #columns is how many columns of pictures on the texture
    
    width = int(self.explosion_texture.size.x)
    height = int(self.explosion_texture.size.y)

    #calculate the x offset
    xpos = int(math.fmod(section,columns) * width)  
    if math.fmod(section,columns) == 0:
        xpos = (7 ) * width
    else:
        pass
    xpos -= width

    #calculate the y offset
    ypos = int((section - 1) / columns) * height 

    #Get the the subtexture from the explosion texture
    pic= self.explosion_texture.subtexture(self.calc(section, columns, columns))
        
    return pic
