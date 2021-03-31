# Erdős–Rényi model visualizer
# Random network visualizer
# Author: 윤수민

import matplotlib.pyplot as plt
import random
import numpy as np

while True:
    try:
        nodes=int(input('Number of Nodes: '))
    except ValueError:
        print('Error: Enter a valid integer.\n')
    if nodes<=0:
        print('Error: Enter a valid integer.\n')
    else:
        break

while True:
    try:
        p=float(input('Probability of Connection: '))
    except ValueError:
        print('Error: Enter a valid number from 0 to 1.\n')
    if p<0 or p>1:
        print('Error: Enter a valid number from 0 to 1.\n')
    else:
        break

NodeList=[]
NodePlot=[]
PossibleConnections=[]
RealConnections=[]

for i in range(nodes):
    for Element in NodeList:
        PossibleConnections.append([Element, i+1])
    NodeList.append(i+1)
    LocalX=random.gauss(0, nodes)
    LocalY=random.gauss(0, nodes)
    plt.plot(LocalX, LocalY, 'ro')
    plt.annotate(str(i+1), (LocalX, LocalY))
    NodePlot.append([LocalX, LocalY])

for i in PossibleConnections:
    token=random.uniform(0, 1)
    if token>p:
        Ident=0
    elif token<=p:
        Ident=1
    if Ident==1:
        RealConnections.append(i)

for i in RealConnections:
    p1, p2 = i[0], i[1]
    Plot1, Plot2 = NodePlot[p1-1], NodePlot[p2-1]
    x1, y1 = Plot1[0], Plot1[1]
    x2, y2 = Plot2[0], Plot2[1]
    x=np.arange(x1, x2, 0.01)
    y=((y2-y1)/(x2-x1))*(x-x1)+y1
    plt.plot(x, y, color='b')
        

print('\nNodes: '+str(NodeList))
print('Connections: '+str(RealConnections))
print('\n'+str(len(RealConnections))+' connections found of possible '+str(int(nodes*(nodes-1)/2))+' instances')
print('Density: '+str(len(RealConnections)/(nodes*(nodes-1)/2)))

#Adjacency Matrix Required!

plt.title('Random Network between '+str(nodes)+' Nodes')
plt.show()
