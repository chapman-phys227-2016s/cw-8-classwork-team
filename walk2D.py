"""
Author: Andrew Malfavon
walk2D code for Classwork 8
Copied from the book. A random walk in two dimensions performs a step either to the north,
south, west, or east, each one with probability 1/4.
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import sys

def random_walk_2D(np, ns, plot_step):
    xpositions = np.zeros(np)
    ypositions = np.zeros(np)
    #extent of the axis on the plot
    xymax = 3 * np.sqrt(ns)
    xymin = -xymax
    #constants
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4
    for step in range(ns):
        for i in range(np):
            direction = random.randint(1, 4)
            if direction == NORTH:
                ypositions[i] -= 1
            elif direction == SOUTH:
                ypositions[i] -= 1
            elif direction == EAST:
                xpositions[i] += 1
            elif direction == WEST:
                xpositions[i] -= 1
        #Plot just every plot_step steps
        if ((step+1) % plot_step == 0):
            fig, ax = plt.subplots(nrows = 1, ncols = 1)
            ax.plot(xpositions, ypositions, 'ko')
            ax.set_ylim([xymin, xymax])
            ax.set_xlim([xymin, xymax])
            fig.savefig('tmp_%03d.png' % (self.step))
    return xpositions, ypositions

if __name__ == "__main__":
    np = int(sys.argv[1]) #number of particles
    ns = int(sys.argv[2]) #number of steps
    plot_step = int(sys.argv[3]) #plot every plot_step steps
    x, y = random_walk_2D(np, ns, plot_step)