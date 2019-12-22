"""
File: MicahNightShift.pyde
Description: A Processing script that randomly draws circles recursively within hexagon of seven circles. See pictures for better details.
Author: Micah Wood

This is my reproduction from https://www.reddit.com/r/proceduralgeneration/comments/dsa9w9/night_shift/
"""

from random import random

# Global constants
WINDOW_SIZE = 600
MAX_DEPTH = 4
PROBABILITY = 0.6

def circleRecursive( x, y, diameter, depth = 0, p = PROBABILITY ):
    if depth > MAX_DEPTH or random() <= p:
        circle( x, y, diameter )

    else:
        newDiameter = diameter / 3
                
        # Top Row
        circleRecursive( x - newDiameter/2, y - sqrt(3)*newDiameter/2, newDiameter, depth+1 )
        circleRecursive( x + newDiameter/2, y - sqrt(3)*newDiameter/2, newDiameter, depth+1 )
        
        # Middle Row
        circleRecursive( x - newDiameter, y, newDiameter, depth+1 )
        circleRecursive( x, y, newDiameter, depth+1 )
        circleRecursive( x + newDiameter, y, newDiameter, depth+1 )
        
        # Bottom Row
        circleRecursive( x - newDiameter/2, y + sqrt(3)*newDiameter/2, newDiameter, depth+1 )
        circleRecursive( x + newDiameter/2, y + sqrt(3)*newDiameter/2, newDiameter, depth+1 )
        

def setup():
    size( WINDOW_SIZE, WINDOW_SIZE )
    background( 25 )
    noFill()
    stroke( 200 );
    
    circleRecursive( WINDOW_SIZE/2, WINDOW_SIZE/2, WINDOW_SIZE, p = 0 )
    
