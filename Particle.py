#!/usr/python/bin
"""
Author: Michael Seaman
Particle class for Classwork 8
Defines particle objects that are seeded at initialization
and move around accordingly
"""
import numpy as np
from datetime import datetime

class Particle:
    """
    Defines particle objects that are seeded at initialization
and move around accordingly
    """
    def __init__(self, seed = datetime.now, x= 0, y = 0):
        self.x = x
        self.y = y
        self.RNG = np.random.RandomState(seed)
    
    def move(self, step_size = 1):
        """
        Moves in a random (seeded) direction with a distance of
        an optional stepsize
        """
        switch = RNG.randint(1, 5)
        if(switch == 1):
            y += step_size #Up
        elif(switch == 2):
            x += step_size #Right
        elif(switch == 3):
            y -= step_size #Down
        else:
            x -= step_size #left

    def test_confined_movement():
        """
        Given n number of steps, the particles
        should not deviate n units from the origin
        n = [10, 100, 1000]
        """
        n = [10, 100, 1000]
        p = Particle()
        for x in xrange(n[0]):
            p.move()
        p = Particle()
        for x in xrange(n[0]):
            p.move()
        
        
        