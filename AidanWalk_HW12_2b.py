#Aidan Walk
#ASTR260-001
#28 April 2021, 17.00

#Problem 2

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

if __name__ == '__main__':
    L = 101 #length of lattice
    lattice = np.zeros((L, L)) #value of lattice = zero
    
    dust_Xpos, dust_Ypos = 50, 50 #initial position conditions
    dust = 1 #value of dust
    
    #insert dust to middle of box
    lattice[dust_Ypos, dust_Xpos] = dust    
    
    moves_max = 10000
    move=0
    while move < moves_max:
        #if near wall, eliminate possibility of that direction
        moves_potential = checkNearWall(dust_Xpos, dust_Ypos)
        #generate random next move
        move_next = np.random.choice(moves_potential)
        
        #return post-move coordinates
        dust_XposNew, dust_YposNew = moveDust(dust_Xpos, dust_Ypos, move_next)
        
        #remove dust from old position
        #lattice[dust_Ypos, dust_Xpos] += 1
        #move dust to new position
        lattice[dust_YposNew, dust_XposNew] += dust
        
        dust_Xpos, dust_Ypos = dust_XposNew, dust_YposNew
        
        move+=1
    
    
    
    plotTitle = 'Dust Movement Over '+str(moves_max)+' Moves'
    plotfName = 'AidanWalk_HW12_2b_Plot'+'.png'
    
    plt.imshow(lattice, cmap='Greys')
    plt.title(plotTitle)
    plt.xlabel('Darker=More visits')
    
    plt.savefig(plotfName, dpi=300)
    print('Plot saved to', plotfName)