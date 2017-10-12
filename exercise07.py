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
(ggplot(seq_table) + theme_classic() + xlab("sequence Length") + ylab("count") 
    + geom_histogram(aes(x = "sequenceLength"))) #create histogram of sequence lengths

#Plotting the first histogrm of sequence lengths
(ggplot(seq_table) + theme_classic() + xlab("GC content") + ylab("count") 
    + geom_histogram(aes(x = "percentGC"))) #create histogram of percent GC

#Begin challenge 2!
#load csv of microbiome relative abundances
microbiome = pandas.read_csv("microbiome.csv")
#create scatterplot of Firmicutes vs Bacteroidetes with linear trendline
(ggplot(microbiome, aes(x = "Firmicutes", y = "Bacteroidetes")) #here we set each bacterial genus as an axis
    + geom_point() + stat_smooth(method="lm") #create scatter plot and linear trendline
    + theme_classic() + xlab("Firmicutes abundance") + ylab("Bacteroidetes abundance"))

#Begin challenge 3!

#read in csv
populations=pandas.read_csv("data.txt",sep=",",header=0)

#set up separate lists for observations for each region
westpop=[]
eastpop=[]
northpop=[]
southpop=[]

#Loop through populations dataframe and add observations to corresponding list
for i in range(len(populations)):
    if populations.iloc[i,0] =="west":
        westpop.append(populations.iloc[i,1])
    elif populations.iloc[i,0] =="east":
        eastpop.append(populations.iloc[i,1])
    elif populations.iloc[i,0] =="north":
        northpop.append(populations.iloc[i,1])
    elif populations.iloc[i,0] =="south":
        southpop.append(populations.iloc[i,1])
        
#Create empty list to hold the average for populations
Averageslist=[]
#Create list for region labels
Populationslist=['W','E','N','S']

#Create separate dataframe for each region
dfwest=pandas.DataFrame(list(zip(westpop)),columns=['Average'])
dfeast=pandas.DataFrame(list(zip(eastpop)),columns=['Average'])
dfnorth=pandas.DataFrame(list(zip(northpop)),columns=['Average'])
dfsouth=pandas.DataFrame(list(zip(southpop)),columns=['Average'])

#Create list of separate dataframes
dataframes=[dfwest,dfeast,dfnorth,dfsouth]

#Loop through lists of dataframes to add average obervations to averages list
for i in dataframes:
    D=float(i.mean())
    Averageslist.append(D)

#Finally make new dataframe of averages, appending region label list and average list
meansdf=pandas.DataFrame(list(zip(Populationslist,Averageslist)),columns=['Population','Averages'])

#plot these as bar graph in ggplot
(ggplot(meansdf, aes(x='Population', y='Averages'))
    + geom_col())


#(Alternatively) You can use this one line of code for graphing the averages of all regions in a bar graph
(ggplot(populations) + geom_bar(aes(x='factor(region)', y='observations'), stat = "summary", fun_y = numpy.mean) + theme_classic() 
    + xlab("region") + ylab("mean observations"))
    
#Code for scatter plot with jitter and color
ggplot(populations) + geom_point(aes(x="region", y="observations", color="factor(region)"), position = "jitter") + theme_classic() + xlab("region") + ylab("observations")
#The scatter plot allows us to see the range of all data points while in the bar graph, the raw data is hidden from view and we don't see the variation


