# Import and define some libraries, this section of code is for GLOBAL code
# pylab is a tool that replicates matlab plotting windows in python 
import pylab

# numpy is a package for scientific computing, need this for a nice array object # np is an alias, you can refer to the modules as np.module instead of numpy.module 
import numpy as np

# matplotlib is essentialy what we plot with 
import matplotlib.pyplot as plt

# general system module, handles i/o, etc. 
import sys

# read in your data file
# see http://docs.python.org/2/tutorial/inputoutput.html, Sec 7.2
f = open('GlobularClusters_clean.tab','r')
header1 = f.readline()
name = []
ra = []
dec = []
for line in f:
    line = line.strip()
    columns = line.split()
    name1 = columns[0]
    name.append(name1)
    ra1 = float(columns[1])
    ra.append(ra1)
    dec1 = float(columns[2])
    dec.append(dec1)
f.close()
#print name
#print ra
#print dec
print min(ra),max(ra),min(dec),max(dec)

# Set up the plot 
pylab.figure(1) #initializes or focuses on figure 1 
pylab.clf() #clears the figure window

# Do the plotting 
#plt.plot(ra,dec) #send data to the plot 

plt.scatter(ra,dec) #send data to the plot 
plt.xlabel('RA') #label the x axis 
plt.ylabel('DEC') #label the y axis 
str_title = 'RA and DEC for Milky Way Globular Clusters' 
plt.title(str_title) #title 

plt.axis([0,360,-90,90]) #[xmin,xmax,ymin,ymax] 

print 'Figure is plotted, your command line is blocked until you close the plot.' 

plt.show() #show the plot and give control to the plotting window
