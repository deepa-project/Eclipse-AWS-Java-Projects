# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 04:33:16 2020

@author: deepa
"""
#Source:Python Crash Course-Eric Matthes
from random import randint

#Creating die class
class Die:
    """A class representing a single die"""
    
    def __init__(self, num_sides=6):
        """Assume a single sided die"""
        self.num_sides=num_sides
        
    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1,self.num_sides)

