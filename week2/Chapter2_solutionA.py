# Question 3.1 #
from Bio import SeqIO
genome = SeqIO.read("chr18.fa", "fasta")

# Question 3.2 #
total_length = len(genome)
print "The length is:", total_length

# Question 3.3 #
A_count = genome.seq.count('A')
C_count = genome.seq.count('C')
G_count = genome.seq.count('G')
T_count = genome.seq.count('T')
print 'A: %s, C: %s, G: %s, T: %s' % (A_count, C_count, G_count, T_count)

# Question 3.4 #
from Bio.SeqUtils import GC
print "The GC fraction is:", GC(genome.seq)

# Question 3.5 computing #
number_of_points = 10000
window_size      = total_length / number_of_points
positions        = range(0, total_length, window_size)
gc_values        = []
for pos in positions:
    start = pos
    stop  = pos + window_size
    gc_values.append(GC(genome[start:stop].seq))

# Question 3.5 plotting #
from matplotlib import pyplot
pyplot.plot(positions, gc_values)
pyplot.title("GC content with a window size of %i base pairs" % window_size)
pyplot.xlabel("Genome position [base pairs]")
pyplot.ylabel("GC content [%]")
pyplot.ion()

# Question 3.6 #
with open('binned_gc.txt', 'w') as f:
    for i in xrange(len(positions)):
        start = positions[i]
        stop  = positions[i] + window_size
        gc    = gc_values[i]
        f.write(str(start) + '\t' + str(stop) + '\t' + str(gc) + '\n')
