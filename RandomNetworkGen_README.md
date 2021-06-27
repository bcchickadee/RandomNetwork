Random Network Visualizer Program
윤수민

Objective of Program: We would like to visualize Random Networks (as featured in the 주탐 lecture about networks) using the matplotlib module in Python.

Characteristics of Random Network

cf) The previously developed Erdős–Rényi model featured a uniform probability for any node to be connected. Therefore, when a new edge is added to the network, that connection was independent from the previous configuration of the network.

In contrast, the probability in which two nodes are connected is not uniform in a Random Network. The probability depends on how many edges are connected to a node: the more edges connected, the more likely an additional edge could be connected to the node. The specific probability mass function (PMF) can vary by one’s discretion. In this program, we will feature 2 versions: one in which the probability is proportional with number of edges connected (to a node), and one in which the probability is proportional with that number squared. The second version was hypothesized to test a similarity between these random network visualizers and Newton’s law of physics.


Program Algorithm

The number of nodes and edges will be based on user input.
To keep track of how many edges there are connected to a node, we will make a list with a “Token” in it. One token refers to each node. Starting from 1, a token is defined by the number of edges connected to that referring node +1.

Therefore,
TokenList=[1, 1, 1, 1, …, 1] [len(TokenList)=Nodes)]

There has to be a list showing what edges are active; we name it EdgeList. Each edge is represented by a list: if Node 1 and 2 is connected, then the element [1, 2] will be added to EdgeList.

For every operation, we need to calculate each probability for each node to be selected; as a result, we make PList.
Furthermore, we need ContList, which shows the probability continuously (the sum of a node and all elements before a node). This is because we need to pick a node randomly, while also considering the tokens.

For the first operation, one selects two random nodes and then connects it.
