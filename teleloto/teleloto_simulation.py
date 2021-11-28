import random
import time # only for execution times

def telelotoWiningProbability():
    ticketNumber = 50000000
    cornerWinners = 0
    lineWinners = 0
    crossWinners = 0
    tableWinners = 0

    for _ in range(1,ticketNumber + 1):
        # game setup
        gameNumbers = random.sample(range(1,76),75)
        firstStageNumbers = gameNumbers[0:37]
        secondStageNumbers = gameNumbers[0:47]
        # ticket generation
        mColumn = random.sample(range(1,16),5)
        jColumn = random.sample(range(16,31),5)
        rColumn = random.sample(range(31,46),5)
        gColumn = random.sample(range(46,61),5)
        zColumn = random.sample(range(61,76),5)
        # generated ticket parts
        corners = [mColumn[0],mColumn[4],zColumn[0],zColumn[4]]
        line = [mColumn[2],jColumn[2],rColumn[2],gColumn[2],zColumn[2]]
        cross = [mColumn[0],mColumn[4],jColumn[1],jColumn[3],rColumn[2],gColumn[1],gColumn[3],zColumn[0],zColumn[4]]
        table = mColumn + jColumn + rColumn + gColumn + zColumn
        # check for winning one of the game parts and adding to the total of the game
        if(set(corners).issubset(firstStageNumbers)):
            cornerWinners += 1
        if(set(line).issubset(firstStageNumbers)):
            lineWinners += 1
        if(set(cross).issubset(firstStageNumbers)):
            crossWinners += 1
        if(set(table).issubset(secondStageNumbers)):
            tableWinners += 1

    print("Total corner winners:" , cornerWinners, " probability: ", '{:.10f}'.format(cornerWinners / ticketNumber))
    print("Total line winners:" , lineWinners, " probability: ", '{:.10f}'.format(lineWinners / ticketNumber))
    print("Total cross winners:" , crossWinners, " probability: ", '{:.10f}'.format(crossWinners / ticketNumber))
    print("Total table winners:" , tableWinners, " probability: ", '{:.10f}'.format(tableWinners / ticketNumber))

if __name__ == "__main__":
    start_time = time.time()
    telelotoWiningProbability()
    print("---Execution time: %s seconds ---" % (time.time() - start_time))