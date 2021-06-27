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

IList=[]
for i in range(nodes):
    IList.append(1)

PList=[]
def PLister():
    PList.clear()
    for Element in IList:
        PList.append(Element/(sum(IList)))

ContList=[]
def ContLister():
    ContList.clear()
    for i in range(len(PList)):
        ContList.append(sum(PList[0:i])/sum(PList))
    ContList.append(1)

EdgeList=[]
Point1, Point2=random.randrange(1, nodes), random.randrange(1, nodes)
EdgeList.append([Point1, Point2])
IList[Point1-1]=IList[Point1-1]+1
IList[Point2-1]=IList[Point2-1]+1
PLister()
ContLister()

for i in range(edges-1):
    Token=random.uniform(0, 1)
    while True:
        for i in range(len(ContList)-1):
            if ContList[i]<=Token<ContList[i+1]:
                EdgeList.append([i, i+1])
                IList[Point1-1]=IList[Point1-1]+1
                IList[Point2-1]=IList[Point2-1]+1
                PLister()
                ContLister()
                break

#Work in Progress..
