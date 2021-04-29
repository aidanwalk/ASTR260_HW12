#Aidan Walk
#ASTR260-001
#28 April 2021, 17.00

#Problem 2 part c

import numpy as np
import matplotlib.pyplot as plt
import AidanWalk_HW12_2c as p2c

if __name__ == "__main__":
    print("c.   Plot the track of the particle over 10000 steps (3 points)")
    pos = np.array([50, 50])
    maxsize = 101
    #run for 10,000 steps
    steps1e4 = p2c.run_simulation(n_steps=10000, initial_pos=pos, maxsize=maxsize)
    #steps1e4 = np.random.randint(0, 101, size = (10000, 2))
    #animate the figure
    plt.ion()
    fig, ax = plt.subplots(figsize=(10,10))
    plt.xlim((0, maxsize))
    plt.ylim(0, maxsize)
    ax.set_aspect('equal')
    scat = ax.scatter(*pos)
    plt.title("Brownian motion in a box "+str(maxsize-1)+" units on a side")
    for i in range(10000):
        scat.set_offsets([steps1e4[i,0], steps1e4[i,1]])
        plt.draw()
        plt.pause(0.01)