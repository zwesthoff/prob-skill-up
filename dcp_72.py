"""Daily Coding Problem ----- Problem #72 [HARD]
4/7/2021

This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. 
We define a path's value as the number of most frequently-occurring 
letter along that path. For example, if a path in the graph goes through "ABACA", 
the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. 
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the 
uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed 
edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

 Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

 A
[(0, 0)]

Should return null, since we have an infinite loop.

.. _Google Python Style Guide:   
http://google.github.io/styleguide/pyguide.html
"""
#Class definitions
class Node():
    def __init__(self, val : str, neighbors = []):
        self.val = val
        self.neighbors = neighbors
        pass

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

#Function definitions
def createGraph(string, edgeList):
    vals = list(string)
    listOfNodes = []

    for node in vals:
        listOfNodes.append(Node(node))
    
    for i, j in edgeList:

        if listOfNodes[j] not in listOfNodes[i].neighbors:
            listOfNodes[i].add_neighbor(listOfNodes[j])


    return listOfNodes


def findLargestPath():
    pass

def main():
    string = 'ABACA'
    edgeList = [(0, 1),(0, 2),(2, 3),(3, 4)]

    graph = createGraph(string, edgeList)

    # print([[neighbor.val for neighbor in node.neighbors] for node in graph])
    print([neighbor.val for neighbor in graph[0].neighbors])
    return

if __name__=="__main__":
    main()


'''
Interesting Takeaways
---------------------


'''