import numpy
import pandas
from plotnine import *

#parsing fasta files


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
c1 = ggplot(seq_table) + theme_classic() + xlab("sequence Length") + ylab("count")
c1 + geom_histogram(aes(x = "sequenceLength"))

#Plotting the first histogrm of sequence lengths
c2 = ggplot(seq_table) + theme_classic() + xlab("GC content") + ylab("count")
c2 + geom_histogram(aes(x = "percentGC"))


