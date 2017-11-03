# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:29:33 2016

@author: Mebius
"""

import random

class Cuboid():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
        #implement this!
    def get_area(self):
        pass
        #implement this!
    def get_volume(self):
        pass

    def __str__(self):
        c_str = 'Length: ' + str(self.x) + \
              ', Width: ' + str(self.y) + \
              ', Height: ' + str(self.z) + \
              ', AREA: ' + str(self.get_area()) + \
              ', VOLUME: ' + str(self.get_volume())
        return c_str

class CCuboid(Cuboid):
    def __init__(self, x,y,z, color ):
            Cuboid.__init__(self, x , y , z )
            pass
        
    def set_color(self, color):
        pass
    
    def get_color(self):
        pass

    def __str__(self):
        a_str = super().__str__() + ', Color: ' + str(self.get_color())
        return a_str    

if __name__ == "__main__":

    x=1
    y=2
    z=3
    
    c = Cuboid(x,y,z)
    print(c)
    
    color= input("Input your color: ")

    a = CCuboid(x,y,z,color)
    print(a)
    #print('Length: '+str(x)+", Width: "+str(y)+', Height: '+str(z)+', AREA: '+str(i.get_area())+', VOLUME: '+str(i.get_volume()))

