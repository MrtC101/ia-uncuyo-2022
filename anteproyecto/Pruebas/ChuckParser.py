import anvil

path=".\\chunkTest.csv"
chunksSize = 1

region = anvil.Region.from_file("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\Anteproyecto\\Minecraft\\Mundo nuevo\\region\\r.0.0.mca")
k = 0
blockList = []
for cx in range(0,chunksSize):
    for cz in range(0,chunksSize):
        chunk = anvil.Chunk.from_region(region, cx, cz)
        #get all blocks
        for x in range(0,15):
            for z in range(0,15):
                for y in range(0,225):
                    blockList.append([k,x,y,z,chunk.get_block(x,y,z).id])

with open(path,'w') as csvFile:
    csvFile.write(";Chuck;X;Y;Z;Tag\n")
    for i in range(1,len(blockList)):
        csvFile.write(str(i))
        for j in blockList[i]:
            csvFile.write(";"+str(j))
        csvFile.write("\n")  