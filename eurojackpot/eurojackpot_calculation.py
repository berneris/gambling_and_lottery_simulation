# Theoretical posibilities of Eurojackpot;
# N - How many numbers there is;
# K - How many numbers to choose;
# B - How many numbers to guess;

import time # only for execution times
import math
import numpy as np

def probability(N:int, K:int, B:int):
    return (math.factorial(K)/(math.factorial(B)*math.factorial(K-B)))*(math.factorial(N-K)/(math.factorial(K-B)*math.factorial(N-2*K+B)))*(math.factorial(K)*math.factorial(N-K)/math.factorial(N))

def eurojackpotProbability(MainNumber:int, SecondaryNumber:int):
    return probability(50,5,MainNumber)*probability(10,2,SecondaryNumber)

def eurojackpotWiningProbability():
    matrix = np.zeros((6,3))
    np.set_printoptions(suppress=True)
    for x in range(0,6):
        for y in range(0,3):
            matrix[x][y] = eurojackpotProbability(x,y)
    print(matrix)

if __name__ == "__main__":
    start_time = time.time()
    eurojackpotWiningProbability()
    print("---Execution time: %s seconds ---" % (time.time() - start_time))