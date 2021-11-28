import random
import time # only for execution times
import numpy as np

def eurojackpotWiningProbability():
    simulationNumber = 500000000
    gameMainNumbers = set(random.sample(range(1,51),5))
    gameSecondaryNumbers = set(random.sample(range(1,11),2))
    matrix = np.zeros((6,3))

    for _ in range(1,simulationNumber + 1):
        ticketMainNumbers = set(random.sample(range(1,51),5))
        ticketSecondaryNumbers = set(random.sample(range(1,11),2))

        x = gameMainNumbers.intersection(ticketMainNumbers)
        y = gameSecondaryNumbers.intersection(ticketSecondaryNumbers)

        matrix[len(x)][len(y)] +=1
    np.set_printoptions(suppress=True)
    print(np.true_divide(matrix,simulationNumber))

if __name__ == "__main__":
    start_time = time.time()
    eurojackpotWiningProbability()
    print("---Execution time: %s seconds ---" % (time.time() - start_time))