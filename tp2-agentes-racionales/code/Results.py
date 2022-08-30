import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
class Results:
    index=0
    
    def __init__(self,head):
        self.resultSet = pd.DataFrame(columns=head)
        self.path = None
    
    def addRegister(self,register):
        self.resultSet.loc[self.index] = register
        self.index+=1

    def makeCSV(self,path):
        self.path=path
        pd.DataFrame.to_csv(self.resultSet,path)

    def plotBoxDiagram(self):
        plt.show()
        plt.pcol
        sns.set_theme()
        sns.set_style("dark")
        sns.color_palette("tab10")
        sns.axes_style()
        sns.catplot(x="Dirt_Cleaned",y="Environment_Size",hue="Random",kind="box",data=self.resultSet)
        plt.savefig("fig1.png")
        sns.catplot(x="Random",y="Dirt_Cleaned",col="Environment_Size",kind="box",data=self.resultSet)
        plt.savefig("fig2.png")
        sns.catplot(x="Random",y="Dirt_Cleaned",col="Dirt_Rate",kind="box",data=self.resultSet)
        plt.savefig("fig3.png")
        plt.show()
