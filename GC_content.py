#! /usr/bin/python/

#Import packages
from Bio.SeqUtils import GC
import re
import operator

#Declare variables
dict_seq_count = {} 

#Read in  the file
f = open("yourfilenamehere.txt", "r")

#Read each line of the file and store it in line.
for line in f:
    #If the line contains > it is a name of the sequence
    if ">" in line:
        #Store the name of the sequence in title. 
        #Remove white space and the > symbol
        title = re.sub('[\s>]',"",line)
        #Set seq to nothing
        seq = ""
    else: 
       # #Seq contains the sequence. Concatenate the sequence into one
        seq += re.sub('[\s]',"",line)
    #Calculate the total GC content of the sequence and store it in a dictionary. {name of sequence: GC content} 
    dict_seq_count[title] = GC(seq)


for i in dict_seq_count:
    print(i +"   " +str(dict_seq_count[i]))

#Sort the dictionary based on items in desending order.

#list the first item in the list. The name of the sequence with the highest GC content.
dict_sorted = list(dict(sorted(dict_seq_count.items(), key = lambda x: x[1], reverse = True)))[0]
print(dict_sorted)