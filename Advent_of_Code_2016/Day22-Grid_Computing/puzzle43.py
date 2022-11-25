# You gain access to a massive storage cluster arranged in a grid; each storage node is only connected to the four 
# nodes directly adjacent to it (three if the node is on an edge, two if it's in a corner).

# You can directly access data only on node /dev/grid/node-x0-y0, but you can perform some limited actions on the 
# other nodes:

# You can get the disk usage of all nodes (via df). The result of doing this is in your puzzle input.
# You can instruct a node to move (not copy) all of its data to an adjacent node (if the destination node has 
# enough space to receive the data). The sending node is left empty after this operation.
# Nodes are named by their position: the node named node-x10-y10 is adjacent to nodes node-x9-y10, node-x11-y10, 
# node-x10-y9, and node-x10-y11.

# Before you begin, you need to understand the arrangement of data on these nodes. Even though you can only move 
# data between directly connected nodes, you're going to need to rearrange a lot of the data to get access to the 
# data you need. Therefore, you need to work out how you might be able to shift data around.

# To do this, you'd like to count the number of viable pairs of nodes. A viable pair is any two nodes (A,B), 
# regardless of whether they are directly connected, such that:

# Node A is not empty (its Used is not zero).
# Nodes A and B are not the same node.
# The data on node A (its Used) would fit on node B (its Avail).
# How many viable pairs of nodes are there?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day22-Grid_Computing\input.txt") as f:
    data = f.readlines()

#List of nodes
nodes = []

#Append nodes to the list
for line in data:
    nodes.append(line.strip().split())
#Remove the header
nodes = nodes[2:]

#Counter for viable pairs
viableParis = 0

#Double loop through all the nodes
for index1 in range(len(nodes)):

    #If A is not empty
    if nodes[index1][2] == "0T":
        continue

    for index2 in range(len(nodes)):

        #If A and B are not the same nodes
        if nodes[index1][0] == nodes[index2][0]:
            continue

        #If data on A could fit on node B
        if int(nodes[index1][2][:-1]) <= int(nodes[index2][3][:-1]):
            # Count it
            viableParis += 1

print("There are {} viable pairs of nodes!".format(viableParis))