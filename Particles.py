#! /usr/bin/env python

"""
File: Particles.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 8.15
Date: March 18, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Framework over Object Particle, to plot and move each Particle

"""
import random as R
import matplotlib.pyplot as plt
from unittest import TestCase

class Particles:
    """
    Moves and plots objects of type 'Particle'
    """
    def __init__(self, particles):
        """
        particles is an array of type 'Particle'
        """
        self.particles = particles
        self.np = len(particles)
        self.step = 1
    def move(self, step_size = 1):
        """
        Translates all particles uniformly by step_size
        """
        for p in self.particles:
            p.move(step_size)

    def plot(self):
        """
        Plots all particles
        """
        xpositions = []
        ypositions = []
        for p in self.particles:
            xpositions.append(p.x)
            ypositions.append(p.y)
            plt.plot(xpostions, ypositions, 'ko',
                     axis = [-100,100,-100,100],
                     title = '%d particles after %d steps' %
                         (np, step+1)
                     savefig = 'tmp_%03d.pdf' % (step+1)


    def moves(self, N = 10, step_size = 1):
        """
        Loops over move() and plot() function N times
        """
        for i in xrange(N):
            self.move(step_size)
            self.plot()

class Test_Particles(TestCase):
    def test(self):