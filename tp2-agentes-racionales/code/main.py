import Simulation
import threading

def writeInConsole(result):
    print("Tiempo nesesario: ",end="")
    print(result[0])
    print("Cantidad de suciedad limpiada: ",end="")
    print(result[1])
    print("cantidad de suciedad faltante: ",end="")
    print(result[2])    

def firstLine():
    file = open("tp2-results.csv",'a')
    try:
        file.write("\n|Random|Size|Dirt Rate|   Time    |   Score   |Remaining Dirt|\n"
            +  "|:-------:|:--:|:-------:|:---------:|:---------:|:------------:|\n")
    finally:
        file.close()

def writeInFile(result,size,rate,num):    
    if num == 1:
        rand="No"
    elif num ==2:
        rand="Si"
    text = "|"+rand+"|"+str(size)+"x"+str(size)+"|"+str(rate)+"|    "+ str(result[0]) + "  |   " + str(result[1]) + "   |   " + str(result[2]) + "    |\n"
    file = open("tp2-results.csv",'a')
    try:
        file.write(text) 
    finally:
        file.close()

def startSimulation(size,dirt_rate,num):
    currSim = Simulation.Simulation(size,dirt_rate,num)
    currSim.run()
    result = currSim.get_Performance()
    writeInFile(result,size,dirt_rate,num)

if __name__== "__main__":
    rateArr = [0.1, 0.2, 0.4, 0.8]
    arrSize = [2,4,8,16,32,64,128]
    #size = arrSize[random.randint(0,6)]
    #dirt_rate = rateArr[random.randint(0,3)]
    iter = 10
    for i in range(0,4):
        firstLine()
        dirt_rate = rateArr[i]
        for j in range(0,7):
            size = arrSize[j]
            for k in range(0,iter):
                sim1 = threading.Thread(target = startSimulation, args = (size,dirt_rate,1))
                sim1.start()
                sim1.join()

    for i in range(0,4):
        firstLine()
        dirt_rate = rateArr[i]
        for j in range(0,7):
            size = arrSize[j]
            for k in range(0,iter):
                sim2 = threading.Thread(target = startSimulation, args = (size,dirt_rate,2))
                sim2.start()
                sim2.join()