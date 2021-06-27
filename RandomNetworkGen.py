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
        edges=int(input('Number of Edges: '))
    except ValueError:
        print('Error: Enter a valid integer.\n')
    if edges<=0:
        print('Error: Enter a valid integer.\n')
    else:
        break

TokenList=[]
for i in range(nodes):
    TokenList.append(1)
# Initial token is 1.

PList=[]
def PLister():
    PList.clear()
    for Element in TokenList:
        PList.append(Element/(sum(TokenList)))
# PList is the relative frequency list of TokenList

ContList=[]
def ContLister():
    ContList.clear()
    for i in range(len(PList)):
        ContList.append(sum(PList[0:i]))
    ContList.append(1)
# ContList is the sum of probabilities, from node 1 to a specific node

EdgeList=[]
Point1, Point2=random.randint(1, nodes), random.randint(1, nodes)
EdgeList.append([Point1, Point2])
# For the initial trial, select two random nodes and link them

TokenList[(Point1)-1]=TokenList[(Point1)-1]+1
TokenList[(Point2)-1]=TokenList[(Point2)-1]+1
# Add 1 to each token of Point1 and Point2
PLister()
ContLister()
# Refresh PList and ContList based on the new token data

NodePlot=[]
for i in range(nodes):
    x=random.gauss(0, nodes)
    y=random.gauss(0, nodes)
    NodePlot.append([x, y])
    plt.plot(x, y, 'ro')
    plt.annotate(str(i+1), (x, y))
# For visualization, randomly visualize dots (following a Gaussian distribtion).
# Visualization enhancement: for nodes with many edges, we want them to be close to the center.
# Therefore, we use the PList element; the distance from the center should be the inverse of the element.
# The angle in which the element is located from the center is decided randomly (random.uniform).
# In conclusion, the NodePlot and plotting section should be moved to the back so that PList works.

for i in range(edges-1):
    RT1=random.uniform(0, 1)
    RT2=random.uniform(0, 1)
    while True:
        for i in range(len(ContList)-1):
            if ContList[i]<=RT1<ContList[i+1]:
                P1=i+1
                break
    while True:
        for i in range(len(ContList)-1):
            if ContList[i]<=RT2<ContList[i+1]:
                P2=i+1
                break
    EdgeList.append([P1, P2])
    TokenList[(P1)-1]=TokenList[(P1)-1]+1
    TokenList[(P2)-1]=TokenList[(P2)-1]+1
    PLister()
    ContLister()

print(EdgeList)

for i in EdgeList:
    Q1, Q2 = i[0], i[1]
    Dot1, Dot2 = NodePlot[Q1-1], NodePlot[Q2-1]
    x1, y1 = Dot1[0], Dot1[1]
    x2, y2 = Dot2[0], Dot2[1]
    x=np.arange(x1, x2, 0.01)
    y=((y2-y1)/(x2-x1))*(x-x1)+y1
    plt.plot(x, y, color='b')

# Work in Progress..
# Adjacency Matrix Required!

print('Density: '+str((edges)/(nodes*(nodes-1)/2)))
plt.title('Random Network of '+str(nodes)+' Nodes and '+str(edges)+' Edges')
plt.show()
