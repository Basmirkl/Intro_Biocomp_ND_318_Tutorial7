import numpy
import pandas
from plotnine import *

#Begin challenge 1!

#import raw data as array of lines
raw_data = numpy.loadtxt("Lecture11.fasta", dtype="string")
fasta_length = raw_data.tostring().count(">")

#create empty data frame with columns: sequenceID, sequenceLength, percentGC, meltingTemp
seq_table = pandas.DataFrame(numpy.zeros((fasta_length, 4)), columns=['sequenceID', 'sequenceLength', 'percentGC', 'meltingTemp'])

#loop through every other line, where i*2 is the headerID and i*2 + 1 is the sequence
for i in xrange(0, fasta_length, 1):
    seqID = raw_data[i * 2]
    seq = raw_data[i * 2 + 1]
    #record sequenceID
    seq_table.sequenceID[i] = seqID[1:]
    
    #record sequenceLength
    seq_table.sequenceLength[i] = len(seq)
    
    #count number of bases in the sequence
    num_c = seq.count("C")
    num_g = seq.count("G")
    num_a = seq.count("A")
    num_t = seq.count("T")
    
    #get GC percent
    seq_table.percentGC[i] = 100 * (num_c + num_g) / seq_table.sequenceLength[i]
    
    #meltingTemp = 4 x (#G + #C) + 2 x (#A + #T); only for length <= 14; else=-9999
    if seq_table.sequenceLength[i] <= 14:
        seq_table.meltingTemp[i] = 4 * (num_c + num_g) + 2 * (num_a + num_t)
    else:
        seq_table.meltingTemp[i] = -9999
seq_table

#Plotting the first histogrm of sequence lengths
ggplot(seq_table) + theme_classic() + xlab("sequence Length") + ylab("count") + geom_histogram(aes(x = "sequenceLength"))

#Plotting the first histogrm of sequence lengths
ggplot(seq_table) + theme_classic() + xlab("GC content") + ylab("count") + geom_histogram(aes(x = "percentGC"))


#Begin challenge 3!

populations=pandas.read_csv("data.txt",sep=",",header=0)
westpop=[]
eastpop=[]
northpop=[]
southpop=[]

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
ggplot(populations) + geom_bar(aes(x='factor(region)', y='observations'), stat = "summary", fun_y = numpy.mean) + theme_classic() + xlab("region") + ylab("mean observations")

#Code for scatter plot with jitter and color
ggplot(populations) + geom_point(aes(x="region", y="observations", color="factor(region)"), position = "jitter") + theme_classic() + xlab("region") + ylab("observations")



