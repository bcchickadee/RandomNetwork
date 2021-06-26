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

NodeList=[]
Point1, Point2=random.randrange(1, nodes), random.randrange(1, nodes)
NodeList.append([Point1, Point2])
IList[Point1-1]=IList[Point1-1]+1
IList[Point2-1]=IList[Point2-1]+1
PLister()

for i in range(edges-1):
    #
