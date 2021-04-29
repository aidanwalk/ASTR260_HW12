#Aidan Walk
#ASTR260-001
#28 April 2021, 17.00

#Problem 2 part b

import numpy as np
import matplotlib.pyplot as plt

def checkNearWall(x, y):
    '''Checks if particle is near wall
       returns list of possible moves
    '''
    moves = ['up', 'down', 'left', 'right']
    #check if we are near wall
    if x == 100: 
        moves.remove('right') #cannot move right
    elif x == 0:
        moves.remove('left')  #cannot move left
    if y == 100:
        moves.remove('up')  #cannot move up
    elif y == 0:
        moves.remove('down')    #cannot move down
            
    return moves
    
def moveDust(x, y, direction):
    '''moves dust up, down, left, or right depending on direction
       returns x, y'''
    if direction == 'up': y+=1
    elif direction =='down': y-=1
    elif direction =='left': x-=1
    elif direction =='right': x+=1
    
    return x, y
    
def run_simulation(n_steps=None, initial_pos=None, maxsize=None):
    dust = 1 #value of dust
    dust_Xpos, dust_Ypos = positions = initial_pos 
    
    moves_max = n_steps
    move=0
    while move < moves_max:
        #if near wall, eliminate possibility of that direction
        moves_potential = checkNearWall(dust_Xpos, dust_Ypos)
        #generate random next move
        move_next = np.random.choice(moves_potential)
        
        #return post-move coordinates
        dust_Xpos, dust_Ypos = moveDust(dust_Xpos, dust_Ypos, move_next)
        
        positions = np.vstack((positions, [dust_Xpos, dust_Ypos]))
        
        move+=1
        
    return positions