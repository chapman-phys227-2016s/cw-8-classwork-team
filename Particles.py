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
import matplotlib
matplotlib.use('Agg')
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
        self.step = 0
    def move(self, step_size = 1):
        """
        Translates all particles uniformly by step_size
        """
        for p in self.particles:
            p.move(step_size)
        self.step += 1
        
    def plot(self):
        """
        Plots all particles
        """
        xpositions = []
        ypositions = []
        for p in self.particles:
            xpositions.append(p.x)
            ypositions.append(p.y)
            plt.plot(xpositions, ypositions, 'ko',
                     axis = [-100,100,-100,100],
                     title = '%d particles after %d steps' %
                         (self.np, self.step+1),
                     savefig = 'tmp_%03d.pdf' % (self.step+1))
    
    def generate_frame(self):
        """
        Plots the particles and outputs them to a file
        """
        xpositions = []
        ypositions = []
        for p in self.particles:
            xpositions.append(p.x)
            ypositions.append(p.y)
            fig, ax = plt.subplots(nrows = 1, ncols = 1)
            ax.plot(xpositions, ypositions, 'ko')
            ax.set_ylim([-10,10])
            ax.set_xlim([-10,10])
            fig.savefig('tmp_%03d.png' % (self.step))
            plt.close(fig)

    def moves(self, N = 10, step_size = 1):
        """
        Loops over move() and plot() function N times
        """
        self.generate_frame()
        for i in xrange(N):
            self.move(step_size)
            self.generate_frame()

class Test_Particles(TestCase):
    def test(self):
        pass