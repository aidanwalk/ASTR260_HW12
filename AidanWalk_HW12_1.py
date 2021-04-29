#Aidan Walk
#ASTR260-001
#28 April 2021, 17.00

#Problem 1 

import numpy as np
import matplotlib.pyplot as plt
    
if __name__ == '__main__':
    numberOfDice = 3
    numberOfRolls = 100000 #number of times to run simulation
    
    #initialize counts
    count = allSixesCount = 0
    #initialize list of sums
    sums = [0]*16
    possibleSums = range(3, 18+1)
    
    while count < numberOfRolls:
        roll = np.random.randint(1, 6+1, numberOfDice) #roll dice
        
        ''' This part solved part A for me
        #if all die are 6, add one to all sixes count
        if np.all(roll == 6): allSixesCount += 1
        '''
        #adds one to the index of the cooresponding sum value
        for sum in range(3, 18+1):
            if np.ndarray.sum(roll) == sum:
                sums[sum-3] += 1 #where "sums" index + 3 = value of dice sum
                break #after sum is found, no need to look at other sums 
        
        count += 1 #increment count by one
    
    
    #calculate probabilities
    '''probability_allSixes = allSixesCount/numberOfRolls''' #Also for part A
    sumsProbability = np.array(sums)/numberOfRolls
    
    
    #print answers
    print('\n\n'+'3 dice are rolled', numberOfRolls, 'times:')
    print('\n'+'The probability of rolling all sixes',
               'on any given roll is approximately {:.3%}'
                .format(sumsProbability[18-3]))
    print('The probability that all', numberOfDice,
               'dice will sum to 11 is {:.3%}'
               .format(sumsProbability[11-3]), '\n\n')
    
    
    #generate plot
    plt.bar(possibleSums, sumsProbability, color='k')
    plt.title('Rolling 3 Dice 100,000 Times')
    plt.xlabel('Sum of Dice Roll')
    plt.xticks(possibleSums)
    plt.ylabel('Probability of Occurance')
    
    #save plot
    plotFName = 'AidanWalk_HW12_1_Plot'+'.png'
    plt.savefig(plotFName, dpi=300)
    print('Plot saved to', plotFName)