import numpy
import pandas
from plotnine import *

populations=pandas.read_csv("data.txt",sep=",",header=0)
westpop=[]
eastpop=[]
northpop=[]
southpop=[]

#Alternatively, you can use populations[populations.region=="west"] to get all entries with 'west' without the loops
for i in range(len(populations)):
    if populations.iloc[i,0] =="west":
        westpop.append(populations.iloc[i,1])
    elif populations.iloc[i,0] =="east":
        eastpop.append(populations.iloc[i,1])
    elif populations.iloc[i,0] =="north":
        northpop.append(populations.iloc[i,1])
    elif populations.iloc[i,0] =="south":
        southpop.append(populations.iloc[i,1])

Averageslist=[]
Populationslist=['W','E','N','S']

dfwest=pandas.DataFrame(list(zip(westpop)),columns=['Average'])
dfeast=pandas.DataFrame(list(zip(eastpop)),columns=['Average'])
dfnorth=pandas.DataFrame(list(zip(northpop)),columns=['Average'])
dfsouth=pandas.DataFrame(list(zip(southpop)),columns=['Average'])

dataframes=[dfwest,dfeast,dfnorth,dfsouth]

for i in dataframes:
    D=float(i.mean())
    Averageslist.append(D)


meansdf=pandas.DataFrame(list(zip(Populationslist,Averageslist)),columns=['Population','Averages'])

(ggplot(meansdf, aes(x='Population', y='Averages'))
 + geom_col()
 )

#You can use this one line of code for graphing the averages of all regions in a bar graph
ggplot(populations) + geom_bar(aes(x='factor(region)', y='observations', fill='factor(region)'), stat = "summary", fun_y = numpy.mean) + theme_classic() + xlab("region") + ylab("mean observations")
