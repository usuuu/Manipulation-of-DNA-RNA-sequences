#! /usr/bin/python/

#Declare the variables 
difference = 0
sequence_1 = "GCACAGGTATCACATTCCCAGGAAGAGTATTCCCGGTTATGCCTGTTACAAGTGAGGCATCGAAAACAGGATAACCAGTACGGTCAGTAAGATCAGATCGTGGATTACGTCATTGGGCACCGTAGCTGCGGAATGTGCCCACGCTGAAATACCAGGGTCCGTTGTGAGCACTGAACAGAGCACATCTACTACAATTCCCTTCGACTAGAATGGATTACGGACAGGACTGCTCCTTCTGCTTACGCGTTGGCATACTGGCACGTGCGCCACTCCACGGGACATGAGTCATGTAGCTCTTGCACGTCACTGTTATTCCACGCTTTCCAAACTAGCTAATTCGTGTCTGGCGGTCTACTGATTGTGGACGCTGGCCGCGAATTTCGAGGCCAGAACTCGTGAGTAATCACATTGGGATACACGAACGAGATGATAAAGCCTACTTTCCTGCGACCCACGTCCGGGGTGTCATGCTATGCCGCAAGGCAAGGGTAGTAAGCGCTTCAGTGCCTTCCATCGGTATAACCGCCCCATTTCCACTAAATCTGCATTGGCTAGTTCTCAACAGCTGCCGGCACGGTGGATTGAATTGCCCGGAGTTTTCCATCATATCGCCAAGAAAACCTTTCTCGGAGAGCTGGTAGGGCAACGGCTAAGCCTATTCTGACAAAGTCCTAATATTACAACCTATTTGGCGTTGCCTTTTTAGCCTACAACAGTCAGTGTTCGTTACTCTTGTCAATTACCCTGATATGCTACTACATCAGAACCGTCATATCCGTAACTGGCACTAACTACATAATTGAGTTAAAGCCGTGTAGGCGTATAAGCAACCACGATTGGGGGGACTGTACCAAACTGTTGGGAACCTTTATAACACAGGTACGTGGGGGAACTCGGGGGCACGACGAACCGAATGCATAGGATACAGTT"
sequence_2 = "GTAGAACTTTCTGGCTGGGTTATATCGAAACACGGGTAGAGACTCTGGCATGAGGGTGGTCGAAAACGGGCACAGCTGGAACGTCATGGGTAGTCCATAGTAGATGGTGTTATGCCGCACCGATAACGATCCGTTTGCAACCTAGATTTCACACGGGAGCGATAGCAGTCCCGCGCGGGTCACCTTCCGGATAGCGGTCACCCGCACGATTTAATAGTGATAGGGGCACATCTTTATCCTGCATAGGTGGCATGACGCCACGTCCTAGCCTTTACGCGAGCTGAGCTTGCTCGATCTTGTGCGTCACACCCGGACCAACATGATGAGCCTAATACGGTACTGTCCACTGGCACGCGGATACTGTACCGTAGTGGGGATTTATGTGACAAGACCTCATAGATTCTTCTCTTGAGCTGCGTTCATGTTGAACTTAGTGTGGTTTTCAATTCACAGTCGTCGATGGTGTCTTTTCGGATCGAAAAAGTCGTTATGGATTCACTACATTGCCTACAATCTTGGACACCGCCTTATATGACCCCACGCAACGTTCAGCTCAACACCTCAGGTCCTGACACATGGGTTTGTATCACTTATGATGTGCGCCCAGATTTCTGATGAAACCCCTTATGCTGAACTGGTAGTGCCACGGGTGATCGTATGATCGACAATTCCTTGTTTTGCACCGTAACGCGGCTTCACCTAGACAGCCAGAGCTATAAGTGTTCAAGCCCCCAGTCAAGGCCCCTTTAGTACCACTACATCGGAACAGTACCATCGGAAACGGAAACCCACATGATACTAGTTTGGGCGCCGTTACGGACTGTTCACTGCCATGATTGGGGCGACTTCACCAAACTGGTAGGACTTTAAATCTCCGAAATCGCATCGGGATCCCATTGACGCAACGATATGGACCAACGGGCTTATCAG"


for i in range(0, len(sequence_1)):
    #Compare each nucleotide, if they differ increment the varibale difference.
  if sequence_1[i] != sequence_2[i]:
    difference+=1

print(difference)

    
