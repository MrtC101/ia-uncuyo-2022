import Simulation
import Results as rs
import threading


def startSimulation(resultSet,size,dirt_rate,num):
    currSim = Simulation.Simulation(size,dirt_rate,num)
    currSim.run()
    currResults = currSim.get_Performance()
    if num == 1:
        random = "No"
    else:
        random = "Yes"    
    register = [random,str(size)+"x"+str(size),dirt_rate] + currResults
    resultSet.addRegister(register)

if __name__== "__main__":
    path="tp2-resultSet.csv"
    rateArr = [0.1, 0.2, 0.4, 0.8]
    arrSize = [2,4,8,16,32,64,128]
    #size = arrSize[random.randint(0,6)]
    #dirt_rate = rateArr[random.randint(0,3)]
    iter = 10
    resultSet = rs.Results(["Random","Environment_Size","Dirt_Rate","Time","Dirt_Cleaned","Dirt_Remaining"])
    for i in range(0,7):
        size = arrSize[i]
        for j in range(0,4):
            dirt_rate = rateArr[j]    
            for k in range(0,iter):
                sim1 = threading.Thread(target = startSimulation, args = (resultSet,size,dirt_rate,1))
                sim1.start()
                sim1.join()

    for i in range(0,7):
        size = arrSize[i]
        for j in range(0,4):
            dirt_rate = rateArr[j] 
            for k in range(0,iter):
                sim2 = threading.Thread(target = startSimulation, args = (resultSet,size,dirt_rate,2))
                sim2.start()
                sim2.join()

    resultSet.makeCSV(path)
    resultSet.plotBoxDiagram()