
library(readxl)
library(dplyr)

#step 1
winePag1 <- readxl::read_xlsx("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\ej-data-transformation\\Zinfandel Extended maceration, double pomace, 2 months bottle aging.xlsx",sheet="Sheet1")
winePag2 <- readxl::read_xlsx("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\ej-data-transformation\\Zinfandel Extended maceration, double pomace, 2 months bottle aging.xlsx",sheet="full scans")
write.csv(winePag1,file="C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\ej-data-transformation\\Zinfandel Extended maceration, double pomace, 2 months bottle aging.csv")
wineCSV <- read.csv("C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\ej-data-transformation\\Zinfandel Extended maceration, double pomace, 2 months bottle aging.csv")

#step 2
for(row in seq(3,422)){
  wavelen <- toString(winePag2[row,1])
  name <- substr(wavelen,1,8)
  wineCSV[name] <- " "
}
#colnames(wineCSV)

#step 3
for(col in seq(2,24,2)){
  fRow <- col / 2
  for(row in seq(3,422)){
    wavelen <- toString(winePag2[row,1])
    name <- substr(wavelen,1,8)
    wineCSV[fRow,name] <- toString(winePag2[row,col])
  }
}  
write.csv(winePag1,file="C:\\Users\\MrtC101\\Desktop\\Ciencias en Computacion\\Cursado\\3.2Inteligencia Artificial I\\repositorio\\ej-data-transformation\\Zinfandel Extended maceration, double pomace, 2 months bottle aging.csv")
