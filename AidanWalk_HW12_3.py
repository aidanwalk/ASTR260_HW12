#Aidan Walk
#ASTR260-001
#28 April 2021, 17.00

#Problem 3

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    timestep = 1 #second
    tmax = 20000
    times = range(0, tmax, timestep)
    
    #atoms initially present
    numBi213 = 10000 
    numTi209 = numPb209 = numBi209 = 0
    
    #half life in min converted to second
    tauBi213 = 46*60 #seconds
    tauTi209 = 2.2*60 #seconds
    tauPb209 = 3.3*60 #seconds
    
    #probability of decay at any second
    chanceBi213 = 1 - 2**(-timestep/tauBi213)
    chanceTi209 = 1 - 2**(-timestep/tauTi209)
    chancePb209 = 1 - 2**(-timestep/tauPb209)
    chanceBitoTi = 0.0209
    
    #lists to append data to
    Bi213 = []
    Bi209 = []
    Ti209 = []
    Pb209 = []
    
    
    for time in times:
    
        #log data into lists
        Bi213.append(numBi213)
        Bi209.append(numBi209)
        Ti209.append(numTi209)
        Pb209.append(numPb209)
        
        #Decay Pb209 atoms 
        for Pb209Atom in range(numPb209):
            if np.random.random()<chancePb209:
                numPb209 -= 1
                numBi209 += 1
                
        #decay Ti209 atoms
        for Tl209Atom in range(numTi209):
            if np.random.random()<chanceTi209:
                numTi209 -= 1
                numPb209 += 1
                
        #decay Bi213 atoms
        for Bi213Atom in range(numBi213):
        
            if np.random.random()<chanceBi213:
                numBi213 -= 1 #1 atom decays
                if np.random.random()<chanceBitoTi:
                    numTi209 += 1 #atom decays into Ti209
                else: numPb209 += 1 #atom decays into Pb209
    
    
    #plot data
    plt.plot(times, Bi213, label='Bi213')
    plt.plot(times, Bi209, label='Bi209')
    plt.plot(times, Ti209, label='Ti209')
    plt.plot(times, Pb209, label='Pb209')
    
    plt.xlabel('Time [s]')
    plt.ylabel('Number of atoms')
    #plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.title('Bismuth 213 Radioactive Decay')
    
    #save plot
    plotFname = 'AidanWalk_HW12_3_Plot'+'.png'
    plt.savefig(plotFname, dpi=300)
    print('Plot saved to', plotFname)